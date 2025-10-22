#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
USB Manager - Button Visibility Test

Copyright (c) 2025 Burak TEMUR and Arda DEMİRHAN. All rights reserved.
This software is proprietary. Unauthorized use is prohibited.
"""

import os
import sys
import unittest
import ast

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))


class TestButtonVisibility(unittest.TestCase):
    """Test that the hide/show buttons are properly implemented in the UI"""
    
    def setUp(self):
        """Set up test environment"""
        # Read the USBManager.py file
        with open(os.path.join(os.path.dirname(__file__), '..', 'src', 'USBManager.py'), 'r', encoding='utf-8') as f:
            self.source_code = f.read()
    
    def test_language_dictionary_entries(self):
        """Test that the language dictionary entries for hide/show buttons exist"""
        # Import USBManager to access LANGUAGES dictionary
        import USBManager
        
        # Check Turkish entries
        self.assertIn('btn_hide', USBManager.LANGUAGES['tr'])
        self.assertIn('btn_show', USBManager.LANGUAGES['tr'])
        self.assertEqual(USBManager.LANGUAGES['tr']['btn_hide'], '👁️ Dosyayı Gizle')
        self.assertEqual(USBManager.LANGUAGES['tr']['btn_show'], '👁️ Dosyayı Göster')
        
        # Check English entries
        self.assertIn('btn_hide', USBManager.LANGUAGES['en'])
        self.assertIn('btn_show', USBManager.LANGUAGES['en'])
        self.assertEqual(USBManager.LANGUAGES['en']['btn_hide'], '👁️ Hide File')
        self.assertEqual(USBManager.LANGUAGES['en']['btn_show'], '👁️ Show File')
    
    def test_button_implementation_in_ui(self):
        """Test that the hide/show buttons are implemented in the UI"""
        # Check that the button creation code exists
        self.assertIn("ttk.Button(ops_grid, text=self.t('btn_hide'), command=self.hide_selected_file", self.source_code)
        self.assertIn("ttk.Button(ops_grid, text=self.t('btn_show'), command=self.show_selected_file", self.source_code)
        
        # Check that the grid layout includes row 3 for the new buttons
        self.assertIn("row=3, column=0", self.source_code)
        self.assertIn("row=3, column=1", self.source_code)
        
        # Check that the methods exist in the source code
        self.assertIn("def hide_selected_file(self):", self.source_code)
        self.assertIn("def show_selected_file(self):", self.source_code)
    
    def test_button_grid_layout(self):
        """Test that the button grid layout is properly configured"""
        # Check that columnconfigure is called for both columns
        self.assertIn("ops_grid.columnconfigure(0, weight=1)", self.source_code)
        self.assertIn("ops_grid.columnconfigure(1, weight=1)", self.source_code)


if __name__ == '__main__':
    unittest.main()