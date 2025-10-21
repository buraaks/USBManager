#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Flash Reader - USB Hidden File Scanner

Copyright (c) 2025 Burak TEMUR and Arda DEMİRHAN. All rights reserved.
This software is proprietary. Unauthorized use is prohibited.
"""

import os
import psutil
import ctypes
from ctypes import wintypes
import threading
import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog, messagebox
import subprocess

# --- Windows API ---
kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
GetFileAttributesW = kernel32.GetFileAttributesW
GetFileAttributesW.argtypes = [wintypes.LPCWSTR]
GetFileAttributesW.restype = wintypes.DWORD

FILE_ATTRIBUTE_HIDDEN = 0x2
FILE_ATTRIBUTE_SYSTEM = 0x4
MAX_READ_BYTES = 4096

def is_hidden_or_system(path: str) -> bool:
    try:
        attrs = GetFileAttributesW(path)
        if attrs == 0xFFFFFFFF:
            return False
        return bool(attrs & (FILE_ATTRIBUTE_HIDDEN | FILE_ATTRIBUTE_SYSTEM))
    except Exception:
        return False

def maybe_text_sample(data: bytes, max_chars=1000):
    if not data:
        return ""
    if b'\x00' in data:
        return None
    try:
        text = data.decode('utf-8', errors='replace')
    except Exception:
        return None
    return text[:max_chars]

def scan_drive_for_hidden(root_path: str, callback_print):
    total_found = 0
    callback_print(f"Tarama başlatıldı: {root_path}\n")
    for dirpath, dirnames, filenames in os.walk(root_path, topdown=True,
                                                onerror=lambda e: callback_print(f"Hata (walk): {e}\n")):
        for fname in filenames:
            full = os.path.join(dirpath, fname)
            try:
                if is_hidden_or_system(full):
                    total_found += 1
                    callback_print(f"[FOUND] {full}\n")
                    try:
                        with open(full, "rb") as f:
                            sample = f.read(MAX_READ_BYTES)
                    except Exception as e:
                        callback_print(f" - OKUNAMADI: {e}\n\n")
                        continue

                    text_sample = maybe_text_sample(sample)
                    if text_sample is None:
                        callback_print(" - Dosya binary veya okunabilir metin değil.\n\n")
                    else:
                        callback_print(" - İçerik örneği:\n")
                        for line in text_sample.splitlines():
                            callback_print(f" {line}\n")
                        callback_print("\n")
            except Exception as e:
                callback_print(f" - İstisna: {e}\n")
                continue
    callback_print(f"Tarama tamamlandı. Toplam gizli dosya: {total_found}\n")
    return total_found

class HiddenScannerGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hidden/System Dosya Tarayıcı")
        self.geometry("950x650")

        top = ttk.Frame(self)
        top.pack(fill="x", padx=8, pady=6)

        ttk.Label(top, text="Tarancak Sürücü:").pack(side="left", padx=(0,6))
        self.drive_combo = ttk.Combobox(top, state="readonly", width=30)
        self.drive_combo.pack(side="left")

        ttk.Button(top, text="Yenile", command=self.populate_drives).pack(side="left", padx=6)
        ttk.Button(top, text="Tarama Başlat", command=self.start_scan).pack(side="left", padx=6)
        ttk.Button(top, text="Durdur", command=self.stop_scan).pack(side="left", padx=6)

        ttk.Button(top, text="Raporu Kaydet", command=self.save_report).pack(side="right", padx=6)
        ttk.Button(top, text="Temizle", command=self.clear_output).pack(side="right", padx=6)
        ttk.Button(top, text="Seçili Dosyayı Sil", command=self.delete_selected).pack(side="right", padx=6)

        self.output = scrolledtext.ScrolledText(self, wrap="none", font=("Consolas", 10))
        self.output.pack(fill="both", expand=True, padx=8, pady=(0,8))

        self.status_var = tk.StringVar(value="Hazır")
        status = ttk.Label(self, textvariable=self.status_var, anchor="w")
        status.pack(fill="x", padx=8, pady=(0,8))

        self._scan_thread = None
        self._stop_event = threading.Event()

        self.populate_drives()

    def populate_drives(self):
        drives = [p.mountpoint for p in psutil.disk_partitions(all=False)]
        display = []
        for d in drives:
            try:
                part = next((p for p in psutil.disk_partitions(all=False) if p.mountpoint == d), None)
                t = part.fstype if part else ""
                display.append(f"{d} [{t}]")
            except Exception:
                display.append(d)
        self.drive_combo["values"] = display
        if display:
            self.drive_combo.current(0)

    def start_scan(self):
        if self._scan_thread and self._scan_thread.is_alive():
            messagebox.showinfo("Zaten çalışıyor", "Tarama zaten çalışıyor.")
            return
        sel = self.drive_combo.get()
        if not sel:
            messagebox.showwarning("Sürücü seçin", "Lütfen bir sürücü seçin.")
            return
        root_path = sel.split()[0]
        if not root_path.endswith("\\"):
            root_path += "\\"

        self._stop_event.clear()
        self.output.insert("end", f"\n--- {root_path} taraması başlıyor ---\n")
        self.status_var.set(f"{root_path} taranıyor...")
        self._scan_thread = threading.Thread(target=self._scan_worker, args=(root_path,), daemon=True)
        self._scan_thread.start()

    def stop_scan(self):
        if self._scan_thread and self._scan_thread.is_alive():
            self._stop_event.set()
            self.status_var.set("Durduruluyor...")
        else:
            self.status_var.set("Çalışan tarama yok.")

    def _scan_worker(self, root_path):
        def cb_print(msg):
            if self._stop_event.is_set():
                raise KeyboardInterrupt()
            self.output.insert("end", msg)
            self.output.see("end")
        try:
            scan_drive_for_hidden(root_path, callback_print=cb_print)
            self.status_var.set("Tarama tamamlandı.")
        except KeyboardInterrupt:
            self.output.insert("end", "\nTarama kullanıcı tarafından durduruldu.\n")
            self.status_var.set("Durduruldu.")
        except Exception as e:
            self.output.insert("end", f"\nTarama sırasında hata: {e}\n")
            self.status_var.set("Hata oluştu.")

    def delete_selected(self):
        try:
            sel_text = self.output.get("sel.first", "sel.last").strip()
        except tk.TclError:
            messagebox.showwarning("Seçim yok", "Lütfen silmek istediğiniz dosya yolunu seçin.")
            return
        if not sel_text or not os.path.exists(sel_text):
            messagebox.showerror("Geçersiz", "Seçili satır geçerli bir dosya değil.")
            return
        confirm = messagebox.askyesno("Onay", f"Bu dosyayı silmek istiyor musunuz?\n{sel_text}")
        if not confirm:
            return
        try:
            subprocess.run(["attrib", "-h", "-s", "-r", sel_text], check=False)
            os.remove(sel_text)
            messagebox.showinfo("Başarılı", f"Silindi: {sel_text}")
            self.output.insert("end", f"[DELETED] {sel_text}\n")
        except Exception as e:
            messagebox.showerror("Hata", f"Silinemedi: {e}")

    def save_report(self):
        if not self.output.get("1.0", "end").strip():
            messagebox.showinfo("Boş", "Kaydedecek içerik yok.")
            return
        path = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("Text files","*.txt"),("All files","*.*")])
        if not path:
            return
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(self.output.get("1.0", "end"))
            messagebox.showinfo("Başarılı", f"Rapor kaydedildi: {path}")
        except Exception as e:
            messagebox.showerror("Hata", f"Kaydederken hata: {e}")

    def clear_output(self):
        self.output.delete("1.0", "end")

if __name__ == "__main__":
    root = HiddenScannerGUI()
    root.mainloop()