# File Visibility Management in USB Manager

## Overview

The USB Manager application now includes file visibility management functionality that allows users to:
1. Hide files from normal directory listings while maintaining their physical presence on USB devices
2. Reveal previously hidden files by restoring their visibility in standard file system views

This feature complements the existing encryption capabilities and provides an additional layer of privacy for sensitive files.

## Implementation Details

### Core Functions

The file visibility management is implemented using two core functions in the [encryption.py](file:///c%3A/Users/burak/OneDrive/Desktop/Burak/USBManager/src/encryption.py) module:

1. **[hide_file](file:///c%3A/Users/burak/OneDrive/Desktop/Burak/USBManager/src/encryption.py#L142-L172)** - Adds the hidden attribute to a file
2. **[make_file_visible](file:///c%3A/Users/burak/OneDrive/Desktop/Burak/USBManager/src/encryption.py#L113-L140)** - Removes the hidden attribute from a file

These functions use Windows `attrib` commands to manipulate file attributes:
- `attrib +h filename` - Hides a file
- `attrib -h -s -r filename` - Removes hidden, system, and read-only attributes

### Integration with USBManager GUI

The functionality is integrated into the main USBManager application through two new methods in the [USBManagerApp](file:///c%3A/Users/burak/OneDrive/Desktop/Burak/USBManager/src/USBManager.py#L458-L1447) class:

1. **[hide_selected_file](file:///c%3A/Users/burak/OneDrive/Desktop/Burak/USBManager/src/USBManager.py#L1282-L1308)** - Hides the currently selected file
2. **[show_selected_file](file:///c%3A/Users/burak/OneDrive/Desktop/Burak/USBManager/src/USBManager.py#L1310-L1337)** - Makes a hidden file visible

### User Interface

Two new buttons have been added to the file operations panel:
- **👁️ Hide File** - Hides the selected file
- **👁️ Show File** - Makes a hidden file visible

These buttons are available in both Turkish and English interfaces.

## Usage Instructions

### Hiding a File

1. Select a file from the file list or output area
2. Click the "👁️ Hide File" button (or "👁️ Dosyayı Gizle" in Turkish)
3. The file will be hidden from normal directory listings
4. A success message will be displayed, and the file will be removed from the found files list

### Showing a Hidden File

1. Select a hidden file from the file list or output area
2. Click the "👁️ Show File" button (or "👁️ Dosyayı Göster" in Turkish)
3. The file will become visible in standard file system views
4. A success message will be displayed, and the file will be added to the found files list

## Technical Considerations

### File Integrity

- Hidden files maintain their physical presence on the USB device
- File contents remain unchanged during visibility operations
- Access controls are preserved during visibility toggling

### Security

- Hidden files are only invisible to standard file browsing
- Files remain accessible through programmatic means
- Visibility operations do not provide encryption or additional security beyond hiding from casual view

### Platform Support

- Currently implemented for Windows platforms only
- Uses Windows-specific `attrib` command for attribute manipulation
- Hidden files on other platforms would require different approaches

## Testing

Unit tests for the visibility management functions are available in:
- [test_visibility.py](file:///c%3A/Users/burak/OneDrive/Desktop/Burak/USBManager/tests/test_visibility.py) - Tests for core functions
- [test_usbmanager_visibility.py](file:///c%3A/Users/burak/OneDrive/Desktop/Burak/USBManager/tests/test_usbmanager_visibility.py) - Tests for UI integration

Run tests with:
```bash
python -m pytest tests/test_visibility.py -v
```

## Error Handling

The implementation includes proper error handling for:
- Files that cannot be found
- Permission issues when modifying file attributes
- System errors during attribute manipulation

Error messages are displayed to the user through appropriate dialog boxes.