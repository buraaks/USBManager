# 🚀 Hızlı Başlangıç Kılavuzu

## 📹 İDEAL KULLANIM: Konsol Olmadan Başlatma ⭐

### Yöntem 1: VBScript ile (Tamamen Gizli)

**Root klasörden:**
```cmd
# Çift tıklama:
baslat_gizli.vbs
```

**src klasöründen:**
```cmd
# Çift tıklama:
src\baslat_gizli.vbs
```

**Avantajları:**
- ✅ Konsol penceresi HIÇ gözükmüyor
- ✅ Sessizce arkaplanda başlıyor
- ✅ Sadece GUI görünür
- ✅ Profesyonel görünüm

### Yöntem 2: Masaaüstü Kısayolu Oluştur (EN KOLAY)

**Adım 1:** PowerShell scripti çalıştır
```powershell
# Sağ tık -> PowerShell ile çalıştır:
create_shortcut.ps1
```

**Adım 2:** Masaaüstüne oluşan "USB Manager" ikonuna çift tıkla

**Avantajları:**
- 🎯 Tek tıklama ile başlat
- 👀 Konsol yok, sadece GUI
- 🎨 İkonlu kısayol
- 📌 Masaaüstünden kolay erişim

---

## 💻 Konsol ile Başlatma (Debug için)

### Yöntem 3: Batch Script (Konsol 2sn sonra kapanır)

**Root klasörden:**
```cmd
baslat.bat
```

**src klasöründen:**
```cmd
cd src
baslat.bat
```

**Not:** Konsol 2 saniye sonra otomatik kapanır, uygulama açık kalır.

### Yöntem 2: Manuel Başlatma

```cmd
# 1. src klasörüne gidin
cd src

# 2. Bağımlılıkları yükleyin
pip install -r ../requirements.txt

# 3. Uygulamayı başlatın
python USBManager.py
```

### Yöntem 3: Python ile Direkt

```cmd
cd src
python -m USBManager
```

---

## ⚠️ Sık Karşılaşılan Sorunlar

### ❌ "No such file or directory" Hatası

**Sorun**: Batch dosyası yanlış dizinden çalıştırılıyor.

**Çözüm**:
```cmd
# 1. Komut istemini KAPAT
# 2. baslat.bat dosyasına SAĞ TIKLAYIN
# 3. "Yönetici olarak çalıştır" seçin
```

### ❌ "ModuleNotFoundError: No module named 'psutil'"

**Çözüm**:
```cmd
pip install psutil
# VEYA
pip install -r requirements.txt
```

### ❌ "Access Denied" Hatası

**Çözüm**:
- Batch dosyasını **yönetici olarak** çalıştırın
- Windows Defender/Antivirüs yazılımında izin verin

---

## 🎯 Doğru Kullanım

### ✅ DOĞRU:
```cmd
C:\Users\burak\OneDrive\Desktop\USBManager> baslat.bat
C:\Users\burak\OneDrive\Desktop\USBManager\src> baslat.bat
```

### ❌ YANLIŞ:
```cmd
C:\Windows\System32> python USBManager.py  # ❌ Dosya bulunamaz!
C:\> baslat.bat  # ❌ Yanlış dizin!
```

---

## 📂 Proje Yapısı

```
USBManager/
├── baslat.bat          ← Buradan çalıştırın (root)
├── src/
│   ├── baslat.bat      ← VEYA buradan
│   ├── USBManager.py   ← Ana uygulama
│   └── ...
├── requirements.txt
└── README.md
```

---

## 🔧 Sistem Gereksinimleri

- ✅ **Windows** 7/8/10/11
- ✅ **Python** 3.8+
- ✅ **psutil** kütüphanesi
- ✅ Yönetici yetkisi (önerilen)

---

## 📞 Destek

Sorun yaşıyorsanız:

1. **Adım 1**: Bu dosyayı okuyun
2. **Adım 2**: [README.md](README.md) dosyasını kontrol edin
3. **Adım 3**: [CHANGELOG.md](CHANGELOG.md) dosyasına bakın
4. **Adım 4**: Log dosyalarını inceleyin (`logs/` klasörü)

---

## ✨ Klavye Kısayolları

- **F5** veya **Ctrl+R**: Sürücüleri yenile
- **Ctrl+S**: Taramayı başlat
- **Ctrl+N**: Dosya oluştur
- **Esc**: Taramayı durdur
- **Delete**: Seçili dosyayı sil
- **Ctrl+Q**: Çıkış

---

**Yazarlar**: Burak TEMUR ve Arda DEMİRHAN  
**Versiyon**: 1.0.0  
**Platform**: Windows
