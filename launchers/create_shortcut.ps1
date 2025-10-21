# USB Manager - Masaustu Kisayolu Olusturucu
# Bu script masaustune konsol olmadan calisacak bir kisayol olusturur

$WshShell = New-Object -ComObject WScript.Shell

# Masaustu yolu
$DesktopPath = [Environment]::GetFolderPath("Desktop")
$ShortcutPath = "$DesktopPath\USB Manager.lnk"

# Kisayol olustur
$Shortcut = $WshShell.CreateShortcut($ShortcutPath)

# Launcher dizini
$LauncherPath = Split-Path -Parent $PSScriptRoot
$ProjectPath = Split-Path -Parent $LauncherPath
$SrcPath = Join-Path $ProjectPath "src"

# Hedef: pythonw.exe (konsol yok)
$PythonwPath = (Get-Command pythonw.exe).Source
$Shortcut.TargetPath = $PythonwPath
$Shortcut.Arguments = "USBManager.py"
$Shortcut.WorkingDirectory = $SrcPath
$Shortcut.Description = "USB Flash Surucu Yonetim Merkezi"
$Shortcut.WindowStyle = 1  # Normal window

# Ikon ayarla (eger varsa)
$IconPath = Join-Path $ProjectPath "assets\tool.ico"
if (Test-Path $IconPath) {
    $Shortcut.IconLocation = $IconPath
}

# Kaydet
$Shortcut.Save()

Write-Host "================================" -ForegroundColor Green
Write-Host "  KISAYOL OLUSTURULDU!" -ForegroundColor Green
Write-Host "================================" -ForegroundColor Green
Write-Host ""
Write-Host "Konum: $ShortcutPath" -ForegroundColor Cyan
Write-Host ""
Write-Host "Artik masaustundeki 'USB Manager' ikonuna" -ForegroundColor Yellow
Write-Host "cift tiklayarak uygulamayi baslatabilirsiniz!" -ForegroundColor Yellow
Write-Host ""
Write-Host "Konsol penceresi GOZUKMEYECEK." -ForegroundColor Green
Write-Host ""
pause
