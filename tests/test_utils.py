#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
USB Manager - Unit Tests for Utility Functions

Copyright (c) 2025 Burak TEMUR and Arda DEMİRHAN. All rights reserved.
This software is proprietary. Unauthorized use is prohibited.
"""

import sys
import os
import unittest
from unittest.mock import patch, MagicMock

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from utils import is_hidden_or_system, maybe_text_sample

class TestUtils(unittest.TestCase):
    
    def test_maybe_text_sample_with_valid_text(self):
        """Test maybe_text_sample with valid text data"""
        data = b"Hello, World!"
        result = maybe_text_sample(data)
        self.assertEqual(result, "Hello, World!")
    
    def test_maybe_text_sample_with_binary_data(self):
        """Test maybe_text_sample with binary data"""
        data = b"\x00\x01\x02\x03"
        result = maybe_text_sample(data)
        self.assertIsNone(result)
    
    def test_maybe_text_sample_with_empty_data(self):
        """Test maybe_text_sample with empty data"""
        data = b""
        result = maybe_text_sample(data)
        self.assertEqual(result, "")
    
    def test_maybe_text_sample_with_unicode(self):
        """Test maybe_text_sample with unicode text"""
        data = "Merhaba Dünya! 🌍".encode('utf-8')
        result = maybe_text_sample(data)
        self.assertEqual(result, "Merhaba Dünya! 🌍")
    
    @patch('utils.GetFileAttributesW')
    def test_is_hidden_or_system_hidden_file(self, mock_get_attrs):
        """Test is_hidden_or_system with hidden file"""
        from utils import FILE_ATTRIBUTE_HIDDEN
        mock_get_attrs.return_value = FILE_ATTRIBUTE_HIDDEN
        result = is_hidden_or_system("test_file.txt")
        self.assertTrue(result)
    
    @patch('utils.GetFileAttributesW')
    def test_is_hidden_or_system_system_file(self, mock_get_attrs):
        """Test is_hidden_or_system with system file"""
        from utils import FILE_ATTRIBUTE_SYSTEM
        mock_get_attrs.return_value = FILE_ATTRIBUTE_SYSTEM
        result = is_hidden_or_system("test_file.txt")
        self.assertTrue(result)
    
    @patch('utils.GetFileAttributesW')
    def test_is_hidden_or_system_normal_file(self, mock_get_attrs):
        """Test is_hidden_or_system with normal file"""
        mock_get_attrs.return_value = 0  # No special attributes
        result = is_hidden_or_system("test_file.txt")
        self.assertFalse(result)
    
    @patch('utils.GetFileAttributesW')
    def test_is_hidden_or_system_invalid_file(self, mock_get_attrs):
        """Test is_hidden_or_system with invalid file path"""
        mock_get_attrs.return_value = 0xFFFFFFFF  # Invalid file
        result = is_hidden_or_system("invalid_file.txt")
        self.assertFalse(result)
    
    @patch('utils.GetFileAttributesW')
    def test_is_hidden_or_system_exception(self, mock_get_attrs):
        """Test is_hidden_or_system when exception occurs"""
        mock_get_attrs.side_effect = Exception("Test exception")
        result = is_hidden_or_system("test_file.txt")
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()