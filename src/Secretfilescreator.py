#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Secret Files Creator - USB Hidden File Creation Tool

Copyright (c) 2025 Burak TEMUR and Arda DEMİRHAN. All rights reserved.
This software is proprietary. Unauthorized use is prohibited.
"""

import os
import psutil
import tkinter as tk
from tkinter import ttk, messagebox
import subprocess

# Varsayılan dosya adı ve token
DEFAULT_FILENAME = "a3f9c7b2.dat"
DEFAULT_TOKEN = "USB-AUTH-2442C3D3"

def get_removable_drives():
    """Takılı çıkarılabilir diskleri listele"""
    drives = []
    for p in psutil.disk_partitions(all=False):
        if "removable" in p.opts.lower() or p.fstype.lower() in ["fat32", "exfat", "ntfs"]:
            drives.append(p.device)
    return drives

class USBFileCreatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("USB Gizli Dosya Oluşturucu")
        self.geometry("500x300")

        ttk.Label(self, text="Hedef Disk Seçin:").pack(pady=(12,6))
        self.disk_combo = ttk.Combobox(self, values=get_removable_drives(), state="readonly", width=15)
        self.disk_combo.pack()
        if self.disk_combo['values']:
            self.disk_combo.current(0)

        ttk.Label(self, text="Dosya Adı:").pack(pady=(12,6))
        self.filename_entry = ttk.Entry(self, width=30)
        self.filename_entry.pack()
        self.filename_entry.insert(0, DEFAULT_FILENAME)

        ttk.Label(self, text="Token:").pack(pady=(12,6))
        self.token_entry = ttk.Entry(self, width=40)
        self.token_entry.pack()
        self.token_entry.insert(0, DEFAULT_TOKEN)

        ttk.Button(self, text="Dosyayı Oluştur", command=self.create_file).pack(pady=(20,12))
        ttk.Button(self, text="Kapat", command=self.quit).pack()

    def create_file(self):
        disk = self.disk_combo.get()
        if not disk:
            messagebox.showerror("Hata", "Lütfen bir disk seçin.")
            return
        if not disk.endswith("\\"):
            disk += "\\"

        filename = self.filename_entry.get().strip()
        token = self.token_entry.get().strip()
        filepath = os.path.join(disk, filename)

        try:
            # Dosya oluştur
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(token)
            
            # Windows'ta gizli, sistem ve salt okunur yap
            if os.name == 'nt':
                subprocess.run(["attrib", "+h", "+s", "+r", filepath], check=True)
            
            messagebox.showinfo("Başarılı", f"Gizli dosya oluşturuldu:\n{filepath}")
        except Exception as e:
            messagebox.showerror("Hata", f"Dosya oluşturulamadı:\n{e}")

if __name__ == "__main__":
    app = USBFileCreatorApp()
    app.mainloop()