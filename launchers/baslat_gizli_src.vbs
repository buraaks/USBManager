Set WshShell = CreateObject("WScript.Shell")

' Calisma dizinini ayarla
strPath = CreateObject("Scripting.FileSystemObject").GetParentFolderName(WScript.ScriptFullName)
WshShell.CurrentDirectory = strPath

' Sessizce pythonw ile baslat (konsol yok)
WshShell.Run "pythonw.exe USBManager.py", 0, False

' Script'i kapat
Set WshShell = Nothing
