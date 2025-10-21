#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
USB Manager - Advanced USB Drive File Management and Security Tool

Copyright (c) 2025 Burak. All rights reserved.
This software is proprietary. Unauthorized use is prohibited.
"""

import os
import psutil
import ctypes
from ctypes import wintypes
import threading
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox, filedialog
import subprocess
import shutil

# --- Windows API ---
kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
GetFileAttributesW = kernel32.GetFileAttributesW
GetFileAttributesW.argtypes = [wintypes.LPCWSTR]
GetFileAttributesW.restype = wintypes.DWORD

GetVolumeInformationW = kernel32.GetVolumeInformationW
GetVolumeInformationW.argtypes = [
    wintypes.LPCWSTR,  # lpRootPathName
    wintypes.LPWSTR,   # lpVolumeNameBuffer
    wintypes.DWORD,    # nVolumeNameSize
    wintypes.LPDWORD,  # lpVolumeSerialNumber
    wintypes.LPDWORD,  # lpMaximumComponentLength
    wintypes.LPDWORD,  # lpFileSystemFlags
    wintypes.LPWSTR,   # lpFileSystemNameBuffer
    wintypes.DWORD     # nFileSystemNameSize
]
GetVolumeInformationW.restype = wintypes.BOOL

FILE_ATTRIBUTE_HIDDEN = 0x2
FILE_ATTRIBUTE_SYSTEM = 0x4
MAX_READ_BYTES = 4096

# Varsayılan dosya adı ve token
DEFAULT_FILENAME = "a3f9c7b2.dat"
DEFAULT_TOKEN = "USB-AUTH-2442C3D3"


def get_volume_label(drive_path):
    """Sürücünün etiket ismini al"""
    try:
        if not drive_path.endswith('\\'):
            drive_path += '\\'
        
        volume_name_buffer = ctypes.create_unicode_buffer(261)
        file_system_name_buffer = ctypes.create_unicode_buffer(261)
        serial_number = wintypes.DWORD()
        max_component_length = wintypes.DWORD()
        file_system_flags = wintypes.DWORD()
        
        result = GetVolumeInformationW(
            drive_path,
            volume_name_buffer,
            261,
            ctypes.byref(serial_number),
            ctypes.byref(max_component_length),
            ctypes.byref(file_system_flags),
            file_system_name_buffer,
            261
        )
        
        if result:
            volume_name = volume_name_buffer.value
            return volume_name if volume_name else "İsimsiz Sürücü"
        else:
            return "İsimsiz Sürücü"
    except Exception:
        return "İsimsiz Sürücü"


def get_removable_drives():
    """Takılı USB flash sürücüleri listele"""
    drives = []
    for p in psutil.disk_partitions(all=False):
        if "removable" in p.opts.lower() or p.fstype.lower() in ["fat32", "exfat"]:
            try:
                usage = psutil.disk_usage(p.mountpoint)
                size_gb = usage.total / (1024**3)
                label = get_volume_label(p.mountpoint)
                drives.append({
                    'device': p.device,
                    'mountpoint': p.mountpoint,
                    'fstype': p.fstype,
                    'size': f"{size_gb:.2f} GB",
                    'label': label
                })
            except Exception:
                drives.append({
                    'device': p.device,
                    'mountpoint': p.mountpoint,
                    'fstype': p.fstype,
                    'size': 'N/A',
                    'label': 'İsimsiz Sürücü'
                })
    return drives


def is_hidden_or_system(path: str) -> bool:
    """Dosyanın gizli veya sistem dosyası olup olmadığını kontrol et"""
    try:
        attrs = GetFileAttributesW(path)
        if attrs == 0xFFFFFFFF:
            return False
        return bool(attrs & (FILE_ATTRIBUTE_HIDDEN | FILE_ATTRIBUTE_SYSTEM))
    except Exception:
        return False


def maybe_text_sample(data: bytes, max_chars=1000):
    """Binary veriden metin örneği çıkar"""
    if not data:
        return ""
    if b'\x00' in data:
        return None
    try:
        text = data.decode('utf-8', errors='replace')
    except Exception:
        return None
    return text[:max_chars]


def scan_drive_for_hidden(root_path: str, callback_print, stop_event):
    """Sürücüdeki gizli dosyaları tara"""
    total_found = 0
    found_files = []
    callback_print(f"🔍 Tarama başlatıldı: {root_path}\n", "info")
    
    for dirpath, dirnames, filenames in os.walk(root_path, topdown=True,
                                                onerror=lambda e: callback_print(f"❌ Hata: {e}\n", "error")):
        if stop_event.is_set():
            raise KeyboardInterrupt()
            
        for fname in filenames:
            if stop_event.is_set():
                raise KeyboardInterrupt()
                
            full = os.path.join(dirpath, fname)
            try:
                if is_hidden_or_system(full):
                    total_found += 1
                    found_files.append(full)
                    callback_print(f"📁 [{total_found}] {full}\n", "found")
                    
                    try:
                        with open(full, "rb") as f:
                            sample = f.read(MAX_READ_BYTES)
                    except Exception as e:
                        callback_print(f"   ⚠️ Okunamadı: {e}\n\n", "warning")
                        continue

                    text_sample = maybe_text_sample(sample)
                    if text_sample is None:
                        callback_print("   📦 Binary dosya\n\n", "info")
                    else:
                        callback_print("   📄 İçerik örneği:\n", "info")
                        for line in text_sample.splitlines()[:10]:
                            callback_print(f"   {line}\n", "content")
                        callback_print("\n", "info")
            except Exception as e:
                continue
                
    callback_print(f"✅ Tarama tamamlandı. Toplam {total_found} gizli dosya bulundu.\n", "success")
    return found_files


class USBManagerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("USB Flash Sürücü Yöneticisi - Gelişmiş Araç")
        self.geometry("1100x700")
        self.configure(bg="#f0f0f0")
        
        # İkon ayarla
        try:
            # assets klasöründen ikonu yükle
            icon_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "tool.ico")
            if os.path.exists(icon_path):
                self.iconbitmap(icon_path)
        except Exception:
            pass
        
        # Renkler
        self.colors = {
            'bg': '#f0f0f0',
            'primary': '#2196F3',
            'success': '#4CAF50',
            'danger': '#f44336',
            'warning': '#FF9800',
            'dark': '#212121',
            'light': '#ffffff'
        }
        
        self._scan_thread = None
        self._stop_event = threading.Event()
        self.found_files = []
        self.drive_data = []  # Sürücü bilgilerini saklamak için
        
        self.create_widgets()
        self.populate_drives()
        
    def create_widgets(self):
        # Başlık
        header = tk.Frame(self, bg=self.colors['primary'], height=60)
        header.pack(fill="x")
        header.pack_propagate(False)
        
        title_label = tk.Label(header, text="🔧 USB Flash Sürücü Yönetim Merkezi", 
                              font=("Segoe UI", 16, "bold"), 
                              bg=self.colors['primary'], 
                              fg=self.colors['light'])
        title_label.pack(pady=15)
        
        # Ana container
        main_container = ttk.Frame(self)
        main_container.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Sol panel - Sürücü Seçimi ve İşlemler
        left_panel = ttk.LabelFrame(main_container, text="📌 Sürücü Bilgileri ve İşlemler", padding=10)
        left_panel.pack(side="left", fill="both", expand=True, padx=(0, 5))
        
        # Sürücü seçimi
        drive_frame = ttk.Frame(left_panel)
        drive_frame.pack(fill="x", pady=(0, 10))
        
        ttk.Label(drive_frame, text="USB Sürücü:", font=("Segoe UI", 10, "bold")).pack(anchor="w")
        
        drive_select_frame = ttk.Frame(drive_frame)
        drive_select_frame.pack(fill="x", pady=5)
        
        self.drive_combo = ttk.Combobox(drive_select_frame, state="readonly", width=40, font=("Segoe UI", 9))
        self.drive_combo.pack(side="left", fill="x", expand=True)
        self.drive_combo.bind("<<ComboboxSelected>>", self.on_drive_selected)
        
        ttk.Button(drive_select_frame, text="🔄 Yenile", command=self.populate_drives, width=12).pack(side="left", padx=(5, 0))
        
        # Sürücü detayları
        self.drive_info_label = ttk.Label(drive_frame, text="", font=("Segoe UI", 9), foreground="#666")
        self.drive_info_label.pack(anchor="w", pady=5)
        
        # Notebook (Sekmeler)
        self.notebook = ttk.Notebook(left_panel)
        self.notebook.pack(fill="both", expand=True)
        
        # Sekme 1: Dosya Oluştur
        create_tab = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(create_tab, text="📝 Dosya Oluştur")
        
        ttk.Label(create_tab, text="Dosya Adı:", font=("Segoe UI", 9)).pack(anchor="w", pady=(5, 2))
        self.filename_entry = ttk.Entry(create_tab, width=40, font=("Segoe UI", 9))
        self.filename_entry.pack(fill="x", pady=(0, 10))
        self.filename_entry.insert(0, DEFAULT_FILENAME)
        
        ttk.Label(create_tab, text="İçerik (Çok satırlı metin):", font=("Segoe UI", 9)).pack(anchor="w", pady=(5, 2))
        self.content_text = scrolledtext.ScrolledText(create_tab, height=10, font=("Consolas", 9), wrap="word")
        self.content_text.pack(fill="both", expand=True, pady=(0, 10))
        self.content_text.insert("1.0", DEFAULT_TOKEN)
        
        options_frame = ttk.Frame(create_tab)
        options_frame.pack(fill="x", pady=5)
        
        self.hide_file_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(options_frame, text="Dosyayı gizle", variable=self.hide_file_var).pack(side="left", padx=5)
        
        self.system_file_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(options_frame, text="Sistem dosyası yap", variable=self.system_file_var).pack(side="left", padx=5)
        
        self.readonly_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(options_frame, text="Salt okunur", variable=self.readonly_var).pack(side="left", padx=5)
        
        create_btn_frame = ttk.Frame(create_tab)
        create_btn_frame.pack(fill="x", pady=10)
        
        ttk.Button(create_btn_frame, text="✅ Dosyayı Oluştur", command=self.create_file, style="Success.TButton").pack(fill="x")
        
        # Sekme 2: Gizli Dosya Tarama
        scan_tab = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(scan_tab, text="🔍 Gizli Dosya Tara")
        
        scan_controls = ttk.Frame(scan_tab)
        scan_controls.pack(fill="x", pady=(0, 10))
        
        ttk.Button(scan_controls, text="▶️ Taramayı Başlat", command=self.start_scan, width=20).pack(side="left", padx=2)
        ttk.Button(scan_controls, text="⏹️ Durdur", command=self.stop_scan, width=15).pack(side="left", padx=2)
        ttk.Button(scan_controls, text="🧹 Temizle", command=self.clear_output, width=15).pack(side="left", padx=2)
        
        ttk.Label(scan_tab, text="Tarama yapılacak sürücüyü yukarıdan seçin.", 
                 font=("Segoe UI", 9), foreground="#666").pack(anchor="w", pady=5)
        
        # Sağ panel - Bulunan Dosyalar
        right_panel = ttk.LabelFrame(main_container, text="📋 Bulunan Gizli Dosyalar", padding=10)
        right_panel.pack(side="left", fill="both", expand=True, padx=(5, 0))
        
        # Arama çubuğu
        search_frame = ttk.Frame(right_panel)
        search_frame.pack(fill="x", pady=(0, 5))
        
        ttk.Label(search_frame, text="🔎 Filtre:", font=("Segoe UI", 9)).pack(side="left", padx=2)
        self.search_entry = ttk.Entry(search_frame, font=("Segoe UI", 9))
        self.search_entry.pack(side="left", fill="x", expand=True, padx=2)
        self.search_entry.bind("<KeyRelease>", self.filter_output)
        
        # Çıktı alanı
        output_frame = ttk.Frame(right_panel)
        output_frame.pack(fill="both", expand=True)
        
        # Scrollbar ve Text widget
        scrollbar = ttk.Scrollbar(output_frame)
        scrollbar.pack(side="right", fill="y")
        
        self.output = tk.Text(output_frame, wrap="none", font=("Consolas", 9), 
                             yscrollcommand=scrollbar.set, bg="#1e1e1e", fg="#d4d4d4",
                             insertbackground="white", selectbackground="#264f78")
        self.output.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.output.yview)
        
        # Metin renklendirme tagları
        self.output.tag_config("info", foreground="#4FC3F7")
        self.output.tag_config("success", foreground="#66BB6A")
        self.output.tag_config("error", foreground="#EF5350")
        self.output.tag_config("warning", foreground="#FFA726")
        self.output.tag_config("found", foreground="#FFD54F", font=("Consolas", 9, "bold"))
        self.output.tag_config("content", foreground="#B0BEC5")
        
        # Dosya seçimi için Combobox
        file_select_frame = ttk.Frame(right_panel)
        file_select_frame.pack(fill="x", pady=(5, 0))
        
        ttk.Label(file_select_frame, text="Dosya Seçimi:", font=("Segoe UI", 9, "bold")).pack(anchor="w", pady=2)
        
        self.file_combo = ttk.Combobox(file_select_frame, state="readonly", font=("Segoe UI", 8))
        self.file_combo.pack(fill="x", pady=2)
        self.file_combo.bind("<<ComboboxSelected>>", self.on_file_selected)
        
        # Dosya işlemleri
        file_ops_frame = ttk.Frame(right_panel)
        file_ops_frame.pack(fill="x", pady=(5, 0))
        
        ttk.Label(file_ops_frame, text="Seçili Dosya İşlemleri:", font=("Segoe UI", 9, "bold")).pack(anchor="w", pady=2)
        
        ops_buttons = ttk.Frame(file_ops_frame)
        ops_buttons.pack(fill="x", pady=2)
        
        ttk.Button(ops_buttons, text="🗑️ Seçili Dosyayı Sil", command=self.delete_selected, width=20).pack(side="left", padx=2)
        ttk.Button(ops_buttons, text="👁️ Dosya Özelliklerini Göster", command=self.show_file_properties, width=25).pack(side="left", padx=2)
        
        ops_buttons2 = ttk.Frame(file_ops_frame)
        ops_buttons2.pack(fill="x", pady=2)
        
        ttk.Button(ops_buttons2, text="📋 USB'ye Kopyala", command=self.copy_to_usb, width=20).pack(side="left", padx=2)
        ttk.Button(ops_buttons2, text="💾 Raporu Kaydet", command=self.save_report, width=18).pack(side="left", padx=2)
        
        # Durum çubuğu
        status_frame = tk.Frame(self, bg=self.colors['dark'], height=30)
        status_frame.pack(fill="x", side="bottom")
        status_frame.pack_propagate(False)
        
        self.status_var = tk.StringVar(value="✅ Hazır")
        status_label = tk.Label(status_frame, textvariable=self.status_var, 
                               font=("Segoe UI", 9), bg=self.colors['dark'], 
                               fg=self.colors['light'], anchor="w", padx=10)
        status_label.pack(fill="both")
        
    def populate_drives(self):
        """Sürücüleri yenile"""
        drives = get_removable_drives()
        display = []
        self.drive_data = drives  # Sürücü verilerini sakla
        
        for d in drives:
            display.append(f"{d['mountpoint']} - {d['label']} - {d['fstype']} ({d['size']})")
        
        if not display:
            display = ["❌ Hiçbir USB sürücü bulunamadı"]
            self.drive_data = []
            
        self.drive_combo["values"] = display
        if display and not display[0].startswith("❌"):
            self.drive_combo.current(0)
            self.on_drive_selected(None)
        else:
            self.drive_info_label.config(text="USB flash sürücü takın ve yenile butonuna basın.")
            
    def on_drive_selected(self, event):
        """Sürücü seçildiğinde bilgileri göster"""
        sel = self.drive_combo.get()
        if sel and not sel.startswith("❌"):
            try:
                mountpoint = sel.split()[0]
                usage = psutil.disk_usage(mountpoint)
                free_gb = usage.free / (1024**3)
                used_gb = usage.used / (1024**3)
                percent = usage.percent
                
                info_text = f"💾 Boş: {free_gb:.2f} GB | Kullanılan: {used_gb:.2f} GB | Dolu: %{percent:.1f}"
                self.drive_info_label.config(text=info_text)
            except Exception as e:
                self.drive_info_label.config(text=f"⚠️ Bilgi alınamadı: {e}")
                
    def create_file(self):
        """Flash sürücüde dosya oluştur"""
        disk = self.drive_combo.get()
        if not disk or disk.startswith("❌"):
            messagebox.showerror("Hata", "Lütfen geçerli bir USB sürücü seçin.")
            return
            
        disk = disk.split()[0]
        if not disk.endswith("\\"):
            disk += "\\"

        filename = self.filename_entry.get().strip()
        if not filename:
            messagebox.showerror("Hata", "Lütfen bir dosya adı girin.")
            return
            
        content = self.content_text.get("1.0", "end-1c")
        filepath = os.path.join(disk, filename)

        try:
            # Dosya oluştur
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            
            # Dosya özniteliklerini ayarla
            attrib_cmd = ["attrib"]
            if self.hide_file_var.get():
                attrib_cmd.append("+h")
            if self.system_file_var.get():
                attrib_cmd.append("+s")
            if self.readonly_var.get():
                attrib_cmd.append("+r")
            attrib_cmd.append(filepath)
            
            if len(attrib_cmd) > 2:
                subprocess.run(attrib_cmd, check=True)
            
            messagebox.showinfo("Başarılı", f"✅ Dosya başarıyla oluşturuldu!\n\n📁 Konum: {filepath}\n📝 Boyut: {len(content)} karakter")
            self.status_var.set(f"✅ Dosya oluşturuldu: {filename}")
        except Exception as e:
            messagebox.showerror("Hata", f"❌ Dosya oluşturulamadı:\n{e}")
            self.status_var.set("❌ Dosya oluşturma başarısız")
            
    def start_scan(self):
        """Taramayı başlat"""
        if self._scan_thread and self._scan_thread.is_alive():
            messagebox.showinfo("Zaten Çalışıyor", "Tarama zaten devam ediyor.")
            return
            
        sel = self.drive_combo.get()
        if not sel or sel.startswith("❌"):
            messagebox.showwarning("Sürücü Seçin", "Lütfen taranacak bir USB sürücü seçin.")
            return
            
        root_path = sel.split()[0]
        if not root_path.endswith("\\"):
            root_path += "\\"

        self._stop_event.clear()
        self.found_files = []
        self.output.delete("1.0", "end")
        self.output.insert("end", f"═══════════════════════════════════════════════════════\n", "info")
        self.output.insert("end", f"  🔍 GİZLİ DOSYA TARAMASI BAŞLATILDI\n", "info")
        self.output.insert("end", f"═══════════════════════════════════════════════════════\n\n", "info")
        
        self.status_var.set(f"🔍 {root_path} taranıyor...")
        self._scan_thread = threading.Thread(target=self._scan_worker, args=(root_path,), daemon=True)
        self._scan_thread.start()
        
    def stop_scan(self):
        """Taramayı durdur"""
        if self._scan_thread and self._scan_thread.is_alive():
            self._stop_event.set()
            self.status_var.set("⏹️ Durduruluyor...")
        else:
            self.status_var.set("ℹ️ Çalışan tarama yok.")
            
    def _scan_worker(self, root_path):
        """Tarama iş parçacığı"""
        def cb_print(msg, tag="info"):
            if self._stop_event.is_set():
                raise KeyboardInterrupt()
            self.output.insert("end", msg, tag)
            self.output.see("end")
            
        try:
            self.found_files = scan_drive_for_hidden(root_path, callback_print=cb_print, stop_event=self._stop_event)
            self.update_file_combo()
            self.status_var.set(f"✅ Tarama tamamlandı. {len(self.found_files)} dosya bulundu.")
        except KeyboardInterrupt:
            self.output.insert("end", "\n⏹️ Tarama kullanıcı tarafından durduruldu.\n", "warning")
            self.status_var.set("⏹️ Tarama durduruldu.")
        except Exception as e:
            self.output.insert("end", f"\n❌ Tarama sırasında hata: {e}\n", "error")
            self.status_var.set("❌ Hata oluştu.")
    
    def update_file_combo(self):
        """Bulunan dosyaları combobox'a ekle"""
        if not self.found_files:
            self.file_combo["values"] = ["❌ Bulunan dosya yok"]
            return
        
        display_files = []
        for idx, filepath in enumerate(self.found_files, 1):
            filename = os.path.basename(filepath)
            display_files.append(f"[{idx}] {filename} - {filepath}")
        
        self.file_combo["values"] = display_files
        if display_files:
            self.file_combo.current(0)
    
    def on_file_selected(self, event):
        """Combobox'tan dosya seçildiğinde"""
        sel = self.file_combo.get()
        if sel and not sel.startswith("❌"):
            # Dosya yolunu çıkar
            if "]" in sel:
                parts = sel.split("]", 1)
                if len(parts) == 2:
                    filepath = parts[1].split(" - ", 1)[-1]
                    # Output'ta ilgili satırı vurgula
                    self.highlight_file_in_output(filepath)
    
    def highlight_file_in_output(self, filepath):
        """Output'ta dosyayı vurgula"""
        content = self.output.get("1.0", "end")
        if filepath in content:
            start = content.index(filepath)
            line_num = content[:start].count('\n') + 1
            self.output.tag_remove("sel", "1.0", "end")
            self.output.tag_add("sel", f"{line_num}.0", f"{line_num}.end")
            self.output.see(f"{line_num}.0")
            
    def get_selected_file(self):
        """Seçili dosya yolunu al (combobox veya output'tan)"""
        # Önce combobox'u kontrol et
        combo_sel = self.file_combo.get()
        if combo_sel and not combo_sel.startswith("❌"):
            if "]" in combo_sel:
                parts = combo_sel.split("]", 1)
                if len(parts) == 2:
                    filepath = parts[1].split(" - ", 1)[-1]
                    if os.path.exists(filepath):
                        return filepath
        
        # Eğer combobox'tan alınamazsa, output'tan dene
        try:
            sel_text = self.output.get("sel.first", "sel.last").strip()
            if "]" in sel_text:
                parts = sel_text.split("]", 1)
                if len(parts) == 2:
                    sel_text = parts[1].strip()
            if sel_text and os.path.exists(sel_text):
                return sel_text
        except tk.TclError:
            pass
        
        return None
    
    def delete_selected(self):
        """Seçili dosyayı sil"""
        filepath = self.get_selected_file()
        
        if not filepath:
            messagebox.showwarning("Seçim Yok", "Lütfen silmek istediğiniz dosyayı seçin (combobox veya output alanından).")
            return
            
        confirm = messagebox.askyesno("Onay", f"⚠️ Bu dosyayı kalıcı olarak silmek istediğinizden emin misiniz?\n\n📁 {filepath}")
        if not confirm:
            return
            
        try:
            # Öznitelikleri kaldır
            subprocess.run(["attrib", "-h", "-s", "-r", filepath], check=False)
            os.remove(filepath)
            
            messagebox.showinfo("Başarılı", f"✅ Dosya başarıyla silindi:\n{filepath}")
            self.output.insert("end", f"\n🗑️ [SİLİNDİ] {filepath}\n", "success")
            self.status_var.set(f"✅ Dosya silindi: {os.path.basename(filepath)}")
            
            if filepath in self.found_files:
                self.found_files.remove(filepath)
                self.update_file_combo()
        except Exception as e:
            messagebox.showerror("Hata", f"❌ Dosya silinemedi:\n{e}")
            self.status_var.set("❌ Silme işlemi başarısız")
            
    def show_file_properties(self):
        """Seçili dosyanın özelliklerini göster"""
        filepath = self.get_selected_file()
        
        if not filepath:
            messagebox.showwarning("Seçim Yok", "Lütfen bir dosya seçin (combobox veya output alanından).")
            return
            
        try:
            stats = os.stat(filepath)
            size = stats.st_size
            
            if size < 1024:
                size_str = f"{size} B"
            elif size < 1024**2:
                size_str = f"{size/1024:.2f} KB"
            else:
                size_str = f"{size/(1024**2):.2f} MB"
                
            attrs = GetFileAttributesW(filepath)
            is_hidden = bool(attrs & FILE_ATTRIBUTE_HIDDEN)
            is_system = bool(attrs & FILE_ATTRIBUTE_SYSTEM)
            
            info = f"""
📁 Dosya Özellikleri
{'='*50}

📄 Dosya: {os.path.basename(filepath)}
📂 Konum: {os.path.dirname(filepath)}
💾 Boyut: {size_str}
🔒 Gizli: {'Evet' if is_hidden else 'Hayır'}
⚙️ Sistem Dosyası: {'Evet' if is_system else 'Hayır'}

📅 Oluşturulma: {stats.st_ctime}
📅 Değiştirilme: {stats.st_mtime}
"""
            messagebox.showinfo("Dosya Özellikleri", info)
        except Exception as e:
            messagebox.showerror("Hata", f"Özellikler alınamadı:\n{e}")
            
    def copy_to_usb(self):
        """Seçili dosyayı USB sürücüye kopyala"""
        source_file = self.get_selected_file()
        
        if not source_file:
            messagebox.showwarning("Seçim Yok", "Lütfen kopyalanacak dosyayı seçin (combobox veya output alanından).")
            return
        
        # Hedef sürücü seçimi için dialog
        if not self.drive_data:
            messagebox.showwarning("USB Yok", "Hedef USB sürücü bulunamadı. Lütfen USB takın ve yenileyin.")
            return
        
        # USB seçim dialogu oluştur
        dialog = tk.Toplevel(self)
        dialog.title("Hedef USB Sürücü Seçin")
        dialog.geometry("500x300")
        dialog.transient(self)
        dialog.grab_set()
        
        ttk.Label(dialog, text="📋 Dosyayı kopyalamak için hedef USB sürücüyü seçin:", 
                 font=("Segoe UI", 10, "bold")).pack(pady=10, padx=10)
        
        ttk.Label(dialog, text=f"Kaynak: {os.path.basename(source_file)}", 
                 font=("Segoe UI", 9)).pack(pady=5, padx=10, anchor="w")
        
        # USB listesi
        list_frame = ttk.Frame(dialog)
        list_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        usb_listbox = tk.Listbox(list_frame, font=("Segoe UI", 9), height=8)
        usb_listbox.pack(side="left", fill="both", expand=True)
        
        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=usb_listbox.yview)
        scrollbar.pack(side="right", fill="y")
        usb_listbox.config(yscrollcommand=scrollbar.set)
        
        # USB'leri listele
        for drive in self.drive_data:
            display = f"{drive['mountpoint']} - {drive['label']} ({drive['size']})"
            usb_listbox.insert(tk.END, display)
        
        selected_drive = [None]
        
        def on_copy():
            sel = usb_listbox.curselection()
            if not sel:
                messagebox.showwarning("Seçim Yok", "Lütfen bir USB sürücü seçin.", parent=dialog)
                return
            
            selected_drive[0] = self.drive_data[sel[0]]['mountpoint']
            dialog.destroy()
        
        button_frame = ttk.Frame(dialog)
        button_frame.pack(fill="x", padx=10, pady=10)
        
        ttk.Button(button_frame, text="✅ Kopyala", command=on_copy).pack(side="left", padx=5)
        ttk.Button(button_frame, text="❌ İptal", command=dialog.destroy).pack(side="left", padx=5)
        
        self.wait_window(dialog)
        
        if not selected_drive[0]:
            return
        
        # Hedef yol
        dest_path = os.path.join(selected_drive[0], os.path.basename(source_file))
        
        # Üzerine yazma kontrolü
        if os.path.exists(dest_path):
            confirm = messagebox.askyesno("Dosya Mevcut", 
                                         f"⚠️ Hedef konumda aynı isimde dosya var:\n{dest_path}\n\nÜzerine yazmak istiyor musunuz?")
            if not confirm:
                return
        
        # Kopyalama işlemi
        try:
            shutil.copy2(source_file, dest_path)
            
            # Başarı mesajı
            messagebox.showinfo("Başarılı", 
                              f"✅ Dosya başarıyla kopyalandı!\n\n📁 Kaynak: {source_file}\n📁 Hedef: {dest_path}")
            
            self.output.insert("end", f"\n📋 [KOPYALANDI] {source_file} -> {dest_path}\n", "success")
            self.status_var.set(f"✅ Dosya kopyalandı: {os.path.basename(source_file)}")
        except Exception as e:
            messagebox.showerror("Hata", f"❌ Dosya kopyalanamadı:\n{e}")
            self.status_var.set("❌ Kopyalama başarısız")
    
    def save_report(self):
        """Raporu dosyaya kaydet"""
        content = self.output.get("1.0", "end").strip()
        if not content:
            messagebox.showinfo("Boş", "Kaydedilecek içerik yok.")
            return
            
        path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text dosyaları", "*.txt"), ("Tüm dosyalar", "*.*")],
            initialfile=f"usb_tarama_raporu.txt"
        )
        
        if not path:
            return
            
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            messagebox.showinfo("Başarılı", f"✅ Rapor kaydedildi:\n{path}")
            self.status_var.set(f"✅ Rapor kaydedildi: {os.path.basename(path)}")
        except Exception as e:
            messagebox.showerror("Hata", f"❌ Rapor kaydedilemedi:\n{e}")
            
    def clear_output(self):
        """Çıktıyı temizle"""
        self.output.delete("1.0", "end")
        self.found_files = []
        self.file_combo["values"] = []
        self.status_var.set("🧹 Çıktı temizlendi")
        
    def filter_output(self, event=None):
        """Çıktıyı filtrele (basit arama)"""
        # Bu özellik gelecekte eklenebilir
        pass


if __name__ == "__main__":
    app = USBManagerApp()
    app.mainloop()
