#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
USB Manager - Advanced USB Drive File Management and Security Tool

Copyright (c) 2025 Burak. All rights reserved.
This software is proprietary. Unauthorized use is prohibited.

This package provides tools for managing USB drives, creating hidden files,
and scanning for system files on removable media.
"""

__version__ = '1.0.0'
__author__ = 'Burak'
__copyright__ = 'Copyright (c) 2025 Burak. All rights reserved.'
__license__ = 'Proprietary'

# Import main components for easy access
try:
    from .USBManager import USBManagerApp
except ImportError:
    # Allow running as script
    pass

__all__ = ['USBManagerApp']
