#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
USB Manager - Utility Functions

Copyright (c) 2025 Burak TEMUR and Arda DEMİRHAN. All rights reserved.
This software is proprietary. Unauthorized use is prohibited.
"""

import os
import ctypes
from ctypes import wintypes

# --- Windows API ---
kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)

GetFileAttributesW = kernel32.GetFileAttributesW
GetFileAttributesW.argtypes = [wintypes.LPCWSTR]
GetFileAttributesW.restype = wintypes.DWORD

FILE_ATTRIBUTE_HIDDEN = 0x2
FILE_ATTRIBUTE_SYSTEM = 0x4
MAX_READ_BYTES = 4096

def is_hidden_or_system(path: str) -> bool:
    """Dosyanın gizli veya sistem dosyası olup olmadığını kontrol et"""
    try:
        attrs = GetFileAttributesW(path)
        if attrs == 0xFFFFFFFF:
            return False
        return bool(attrs & (FILE_ATTRIBUTE_HIDDEN | FILE_ATTRIBUTE_SYSTEM))
    except Exception:
        return False

def is_hidden(path: str) -> bool:
    """Dosyanın gizli olup olmadığını kontrol et"""
    try:
        attrs = GetFileAttributesW(path)
        if attrs == 0xFFFFFFFF:
            return False
        return bool(attrs & FILE_ATTRIBUTE_HIDDEN)
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