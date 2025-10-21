"""
USB Manager - Advanced USB Drive File Management and Security Tool
"""

from setuptools import setup, find_packages
import os

# Read the contents of README file
def read_file(filename):
    filepath = os.path.join(os.path.dirname(__file__), filename)
    if os.path.exists(filepath):
        with open(filepath, encoding='utf-8') as f:
            return f.read()
    return "USB Manager - Advanced USB Drive File Management and Security Tool"

setup(
    name='usbmanager',
    version='1.0.0',
    author='Burak TEMUR and Arda DEMİRHAN',
    description='Python-based tool for advanced USB drive file management and security',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/usbmanager',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: System Administrators',
        'Intended Audience :: End Users/Desktop',
        'Topic :: System :: Systems Administration',
        'Topic :: Utilities',
        'License :: Other/Proprietary License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Operating System :: Microsoft :: Windows',
    ],
    python_requires='>=3.8',
    install_requires=[
        'psutil>=5.9.0',
    ],
    extras_require={
        'dev': [
            'pytest>=7.0',
            'pytest-cov>=4.0',
        ],
    },
    entry_points={
        'console_scripts': [
            'usbmanager=USBManager:main',
        ],
    },
    include_package_data=True,
    package_data={
        '': ['*.ico', '*.bat'],
    },
    zip_safe=False,
    keywords='usb flash drive security file management hidden system proprietary',
    project_urls={
        'Bug Reports': 'https://github.com/yourusername/usbmanager/issues',
        'Source': 'https://github.com/yourusername/usbmanager',
    },
)
