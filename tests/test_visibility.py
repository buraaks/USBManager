#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
USB Manager - File Visibility Management Tests

Copyright (c) 2025 Burak TEMUR and Arda DEMİRHAN. All rights reserved.
This software is proprietary. Unauthorized use is prohibited.
"""

import os
import sys
import tempfile
import unittest
from unittest.mock import patch, MagicMock

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from encryption import hide_file, make_file_visible


class TestFileVisibility(unittest.TestCase):
    """Test file visibility management functions"""
    
    def setUp(self):
        """Set up test environment"""
        # Create a temporary file for testing
        self.test_file = tempfile.NamedTemporaryFile(delete=False, suffix='.txt')
        self.test_file.write(b"Test content for visibility testing")
        self.test_file.close()
        
    def tearDown(self):
        """Clean up test environment"""
        # Remove test file if it exists
        if os.path.exists(self.test_file.name):
            os.remove(self.test_file.name)
            
        # Also try to remove any hidden versions
        hidden_name = '.' + os.path.basename(self.test_file.name)
        hidden_path = os.path.join(os.path.dirname(self.test_file.name), hidden_name)
        if os.path.exists(hidden_path):
            os.remove(hidden_path)
    
    @patch('subprocess.run')
    def test_hide_file_windows_success(self, mock_subprocess):
        """Test successful file hiding on Windows"""
        # Mock successful subprocess call
        mock_subprocess.return_value = MagicMock()
        
        # Test hiding file
        result = hide_file(self.test_file.name)
        
        # Verify the function returned True
        self.assertTrue(result)
        
        # Verify subprocess was called with correct arguments
        mock_subprocess.assert_called_once_with(["attrib", "+h", self.test_file.name], check=True)
    
    @patch('subprocess.run')
    def test_hide_file_windows_failure(self, mock_subprocess):
        """Test file hiding failure on Windows"""
        from subprocess import CalledProcessError
        
        # Mock subprocess failure
        mock_subprocess.side_effect = CalledProcessError(1, "attrib")
        
        # Test hiding file
        result = hide_file(self.test_file.name)
        
        # Verify the function returned False
        self.assertFalse(result)
    
    @patch('subprocess.run')
    def test_make_file_visible_windows_success(self, mock_subprocess):
        """Test successful file visibility restoration on Windows"""
        # Mock successful subprocess call
        mock_subprocess.return_value = MagicMock()
        
        # Test making file visible
        result = make_file_visible(self.test_file.name)
        
        # Verify the function returned True
        self.assertTrue(result)
        
        # Verify subprocess was called with correct arguments
        mock_subprocess.assert_called_once_with(["attrib", "-h", "-s", "-r", self.test_file.name], check=True)
    
    @patch('subprocess.run')
    def test_make_file_visible_windows_failure(self, mock_subprocess):
        """Test file visibility restoration failure on Windows"""
        from subprocess import CalledProcessError
        
        # Mock subprocess failure
        mock_subprocess.side_effect = CalledProcessError(1, "attrib")
        
        # Test making file visible
        result = make_file_visible(self.test_file.name)
        
        # Verify the function returned False
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()