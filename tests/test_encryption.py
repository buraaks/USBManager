#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
USB Manager - Unit Tests for Encryption Functions

Copyright (c) 2025 Burak TEMUR and Arda DEMİRHAN. All rights reserved.
This software is proprietary. Unauthorized use is prohibited.
"""

import sys
import os
import unittest
from unittest.mock import patch, mock_open
import tempfile

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from encryption import generate_key_from_password, encrypt_file, decrypt_file, encrypt_text, decrypt_text, make_file_visible, hide_file

class TestEncryption(unittest.TestCase):
    
    def test_generate_key_from_password(self):
        """Test key generation from password"""
        password = "test_password"
        key1, salt1 = generate_key_from_password(password)
        key2, salt2 = generate_key_from_password(password, salt1)
        
        # Same password and salt should generate same key
        self.assertEqual(key1, key2)
        # Same salt should be used
        self.assertEqual(salt1, salt2)
        
        # Different passwords should generate different keys
        key3, salt3 = generate_key_from_password("different_password", salt1)
        self.assertNotEqual(key1, key3)
    
    def test_encrypt_decrypt_text(self):
        """Test text encryption and decryption"""
        original_text = "This is a secret message! 🌍"
        password = "test_password"
        
        # Encrypt text
        encrypted_data = encrypt_text(original_text, password)
        self.assertIsInstance(encrypted_data, bytes)
        self.assertGreater(len(encrypted_data), 16)  # Should include salt
        
        # Decrypt text
        decrypted_text = decrypt_text(encrypted_data, password)
        self.assertEqual(original_text, decrypted_text)
    
    def test_encrypt_decrypt_file(self):
        """Test file encryption and decryption"""
        password = "test_password"
        
        # Create a temporary file with test content
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt', encoding='utf-8') as temp_file:
            temp_file.write("This is a secret file!\nWith multiple lines.\n")
            original_file_path = temp_file.name
        
        # Initialize variables
        encrypted_file_path = None
        decrypted_file_path = None
        
        try:
            # Encrypt file
            encrypted_file_path = encrypt_file(original_file_path, password)
            self.assertTrue(os.path.exists(encrypted_file_path))
            self.assertTrue(encrypted_file_path.endswith('.encrypted'))
            
            # Check if the encrypted file is hidden on Windows
            if os.name == 'nt':
                # We can't easily check file attributes in a cross-platform way in this test
                # but we can at least verify the file exists
                pass
            
            # Decrypt file
            decrypted_file_path = decrypt_file(encrypted_file_path, password)
            self.assertTrue(os.path.exists(decrypted_file_path))
            self.assertTrue(decrypted_file_path.endswith('.decrypted'))
            
            # Check content
            with open(decrypted_file_path, 'r', encoding='utf-8') as f:
                decrypted_content = f.read()
            
            with open(original_file_path, 'r', encoding='utf-8') as f:
                original_content = f.read()
                
            self.assertEqual(original_content, decrypted_content)
            
        finally:
            # Clean up temporary files
            for path in [original_file_path]:
                if os.path.exists(path):
                    os.remove(path)
            
            # Clean up encrypted and decrypted files if they exist
            if encrypted_file_path and os.path.exists(encrypted_file_path):
                os.remove(encrypted_file_path)
            if decrypted_file_path and os.path.exists(decrypted_file_path):
                os.remove(decrypted_file_path)
    
    def test_decrypt_with_wrong_password(self):
        """Test decryption with wrong password raises exception"""
        original_text = "Secret message"
        password = "correct_password"
        wrong_password = "wrong_password"
        
        # Encrypt text
        encrypted_data = encrypt_text(original_text, password)
        
        # Try to decrypt with wrong password
        with self.assertRaises(Exception):
            decrypt_text(encrypted_data, wrong_password)
            
    def test_make_file_visible(self):
        """Test making a file visible"""
        # Create a temporary file
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt', encoding='utf-8') as temp_file:
            temp_file.write("Test content")
            test_file_path = temp_file.name
            
        try:
            # Test making file visible
            # On non-Windows systems, this should always return True
            result = make_file_visible(test_file_path)
            self.assertIsInstance(result, bool)
            
            # File should still exist
            self.assertTrue(os.path.exists(test_file_path))
            
        finally:
            # Clean up
            if os.path.exists(test_file_path):
                os.remove(test_file_path)
                
    def test_hide_file(self):
        """Test hiding a file"""
        # Create a temporary file
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt', encoding='utf-8') as temp_file:
            temp_file.write("Test content")
            test_file_path = temp_file.name
            
        try:
            # Test hiding file
            # On non-Windows systems, this should always return True
            result = hide_file(test_file_path)
            self.assertIsInstance(result, bool)
            
            # File should still exist
            self.assertTrue(os.path.exists(test_file_path))
            
        finally:
            # Clean up
            if os.path.exists(test_file_path):
                os.remove(test_file_path)

if __name__ == '__main__':
    unittest.main()