@echo off
cd /d "%~dp0"
echo ================================================
echo   USB Flash Surucu Yonetim Merkezi
echo ================================================
echo.
echo Gereksinimler kontrol ediliyor...
python -c "import psutil" 2>nul
if errorlevel 1 (
    echo psutil kutuphanesi bulunamadi. Yukleniyor...
    pip install -r ../requirements.txt
)
echo.
echo Uygulama baslatiliyor...
echo.
echo Konsol penceresi 2 saniye sonra kapanacak...
timeout /t 2 /nobreak >nul

REM GUI modunda baslat (konsol gizli)
start "" pythonw.exe USBManager.py

REM Batch penceresini kapat
exit
