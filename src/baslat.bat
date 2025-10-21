@echo off
echo ================================================
echo   USB Flash Surucu Yonetim Merkezi
echo ================================================
echo.
echo Gereksinimler kontrol ediliyor...
python -c "import psutil" 2>nul
if errorlevel 1 (
    echo psutil kutuphanesi bulunamadi. Yukleniyor...
    pip install -r ../requirements.txt
) else (
    echo Tum gereksinimler yuklu!
)
echo.
echo Uygulama baslatiliyor...
echo.
python USBManager.py
pause
