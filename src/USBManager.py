#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
USB Manager - Advanced USB Drive File Management and Security Tool

Copyright (c) 2025 Burak TEMUR and Arda DEMİRHAN. All rights reserved.
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
import sys
import logging
from datetime import datetime
import time
import re

# Encryption support
try:
    from .encryption import encrypt_file, decrypt_file, encrypt_text, decrypt_text
except ImportError:
    # Fallback for direct script execution
    from encryption import encrypt_file, decrypt_file, encrypt_text, decrypt_text

# --- Windows API ---
kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)

GetFileAttributesW = kernel32.GetFileAttributesW
GetFileAttributesW.argtypes = [wintypes.LPCWSTR]
GetFileAttributesW.restype = wintypes.DWORD

SetFileAttributesW = kernel32.SetFileAttributesW
SetFileAttributesW.argtypes = [wintypes.LPCWSTR, wintypes.DWORD]
SetFileAttributesW.restype = wintypes.BOOL

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

FILE_ATTRIBUTE_READONLY = 0x1
FILE_ATTRIBUTE_HIDDEN = 0x2
FILE_ATTRIBUTE_SYSTEM = 0x4
MAX_READ_BYTES = 4096

# Import utility functions
try:
    from .utils import is_hidden_or_system, maybe_text_sample
except ImportError:
    # Fallback for direct script execution
    from utils import is_hidden_or_system, maybe_text_sample

# Varsayılan dosya adı ve token
# Default configuration values - now defined in config file
DEFAULT_FILENAME = "secret_file.dat"
DEFAULT_TOKEN = "ENTER_YOUR_TOKEN_HERE"

# Dil sözlükleri
LANGUAGES = {
    'tr': {
        # Menü
        'menu_file': 'Dosya',
        'menu_help': 'Yardım',
        'menu_language': 'Dil',
        'menu_refresh': 'Yenile (F5)',
        'menu_start_scan': 'Taramayı Başlat (Ctrl+S)',
        'menu_exit': 'Çıkış (Ctrl+Q)',
        'menu_about': 'Hakkında',
        'menu_shortcuts': 'Klavye Kısayolları',
        
        # Başlık
        'title': '🔧 USB Flash Sürücü Yönetim Merkezi',
        
        # Sol panel
        'panel_drive_info': '📏 Sürücü Bilgileri ve İşlemler',
        'label_usb_drive': 'USB Sürücü:',
        'btn_refresh': '🔄 Yenile',
        
        # Sekmeler
        'tab_create_file': '📝 Dosya Oluştur',
        'tab_scan_files': '🔍 Gizli Dosya Tara',
        
        # Dosya oluştur sekmesi
        'label_filename': 'Dosya Adı:',
        'label_content': 'İçerik (Çok satırlı metin):',
        'cb_hide_file': 'Dosyayı gizle',
        'cb_system_file': 'Sistem dosyası yap',
        'cb_readonly': 'Salt okunur',
        'btn_create_file': '✅ Dosyayı Oluştur',
        
        # Tarama sekmesi
        'btn_start_scan': '▶️ Taramayı Başlat',
        'btn_stop': '⏹️ Durdur',
        'btn_clear': '🧹 Temizle',
        'label_ready': 'Hazır',
        'label_scan_info': 'Tarama yapılacak sürücüyü yukarıdan seçin.',
        
        # Sağ panel
        'panel_found_files': '📋 Bulunan Gizli Dosyalar',
        'label_filter': '🔎 Filtre:',
        'label_file_selection': 'Dosya Seçimi:',
        'label_file_operations': 'Seçili Dosya İşlemleri:',
        
        # Dosya işlemleri butonları
        'btn_delete': '🗑️ Dosyayı Sil',
        'btn_properties': '👁️ Özellikleri Göster',
        'btn_copy_usb': '📋 USB\'ye Kopyala',
        'btn_save_report': '💾 Raporu Kaydet',
        'btn_encrypt': '🔒 Şifrele',
        'btn_decrypt': '🔓 Deşifre Et',
        
        # Durum çubuğu
        'status_ready': '✅ Hazır',
        
        # Mesajlar
        'no_usb_found': '❌ Hiçbir USB sürücü bulunamadı',
        'insert_usb': 'USB flash sürücü takın ve yenile butonuna basın.',
        'no_files_found': '❌ Bulunan dosya yok',
    },
    'en': {
        # Menu
        'menu_file': 'File',
        'menu_help': 'Help',
        'menu_language': 'Language',
        'menu_refresh': 'Refresh (F5)',
        'menu_start_scan': 'Start Scan (Ctrl+S)',
        'menu_exit': 'Exit (Ctrl+Q)',
        'menu_about': 'About',
        'menu_shortcuts': 'Keyboard Shortcuts',
        
        # Title
        'title': '🔧 USB Flash Drive Management Center',
        
        # Left panel
        'panel_drive_info': '📏 Drive Information and Operations',
        'label_usb_drive': 'USB Drive:',
        'btn_refresh': '🔄 Refresh',
        
        # Tabs
        'tab_create_file': '📝 Create File',
        'tab_scan_files': '🔍 Scan Hidden Files',
        
        # Create file tab
        'label_filename': 'File Name:',
        'label_content': 'Content (Multi-line text):',
        'cb_hide_file': 'Hide file',
        'cb_system_file': 'Make system file',
        'cb_readonly': 'Read-only',
        'btn_create_file': '✅ Create File',
        
        # Scan tab
        'btn_start_scan': '▶️ Start Scan',
        'btn_stop': '⏹️ Stop',
        'btn_clear': '🧹 Clear',
        'label_ready': 'Ready',
        'label_scan_info': 'Select the drive to scan from above.',
        
        # Right panel
        'panel_found_files': '📋 Found Hidden Files',
        'label_filter': '🔎 Filter:',
        'label_file_selection': 'File Selection:',
        'label_file_operations': 'Selected File Operations:',
        
        # File operation buttons
        'btn_delete': '🗑️ Delete File',
        'btn_properties': '👁️ Show Properties',
        'btn_copy_usb': '📋 Copy to USB',
        'btn_save_report': '💾 Save Report',
        'btn_encrypt': '🔒 Encrypt',
        'btn_decrypt': '🔓 Decrypt',
        
        # Status bar
        'status_ready': '✅ Ready',
        
        # Messages
        'no_usb_found': '❌ No USB drive found',
        'insert_usb': 'Insert USB flash drive and click refresh button.',
        'no_files_found': '❌ No files found',
    }
}

# Logging yapılandırması
log_dir = os.path.join(os.path.dirname(__file__), "logs")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(
            os.path.join(log_dir, f'usbmanager_{datetime.now().strftime("%Y%m%d")}.log'),
            encoding='utf-8'
        ),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


def validate_filename(filename):
    """
    Dosya adını güvenli şekilde doğrula
    
    Args:
        filename (str): Kontrol edilecek dosya adı
        
    Returns:
        bool: Geçerliyse True
        
    Raises:
        ValueError: Geçersiz dosya adı
    """
    # Geçersiz karakterler
    invalid_chars = r'[<>:"/\\|?*]'
    if re.search(invalid_chars, filename):
        raise ValueError("Dosya adı geçersiz karakterler içeriyor: < > : \\ / | ? *")
    
    # Yol ayırıcı kontrolü
    if '/' in filename or '\\' in filename:
        raise ValueError("Dosya adı yol içeremez")
    
    # Uzunluk kontrolü
    if len(filename) > 255:
        raise ValueError("Dosya adı çok uzun (max 255 karakter)")
    
    if len(filename) == 0:
        raise ValueError("Dosya adı boş olamaz")
    
    # Ayrılmış adlar (Windows)
    reserved = ['CON', 'PRN', 'AUX', 'NUL', 'COM1', 'COM2', 'COM3', 'COM4', 'COM5',
                'COM6', 'COM7', 'COM8', 'COM9', 'LPT1', 'LPT2', 'LPT3', 'LPT4',
                'LPT5', 'LPT6', 'LPT7', 'LPT8', 'LPT9']
    name_without_ext = filename.split('.')[0].upper()
    if name_without_ext in reserved:
        raise ValueError(f"'{filename}' ayrılmış bir dosya adı")
    
    logger.info(f"Dosya adı doğrulandı: {filename}")
    return True


def validate_content(content):
    """
    Dosya içeriğini doğrula
    
    Args:
        content (str): Kontrol edilecek içerik
        
    Returns:
        bool: Geçerliyse True
        
    Raises:
        ValueError: Geçersiz içerik
    """
    # Boyut kontrolü (max 10 MB)
    max_size = 10 * 1024 * 1024
    content_size = len(content.encode('utf-8'))
    
    if content_size > max_size:
        raise ValueError(f"İçerik çok büyük (max 10 MB, mevcut: {content_size / (1024*1024):.2f} MB)")
    
    logger.info(f"İçerik doğrulandı: {content_size} bytes")
    return True


def is_admin():
    """
    Yönetici yetkisiyle çalışıp çalışmadığını kontrol et
    
    Returns:
        bool: Yönetici ise True
    """
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


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


# Utility functions imported from utils.py
# def is_hidden_or_system(path: str) -> bool:
# def maybe_text_sample(data: bytes, max_chars=1000):


def scan_drive_for_hidden(root_path: str, callback_print, stop_event):
    """
    Sürücüdeki gizli dosyaları tara - Optimize edilmiş
    
    Args:
        root_path (str): Taranacak sürücü yolu
        callback_print: Çıktı yazdırma fonksiyonu
        stop_event: Durdurma eventi
        
    Returns:
        list: Bulunan dosya listesi
    """
    total_found = 0
    found_files = []
    total_scanned = 0
    start_time = time.time()
    
    callback_print(f"🔍 Tarama başlatıldı: {root_path}\n", "info")
    logger.info(f"Tarama başlatıldı: {root_path}")
    
    try:
        # Use a generator to avoid loading all files into memory at once
        for dirpath, dirnames, filenames in os.walk(root_path, topdown=True,
                                                    onerror=lambda e: callback_print(f"❌ Hata: {e}\n", "error")):
            if stop_event.is_set():
                logger.warning("Tarama kullanıcı tarafından durduruldu")
                raise KeyboardInterrupt()
            
            # Process files in smaller batches to reduce memory usage
            batch_size = 50  # Reduced from 100 for better memory management
            for i in range(0, len(filenames), batch_size):
                batch = filenames[i:i+batch_size]
                total_scanned += len(batch)
                
                for fname in batch:
                    if stop_event.is_set():
                        raise KeyboardInterrupt()
                        
                    full = os.path.join(dirpath, fname)
                    try:
                        if is_hidden_or_system(full):
                            total_found += 1
                            found_files.append(full)
                            callback_print(f"📁 [{total_found}] {full}\n", "found")
                            logger.info(f"Gizli dosya bulundu: {full}")
                            
                            try:
                                with open(full, "rb") as f:
                                    sample = f.read(MAX_READ_BYTES)
                            except Exception as e:
                                callback_print(f"   ⚠️ Okunamadı: {e}\n\n", "warning")
                                logger.warning(f"Dosya okunamadı {full}: {e}")
                                continue

                            text_sample = maybe_text_sample(sample)
                            if text_sample is None:
                                callback_print("   📦 Binary dosya\n\n", "info")
                            else:
                                callback_print("   📄 İçerik örneği:\n", "info")
                                for line in text_sample.splitlines()[:5]:  # Reduced from 10 lines
                                    callback_print(f"   {line}\n", "content")
                                callback_print("\n", "info")
                    except Exception as e:
                        logger.error(f"Dosya işlenirken hata {full}: {e}")
                        continue
                
                # More frequent progress updates for better UX
                if total_scanned % 100 == 0:  # Changed from 500 to 100
                    elapsed = time.time() - start_time
                    rate = total_scanned / elapsed if elapsed > 0 else 0
                    callback_print(f"ℹ️ İlerleme: {total_scanned} dosya tarandı ({rate:.0f} dosya/sn) - {total_found} gizli dosya\n", "info")
                    logger.info(f"İlerleme: {total_scanned} dosya, {total_found} gizli")
                    
                    # Yield control to the GUI thread more frequently
                    time.sleep(0.01)
    
    except KeyboardInterrupt:
        elapsed = time.time() - start_time
        callback_print(f"\n⏹️ Tarama durduruldu. Süre: {elapsed:.1f}sn\n", "warning")
        logger.warning(f"Tarama durduruldu. {total_scanned} dosya tarandı, {total_found} gizli dosya")
        raise
    
    elapsed = time.time() - start_time
    callback_print(f"✅ Tarama tamamlandı. Toplam {total_found} gizli dosya bulundu.\n", "success")
    callback_print(f"📊 İstatistikler: {total_scanned} dosya tarandı, Süre: {elapsed:.1f}sn\n", "info")
    logger.info(f"Tarama tamamlandı. {total_scanned} dosya, {total_found} gizli, {elapsed:.1f}sn")
    
    return found_files


class USBManagerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Varsayılan dil (Türkçe)
        self.current_language = 'tr'
        
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
        
        # Klavye kısayolları
        self.setup_keyboard_shortcuts()
        
        self.create_widgets()
        self.populate_drives()
        
        # Yönetici yetkisi kontrolü
        if not is_admin():
            self.after(100, self.show_admin_warning)
    
    def setup_keyboard_shortcuts(self):
        """Klavye kısayollarını ayarla"""
        self.bind('<Control-r>', lambda e: self.populate_drives())  # Ctrl+R: Yenile
        self.bind('<F5>', lambda e: self.populate_drives())         # F5: Yenile
        self.bind('<Control-s>', lambda e: self.start_scan())       # Ctrl+S: Tara
        self.bind('<Control-n>', lambda e: self.create_file())      # Ctrl+N: Oluştur
        self.bind('<Escape>', lambda e: self.stop_scan())           # Esc: Durdur
        self.bind('<Delete>', lambda e: self.delete_selected())     # Del: Sil
        self.bind('<Control-q>', lambda e: self.quit())             # Ctrl+Q: Çık
        logger.info("Klavye kısayolları ayarlandı")
    
    def t(self, key: str) -> str:
        """Dil çevirisi için yardımcı fonksiyon"""
        return LANGUAGES.get(self.current_language, LANGUAGES['tr']).get(key, key)
    
    def change_language(self, lang):
        """Dili değiştir ve arayüzü güncelle"""
        self.current_language = lang
        logger.info(f"Dil değiştirildi: {lang}")
        
        # Arayüzü yeniden oluştur
        for widget in self.winfo_children():
            widget.destroy()
        
        self.create_widgets()
        self.populate_drives()
        
        # Durum mesajı
        if lang == 'tr':
            messagebox.showinfo("İşlem Başarılı", "✅ Dil Türkçe olarak ayarlandı.")
        else:
            messagebox.showinfo("Operation Successful", "✅ Language set to English.")
    
    def show_admin_warning(self):
        """Yönetici yetkisi uyarısı göster"""
        response = messagebox.showwarning(
            "Yönetici Yetkisi Önerilir",
            "⚠️ Bazı özellikler için yönetici yetkisi gerekiyor:\n\n"
            "• Sistem dosyası özniteliği ayarlama\n"
            "• Gizli/sistem dosyalarını silme\n"
            "• Dosya özniteliklerini değiştirme\n\n"
            "Tam işlevsellik için uygulamayı yönetici olarak çalıştırmanız önerilir."
        )
        logger.warning("Yönetici yetkisi olmadan çalışıyor")
        
    def create_widgets(self):
        # Menü çubuğu
        menubar = tk.Menu(self)
        self.config(menu=menubar)
        
        # Dosya menüsü
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label=self.t('menu_file'), menu=file_menu)
        file_menu.add_command(label=self.t('menu_refresh'), command=self.populate_drives, accelerator="F5")
        file_menu.add_command(label=self.t('menu_start_scan'), command=self.start_scan, accelerator="Ctrl+S")
        file_menu.add_separator()
        file_menu.add_command(label=self.t('menu_exit'), command=self.quit, accelerator="Ctrl+Q")
        
        # Dil menüsü
        lang_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label=self.t('menu_language'), menu=lang_menu)
        lang_menu.add_command(label="🇹🇷 Türkçe", command=lambda: self.change_language('tr'))
        lang_menu.add_command(label="🇬🇧 English", command=lambda: self.change_language('en'))
        
        # Yardım menüsü
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label=self.t('menu_help'), menu=help_menu)
        help_menu.add_command(label=self.t('menu_about'), command=self.show_about)
        help_menu.add_command(label=self.t('menu_shortcuts'), command=self.show_shortcuts)
        
        # Başlık
        header = tk.Frame(self, bg=self.colors['primary'], height=60)
        header.pack(fill="x")
        header.pack_propagate(False)
        
        title_label = tk.Label(header, text=self.t('title'), 
                              font=("Segoe UI", 16, "bold"), 
                              bg=self.colors['primary'], 
                              fg=self.colors['light'])
        title_label.pack(pady=15)
        
        # Ana container
        main_container = ttk.Frame(self)
        main_container.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Sol panel - Sürücü Seçimi ve İşlemler
        left_panel = ttk.LabelFrame(main_container, text=self.t('panel_drive_info'), padding=10)
        left_panel.pack(side="left", fill="both", expand=True, padx=(0, 5))
        
        # Sürücü seçimi
        drive_frame = ttk.Frame(left_panel)
        drive_frame.pack(fill="x", pady=(0, 10))
        
        ttk.Label(drive_frame, text=self.t('label_usb_drive'), font=("Segoe UI", 10, "bold")).pack(anchor="w")
        
        drive_select_frame = ttk.Frame(drive_frame)
        drive_select_frame.pack(fill="x", pady=5)
        
        self.drive_combo = ttk.Combobox(drive_select_frame, state="readonly", width=40, font=("Segoe UI", 9))
        self.drive_combo.pack(side="left", fill="x", expand=True)
        self.drive_combo.bind("<<ComboboxSelected>>", self.on_drive_selected)
        
        ttk.Button(drive_select_frame, text=self.t('btn_refresh'), command=self.populate_drives, width=12).pack(side="left", padx=(5, 0))
        
        # Sürücü detayları
        self.drive_info_label = ttk.Label(drive_frame, text="", font=("Segoe UI", 9), foreground="#666")
        self.drive_info_label.pack(anchor="w", pady=5)
        
        # Notebook (Sekmeler)
        self.notebook = ttk.Notebook(left_panel)
        self.notebook.pack(fill="both", expand=True)
        
        # Sekme 1: Dosya Oluştur
        create_tab = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(create_tab, text=self.t('tab_create_file'))
        
        ttk.Label(create_tab, text=self.t('label_filename'), font=("Segoe UI", 9)).pack(anchor="w", pady=(5, 2))
        self.filename_entry = ttk.Entry(create_tab, width=40, font=("Segoe UI", 9))
        self.filename_entry.pack(fill="x", pady=(0, 10))
        self.filename_entry.insert(0, DEFAULT_FILENAME)
        
        ttk.Label(create_tab, text=self.t('label_content'), font=("Segoe UI", 9)).pack(anchor="w", pady=(5, 2))
        self.content_text = scrolledtext.ScrolledText(create_tab, height=10, font=("Consolas", 9), wrap="word")
        self.content_text.pack(fill="both", expand=True, pady=(0, 10))
        self.content_text.insert("1.0", DEFAULT_TOKEN)
        
        options_frame = ttk.Frame(create_tab)
        options_frame.pack(fill="x", pady=5)
        
        self.hide_file_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(options_frame, text=self.t('cb_hide_file'), variable=self.hide_file_var).pack(side="left", padx=5)
        
        self.system_file_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(options_frame, text=self.t('cb_system_file'), variable=self.system_file_var).pack(side="left", padx=5)
        
        self.readonly_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(options_frame, text=self.t('cb_readonly'), variable=self.readonly_var).pack(side="left", padx=5)
        
        create_btn_frame = ttk.Frame(create_tab)
        create_btn_frame.pack(fill="x", pady=10)
        
        ttk.Button(create_btn_frame, text=self.t('btn_create_file'), command=self.create_file, style="Success.TButton").pack(fill="x")
        
        # Sekme 2: Gizli Dosya Tarama
        scan_tab = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(scan_tab, text=self.t('tab_scan_files'))
        
        scan_controls = ttk.Frame(scan_tab)
        scan_controls.pack(fill="x", pady=(0, 10))
        
        ttk.Button(scan_controls, text=self.t('btn_start_scan'), command=self.start_scan, width=20).pack(side="left", padx=2)
        ttk.Button(scan_controls, text=self.t('btn_stop'), command=self.stop_scan, width=15).pack(side="left", padx=2)
        ttk.Button(scan_controls, text=self.t('btn_clear'), command=self.clear_output, width=15).pack(side="left", padx=2)
        
        # İlerleme çubuğu
        progress_frame = ttk.Frame(scan_tab)
        progress_frame.pack(fill="x", pady=(5, 5))
        
        self.progress_var = tk.DoubleVar()
        self.progress = ttk.Progressbar(
            progress_frame,
            variable=self.progress_var,
            maximum=100,
            mode='determinate'
        )
        self.progress.pack(fill="x", pady=2)
        
        self.progress_label = ttk.Label(progress_frame, text=self.t('label_ready'), font=("Segoe UI", 8), foreground="#666")
        self.progress_label.pack(anchor="w")
        
        ttk.Label(scan_tab, text=self.t('label_scan_info'), 
                 font=("Segoe UI", 9), foreground="#666").pack(anchor="w", pady=5)
        
        # Sağ panel - Bulunan Dosyalar
        right_panel = ttk.LabelFrame(main_container, text=self.t('panel_found_files'), padding=10)
        right_panel.pack(side="left", fill="both", expand=True, padx=(5, 0))
        
        # Arama çubuğu
        search_frame = ttk.Frame(right_panel)
        search_frame.pack(fill="x", pady=(0, 5))
        
        ttk.Label(search_frame, text=self.t('label_filter'), font=("Segoe UI", 9)).pack(side="left", padx=2)
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
        
        ttk.Label(file_select_frame, text=self.t('label_file_selection'), font=("Segoe UI", 9, "bold")).pack(anchor="w", pady=2)
        
        self.file_combo = ttk.Combobox(file_select_frame, state="readonly", font=("Segoe UI", 8))
        self.file_combo.pack(fill="x", pady=2)
        self.file_combo.bind("<<ComboboxSelected>>", self.on_file_selected)
        
        # Dosya işlemleri
        file_ops_frame = ttk.Frame(right_panel)
        file_ops_frame.pack(fill="x", pady=(5, 0))
        
        ttk.Label(file_ops_frame, text=self.t('label_file_operations'), font=("Segoe UI", 9, "bold")).pack(anchor="w", pady=2)
        
        # Grid layout kullan - 3 satır, 2 sütun
        ops_grid = ttk.Frame(file_ops_frame)
        ops_grid.pack(fill="x", pady=2)
        
        # Sabit genişlik - tüm butonlar için
        button_width = 28
        
        # 1. satır
        ttk.Button(ops_grid, text=self.t('btn_delete'), command=self.delete_selected, width=button_width).grid(row=0, column=0, padx=2, pady=2, sticky="ew")
        ttk.Button(ops_grid, text=self.t('btn_properties'), command=self.show_file_properties, width=button_width).grid(row=0, column=1, padx=2, pady=2, sticky="ew")
        
        # 2. satır
        ttk.Button(ops_grid, text=self.t('btn_copy_usb'), command=self.copy_to_usb, width=button_width).grid(row=1, column=0, padx=2, pady=2, sticky="ew")
        ttk.Button(ops_grid, text=self.t('btn_save_report'), command=self.save_report, width=button_width).grid(row=1, column=1, padx=2, pady=2, sticky="ew")
        
        # 3. satır - Şifreleme işlemleri
        ttk.Button(ops_grid, text=self.t('btn_encrypt'), command=self.encrypt_selected, width=button_width).grid(row=2, column=0, padx=2, pady=2, sticky="ew")
        ttk.Button(ops_grid, text=self.t('btn_decrypt'), command=self.decrypt_selected, width=button_width).grid(row=2, column=1, padx=2, pady=2, sticky="ew")
        
        # Sütunları eşit genişlikte yap
        ops_grid.columnconfigure(0, weight=1)
        ops_grid.columnconfigure(1, weight=1)
        
        # Durum çubuğu
        status_frame = tk.Frame(self, bg=self.colors['dark'], height=30)
        status_frame.pack(fill="x", side="bottom")
        status_frame.pack_propagate(False)
        
        self.status_var = tk.StringVar(value=self.t('status_ready'))
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
            display = [self.t('no_usb_found')]
            self.drive_data = []
            
        self.drive_combo["values"] = display
        if display and not display[0].startswith("❌"):
            self.drive_combo.current(0)
            self.on_drive_selected(None)
        else:
            self.drive_info_label.config(text=self.t('insert_usb'))
            
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
        """Flash sürücüde dosya oluştur - Validation eklendi"""
        disk = self.drive_combo.get()
        if not disk or disk.startswith("❌"):
            messagebox.showerror("Hata", "Lütfen geçerli bir USB sürücü seçin.")
            logger.warning("USB sürücü seçilmedi")
            return
            
        disk = disk.split()[0]
        if not disk.endswith("\\"):
            disk += "\\"

        filename = self.filename_entry.get().strip()
        if not filename:
            messagebox.showerror("Hata", "Lütfen bir dosya adı girin.")
            return
        
        # Dosya adı validasyonu
        try:
            validate_filename(filename)
        except ValueError as e:
            messagebox.showerror("Geçersiz Dosya Adı", str(e))
            logger.error(f"Geçersiz dosya adı: {filename} - {e}")
            return
            
        content = self.content_text.get("1.0", "end-1c")
        
        # İçerik validasyonu
        try:
            validate_content(content)
        except ValueError as e:
            messagebox.showerror("Geçersiz İçerik", str(e))
            logger.error(f"İçerik validasyon hatası: {e}")
            return
        
        filepath = os.path.join(disk, filename)

        try:
            # Dosya oluştur
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            
            logger.info(f"Dosya oluşturuldu: {filepath}")
            
            # Dosya özniteliklerini ayarla - Windows API kullan
            attrs = 0
            if self.hide_file_var.get():
                attrs |= FILE_ATTRIBUTE_HIDDEN
            if self.system_file_var.get():
                attrs |= FILE_ATTRIBUTE_SYSTEM
            if self.readonly_var.get():
                attrs |= FILE_ATTRIBUTE_READONLY
            
            if attrs > 0:
                result = SetFileAttributesW(filepath, attrs)
                if not result:
                    # Fallback: subprocess kullan
                    logger.warning("SetFileAttributesW başarısız, subprocess kullanılıyor")
                    attrib_cmd = ["attrib"]
                    if self.hide_file_var.get():
                        attrib_cmd.append("+h")
                    if self.system_file_var.get():
                        attrib_cmd.append("+s")
                    if self.readonly_var.get():
                        attrib_cmd.append("+r")
                    attrib_cmd.append(filepath)
                    subprocess.run(attrib_cmd, check=True)
                else:
                    logger.info(f"Dosya öznitelikleri ayarlandı: {attrs}")
            
            messagebox.showinfo("Başarılı", f"✅ Dosya başarıyla oluşturuldu!\n\n📁 Konum: {filepath}\n📝 Boyut: {len(content)} karakter")
            self.status_var.set(f"✅ Dosya oluşturuldu: {filename}")
            logger.info(f"Dosya başarıyla oluşturuldu: {filepath}")
        except Exception as e:
            messagebox.showerror("Hata", f"❌ Dosya oluşturulamadı:\n{e}")
            self.status_var.set("❌ Dosya oluşturma başarısız")
            logger.error(f"Dosya oluşturma hatası: {filepath} - {e}")
            
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
        
        # İlerleme çubuğunu başlat
        self.progress_var.set(0)
        self.progress.config(mode='indeterminate')
        self.progress.start(10)
        self.progress_label.config(text="Tarama başlatılıyor...")
        
        self.status_var.set(f"🔍 {root_path} taranıyor...")
        logger.info(f"Tarama başlatıldı: {root_path}")
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
            
            # İlerleme çubuğunu tamamla
            self.progress.stop()
            self.progress.config(mode='determinate')
            self.progress_var.set(100)
            self.progress_label.config(text=f"Tamamlandı - {len(self.found_files)} gizli dosya bulundu")
            
            self.status_var.set(f"✅ Tarama tamamlandı. {len(self.found_files)} dosya bulundu.")
            logger.info(f"Tarama başarıyla tamamlandı: {len(self.found_files)} dosya")
        except KeyboardInterrupt:
            self.output.insert("end", "\n⏹️ Tarama kullanıcı tarafından durduruldu.\n", "warning")
            
            # İlerleme çubuğunu durdur
            self.progress.stop()
            self.progress.config(mode='determinate')
            self.progress_var.set(0)
            self.progress_label.config(text="Durduruldu")
            
            self.status_var.set("⏹️ Tarama durduruldu.")
            logger.warning("Tarama durduruldu")
        except Exception as e:
            self.output.insert("end", f"\n❌ Tarama sırasında hata: {e}\n", "error")
            
            # İlerleme çubuğunu sıfırla
            self.progress.stop()
            self.progress.config(mode='determinate')
            self.progress_var.set(0)
            self.progress_label.config(text="Hata oluştu")
            
            self.status_var.set("❌ Hata oluştu.")
            logger.error(f"Tarama hatası: {e}")
    
    def update_file_combo(self):
        """Bulunan dosyaları combobox'a ekle"""
        if not self.found_files:
            self.file_combo["values"] = [self.t('no_files_found')]
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
            
    def encrypt_selected(self):
        """Seçili dosyayı şifrele"""
        filepath = self.get_selected_file()
        
        if not filepath:
            messagebox.showwarning("Seçim Yok", "Lütfen şifrelenecek dosyayı seçin (combobox veya output alanından).")
            return
            
        # Şifreleme için şifre iste
        password = self.ask_password("Şifreleme için bir şifre girin:")
        if not password:
            return
            
        try:
            encrypted_path = encrypt_file(filepath, password)
            messagebox.showinfo("Başarılı", f"✅ Dosya şifrelendi:\n{encrypted_path}")
            self.output.insert("end", f"\n🔒 [ŞİFRELENDİ] {filepath} -> {encrypted_path}\n", "success")
            self.status_var.set(f"✅ Dosya şifrelendi: {os.path.basename(filepath)}")
        except Exception as e:
            messagebox.showerror("Hata", f"❌ Dosya şifrelenemedi:\n{e}")
            self.status_var.set("❌ Şifreleme başarısız")
            
    def decrypt_selected(self):
        """Seçili dosyanın şifresini çöz"""
        filepath = self.get_selected_file()
        
        if not filepath:
            messagebox.showwarning("Seçim Yok", "Lütfen şifresi çözülecek dosyayı seçin (combobox veya output alanından).")
            return
            
        # Şifre çözme için şifre iste
        password = self.ask_password("Şifre çözme için şifreyi girin:")
        if not password:
            return
            
        try:
            decrypted_path = decrypt_file(filepath, password)
            messagebox.showinfo("Başarılı", f"✅ Dosya şifresi çözüldü:\n{decrypted_path}")
            self.output.insert("end", f"\n🔓 [ŞİFRESİ ÇÖZÜLDÜ] {filepath} -> {decrypted_path}\n", "success")
            self.status_var.set(f"✅ Dosya şifresi çözüldü: {os.path.basename(filepath)}")
        except Exception as e:
            messagebox.showerror("Hata", f"❌ Dosya şifresi çözülemedi:\n{e}")
            self.status_var.set("❌ Şifre çözme başarısız")
            
    def ask_password(self, prompt):
        """Kullanıcıdan şifre iste"""
        # Basit bir şifre dialogu oluştur
        dialog = tk.Toplevel(self)
        dialog.title("Şifre Girişi")
        dialog.geometry("300x150")
        dialog.transient(self)
        dialog.grab_set()
        
        ttk.Label(dialog, text=prompt, font=("Segoe UI", 10)).pack(pady=10)
        
        password_entry = ttk.Entry(dialog, show="*", width=30)
        password_entry.pack(pady=5)
        password_entry.focus()
        
        password_var = tk.StringVar()
        
        def on_ok():
            password_var.set(password_entry.get())
            dialog.destroy()
            
        def on_cancel():
            password_var.set("")
            dialog.destroy()
            
        button_frame = ttk.Frame(dialog)
        button_frame.pack(pady=10)
        
        ttk.Button(button_frame, text="Tamam", command=on_ok).pack(side="left", padx=5)
        ttk.Button(button_frame, text="İptal", command=on_cancel).pack(side="left", padx=5)
        
        # Enter tuşunu bağla
        password_entry.bind("<Return>", lambda e: on_ok())
        
        self.wait_window(dialog)
        return password_var.get()
            
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
    
    def show_about(self):
        """Hakkında penceresi göster"""
        about_text = f"""
USB Flash Sürücü Yöneticisi
Versiyon: 1.0.0

Gelişmiş USB sürücü dosya yönetimi ve güvenlik aracı

Yazarlar: Burak TEMUR ve Arda DEMİRHAN
Copyright © 2025 - Tüm hakları saklıdır

Özellikler:
• Gizli dosya oluşturma
• Sistem dosyası tarama
• Güvenli dosya silme
• USB'ler arası kopyalama
• Rapor kaydetme

Lisans: Proprietary
Platform: Windows
        """
        messagebox.showinfo("🔧 Hakkında", about_text)
        logger.info("Hakkında penceresi görüntülendi")
    
    def show_shortcuts(self):
        """Klavye kısayollarını göster"""
        shortcuts_text = """
⌨️ Klavye Kısayolları

F5 veya Ctrl+R   - Sürücüleri yenile
Ctrl+S           - Taramayı başlat
Ctrl+N           - Dosya oluştur
Esc              - Taramayı durdur
Delete           - Seçili dosyayı sil
Ctrl+Q           - Uygulamadan çık

💡 İpuçları:
• Dosya seçmek için combobox veya output alanını kullanın
• Tam işlevsellik için yönetici yetkisi gerekir
• İlerleme bilgisi output alanında görüntülenir
        """
        messagebox.showinfo("⌨️ Klavye Kısayolları", shortcuts_text)
        logger.info("Klavye kısayolları penceresi görüntülendi")


if __name__ == "__main__":
    logger.info("="*50)
    logger.info("USB Manager başlatılıyor...")
    logger.info(f"Python versiyonu: {sys.version}")
    logger.info(f"Platform: {sys.platform}")
    
    # Yönetici yetki kontrolü
    admin_status = is_admin()
    logger.info(f"Yönetici yetkisi: {admin_status}")
    
    try:
        app = USBManagerApp()
        logger.info("Uygulama başlatıldı")
        app.mainloop()
    except Exception as e:
        logger.error(f"Uygulama hatası: {e}")
        messagebox.showerror("Kritik Hata", f"Uygulama başlatılamadı:\n{e}")
    finally:
        logger.info("Uygulama kapatıldı")
        logger.info("="*50)
