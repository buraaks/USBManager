Set WshShell = CreateObject("WScript.Shell")

' Ana proje dizinini bul
strScriptPath = CreateObject("Scripting.FileSystemObject").GetParentFolderName(WScript.ScriptFullName)
strProjectPath = CreateObject("Scripting.FileSystemObject").GetParentFolderName(strScriptPath)

' src klasorune git
WshShell.CurrentDirectory = strProjectPath & "\src"

' Pythonw ile GUI'yi baslat (konsol olmadan)
WshShell.Run "pythonw.exe USBManager.py", 0, False

Set WshShell = Nothing
