#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
USB Manager - USBManager Visibility Integration Tests

Copyright (c) 2025 Burak TEMUR and Arda DEMİRHAN. All rights reserved.
This software is proprietary. Unauthorized use is prohibited.
"""

import os
import sys
import tempfile
import unittest
from unittest.mock import patch, MagicMock, mock_open

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import USBManager


class TestUSBManagerVisibility(unittest.TestCase):
    """Test USBManager file visibility integration"""
    
    def setUp(self):
        """Set up test environment"""
        # Create a mock USBManager app instance
        with patch('USBManager.tk.Tk.__init__', return_value=None):
            self.app = USBManager.USBManagerApp()
            # Manually set required attributes
            self.app.found_files = []
    
    def test_hide_selected_file_no_selection(self):
        """Test hide_selected_file when no file is selected"""
        with patch('USBManager.messagebox.showwarning') as mock_warning:
            # Mock get_selected_file to return None
            with patch.object(self.app, 'get_selected_file', return_value=None):
                self.app.hide_selected_file()
                mock_warning.assert_called_once_with("No Selection", "Please select a file to hide (from combobox or output area).")
    
    def test_show_selected_file_no_selection(self):
        """Test show_selected_file when no file is selected"""
        with patch('USBManager.messagebox.showwarning') as mock_warning:
            # Mock get_selected_file to return None
            with patch.object(self.app, 'get_selected_file', return_value=None):
                self.app.show_selected_file()
                mock_warning.assert_called_once_with("No Selection", "Please select a file to show (from combobox or output area).")
    
    @patch('USBManager.encryption.hide_file')
    @patch('USBManager.messagebox.showinfo')
    @patch('USBManager.messagebox.showerror')
    def test_hide_selected_file_success(self, mock_error, mock_info, mock_hide):
        """Test successful file hiding"""
        # Mock hide_file to return True (success)
        mock_hide.return_value = True
        
        # Create a temporary file path for testing
        test_file = "C:\\test\\test_file.txt"
        
        # Mock get_selected_file to return our test file
        with patch.object(self.app, 'get_selected_file', return_value=test_file):
            with patch.object(self.app, 'update_file_combo'):
                self.app.hide_selected_file()
                
                # Verify hide_file was called with correct argument
                mock_hide.assert_called_once_with(test_file)
                
                # Verify success message was shown
                mock_info.assert_called_once()
                
                # Verify no error message was shown
                mock_error.assert_not_called()
    
    @patch('USBManager.encryption.hide_file')
    @patch('USBManager.messagebox.showinfo')
    @patch('USBManager.messagebox.showerror')
    def test_hide_selected_file_failure(self, mock_error, mock_info, mock_hide):
        """Test file hiding failure"""
        # Mock hide_file to return False (failure)
        mock_hide.return_value = False
        
        # Create a temporary file path for testing
        test_file = "C:\\test\\test_file.txt"
        
        # Mock get_selected_file to return our test file
        with patch.object(self.app, 'get_selected_file', return_value=test_file):
            self.app.hide_selected_file()
            
            # Verify hide_file was called with correct argument
            mock_hide.assert_called_once_with(test_file)
            
            # Verify error message was shown
            mock_error.assert_called_once()
            
            # Verify no success message was shown
            mock_info.assert_not_called()
    
    @patch('USBManager.encryption.make_file_visible')
    @patch('USBManager.messagebox.showinfo')
    @patch('USBManager.messagebox.showerror')
    def test_show_selected_file_success(self, mock_error, mock_info, mock_show):
        """Test successful file visibility restoration"""
        # Mock make_file_visible to return True (success)
        mock_show.return_value = True
        
        # Create a temporary file path for testing
        test_file = "C:\\test\\test_file.txt"
        
        # Mock get_selected_file to return our test file
        with patch.object(self.app, 'get_selected_file', return_value=test_file):
            with patch.object(self.app, 'update_file_combo'):
                self.app.show_selected_file()
                
                # Verify make_file_visible was called with correct argument
                mock_show.assert_called_once_with(test_file)
                
                # Verify success message was shown
                mock_info.assert_called_once()
                
                # Verify no error message was shown
                mock_error.assert_not_called()
    
    @patch('USBManager.encryption.make_file_visible')
    @patch('USBManager.messagebox.showinfo')
    @patch('USBManager.messagebox.showerror')
    def test_show_selected_file_failure(self, mock_error, mock_info, mock_show):
        """Test file visibility restoration failure"""
        # Mock make_file_visible to return False (failure)
        mock_show.return_value = False
        
        # Create a temporary file path for testing
        test_file = "C:\\test\\test_file.txt"
        
        # Mock get_selected_file to return our test file
        with patch.object(self.app, 'get_selected_file', return_value=test_file):
            self.app.show_selected_file()
            
            # Verify make_file_visible was called with correct argument
            mock_show.assert_called_once_with(test_file)
            
            # Verify error message was shown
            mock_error.assert_called_once()
            
            # Verify no success message was shown
            mock_info.assert_not_called()


if __name__ == '__main__':
    unittest.main()