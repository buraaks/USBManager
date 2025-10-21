@echo off
REM USB Manager - Masaustu Kisayolu Olusturucu
REM Burak TEMUR ve Arda DEMIRHAN

echo.
echo ========================================
echo   USB Manager - Kisayol Olusturucu  
echo ========================================
echo.
echo [1/5] Masaustu yolu bulunuyor...
echo [2/5] Proje dizini ayarlaniyor...
echo [3/5] pythonw.exe kontrol ediliyor...
echo [4/5] Kisayol olusturuluyor...
echo [5/5] Ikon ayarlaniyor...
echo.

REM PowerShell ile kisayol olustur
powershell -ExecutionPolicy Bypass -Command "& { $Desktop = [Environment]::GetFolderPath('Desktop'); $Shell = New-Object -ComObject WScript.Shell; $Shortcut = $Shell.CreateShortcut(\"$Desktop\USB Manager.lnk\"); $ScriptDir = Split-Path -Parent '%~f0'; $ProjectPath = Split-Path -Parent $ScriptDir; $Shortcut.TargetPath = 'pythonw.exe'; $Shortcut.Arguments = 'USBManager.py'; $Shortcut.WorkingDirectory = Join-Path $ProjectPath 'src'; $Shortcut.Description = 'USB Manager'; $IconPath = Join-Path $ProjectPath 'assets\tool.ico'; if (Test-Path $IconPath) { $Shortcut.IconLocation = $IconPath }; $Shortcut.Save(); Write-Host ''; Write-Host '================================' -ForegroundColor Green; Write-Host '  BASARILI!' -ForegroundColor Green; Write-Host '================================' -ForegroundColor Green; Write-Host ''; Write-Host 'Konum:' $Desktop'\USB Manager.lnk' -ForegroundColor Cyan; Write-Host ''; Write-Host 'Masaustundeki USB Manager ikonuna cift tiklayin!' -ForegroundColor Yellow }"

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo HATA: Kisayol olusturulamadi!
    echo.
) else (
    echo.
    echo Kisayol basariyla olusturuldu!
    echo.
)

pause
