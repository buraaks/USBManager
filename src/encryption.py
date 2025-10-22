#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
USB Manager - Encryption Utilities

Copyright (c) 2025 Burak TEMUR and Arda DEMİRHAN. All rights reserved.
This software is proprietary. Unauthorized use is prohibited.
"""

import os
import hashlib
import subprocess
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64

def generate_key_from_password(password: str, salt: bytes | None = None) -> tuple[bytes, bytes]:
    """
    Generate an encryption key from a password using PBKDF2
    
    Args:
        password (str): Password to derive key from
        salt (bytes): Salt for key derivation (randomly generated if None)
        
    Returns:
        tuple: (key, salt) - Encryption key and salt used
    """
    if salt is None:
        salt = os.urandom(16)
    
    # Derive key using PBKDF2
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key, salt

def encrypt_file(file_path: str, password: str) -> str:
    """
    Encrypt a file using a password
    
    Args:
        file_path (str): Path to file to encrypt
        password (str): Password to use for encryption
        
    Returns:
        str: Path to encrypted file
    """
    # Generate key from password
    key, salt = generate_key_from_password(password)
    fernet = Fernet(key)
    
    # Read file data
    with open(file_path, 'rb') as file:
        file_data = file.read()
    
    # Encrypt data
    encrypted_data = fernet.encrypt(file_data)
    
    # Write encrypted data with salt prepended
    encrypted_file_path = file_path + '.encrypted'
    with open(encrypted_file_path, 'wb') as file:
        file.write(salt)  # Write salt first
        file.write(encrypted_data)  # Then write encrypted data
    
    # Make the encrypted file hidden on Windows
    if os.name == 'nt':
        try:
            subprocess.run(["attrib", "+h", encrypted_file_path], check=True)
        except subprocess.CalledProcessError:
            # If attrib command fails, continue without hiding the file
            pass
    
    return encrypted_file_path

def decrypt_file(encrypted_file_path: str, password: str) -> str:
    """
    Decrypt a file using a password
    
    Args:
        encrypted_file_path (str): Path to encrypted file
        password (str): Password used for encryption
        
    Returns:
        str: Path to decrypted file
    """
    # Read encrypted file
    with open(encrypted_file_path, 'rb') as file:
        salt = file.read(16)  # Read salt first
        encrypted_data = file.read()  # Then read encrypted data
    
    # Generate key from password and salt
    key, _ = generate_key_from_password(password, salt)
    fernet = Fernet(key)
    
    # Decrypt data
    decrypted_data = fernet.decrypt(encrypted_data)
    
    # Write decrypted data
    decrypted_file_path = encrypted_file_path.replace('.encrypted', '.decrypted')
    with open(decrypted_file_path, 'wb') as file:
        file.write(decrypted_data)
    
    return decrypted_file_path

def make_file_visible(file_path: str) -> bool:
    """
    Remove hidden attribute from a file, making it visible
    
    Args:
        file_path (str): Path to file to make visible
        
    Returns:
        bool: True if successful, False otherwise
    """
    if os.name == 'nt':  # Windows
        try:
            # Remove hidden, system, and read-only attributes
            subprocess.run(["attrib", "-h", "-s", "-r", file_path], check=True)
            return True
        except subprocess.CalledProcessError:
            return False
    else:
        # On non-Windows systems, hidden files start with a dot
        # To make them visible, we would need to rename them
        # This is a simplified implementation
        try:
            if os.path.basename(file_path).startswith('.'):
                new_path = os.path.join(
                    os.path.dirname(file_path),
                    os.path.basename(file_path)[1:]  # Remove the leading dot
                )
                os.rename(file_path, new_path)
                return True
            return True  # File was already visible
        except OSError:
            return False

def hide_file(file_path: str) -> bool:
    """
    Add hidden attribute to a file, making it invisible in standard file system view
    
    Args:
        file_path (str): Path to file to hide
        
    Returns:
        bool: True if successful, False otherwise
    """
    if os.name == 'nt':  # Windows
        try:
            # Add hidden attribute
            subprocess.run(["attrib", "+h", file_path], check=True)
            return True
        except subprocess.CalledProcessError:
            return False
    else:
        # On non-Windows systems, hidden files start with a dot
        # To hide them, we need to rename them to start with a dot
        try:
            filename = os.path.basename(file_path)
            if not filename.startswith('.'):
                new_path = os.path.join(
                    os.path.dirname(file_path),
                    '.' + filename  # Add leading dot
                )
                os.rename(file_path, new_path)
                return True
            return True  # File was already hidden
        except OSError:
            return False

def encrypt_text(text: str, password: str) -> bytes:
    """
    Encrypt text using a password
    
    Args:
        text (str): Text to encrypt
        password (str): Password to use for encryption
        
    Returns:
        bytes: Encrypted text with salt prepended
    """
    # Generate key from password
    key, salt = generate_key_from_password(password)
    fernet = Fernet(key)
    
    # Encrypt text
    encrypted_text = fernet.encrypt(text.encode())
    
    # Return salt + encrypted text
    return salt + encrypted_text

def decrypt_text(encrypted_data: bytes, password: str) -> str:
    """
    Decrypt text using a password
    
    Args:
        encrypted_data (bytes): Encrypted text with salt prepended
        password (str): Password used for encryption
        
    Returns:
        str: Decrypted text
    """
    # Extract salt and encrypted text
    salt = encrypted_data[:16]
    encrypted_text = encrypted_data[16:]
    
    # Generate key from password and salt
    key, _ = generate_key_from_password(password, salt)
    fernet = Fernet(key)
    
    # Decrypt text
    decrypted_text = fernet.decrypt(encrypted_text)
    
    return decrypted_text.decode()