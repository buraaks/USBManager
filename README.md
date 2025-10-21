# 🔧 USB Manager

**Advanced USB Drive File Management and Security Tool**

[![Version](https://img.shields.io/badge/version-1.0.0-blue)](https://github.com/yourusername/usbmanager)
[![Python](https://img.shields.io/badge/python-3.8+-green)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-Proprietary-red)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows-lightgrey)](https://www.microsoft.com/windows)

---

## 🚀 Hızlı Başlangıç

### En Kolay Yöntem (Önerilen)

```cmd
# Proje klasörünü açın
cd USBManager

# Uygulamayı başlatın (konsol yok)
launchers\baslat.vbs
```

**Veya çift tıklama:** `launchers\baslat.vbs`

---

## 📋 İçindekiler

- [Özellikler](#-özellikler)
- [Kurulum](#-kurulum)
- [Kullanım](#-kullanım)
- [Proje Yapısı](#-proje-yapısı)
- [Dokümantasyon](#-dokümantasyon)
- [Lisans](#-lisans)

---

## ✨ Özellikler

- 📝 **Gizli Dosya Oluşturma** - Hidden, System, Read-only öznitelikleri
- 🔍 **Gelişmiş Tarama** - Gizli ve sistem dosyalarını bul
- 👁️ **İçerik Önizleme** - Metin dosyalarını hızlıca görüntüle
- 🗑️ **Güvenli Silme** - Dosya özniteliklerini otomatik kaldırma
- 💾 **Rapor Kaydetme** - Tarama sonuçlarını .txt olarak kaydet
- 🔄 **USB Algılama** - Otomatik volume label ve detaylı bilgi
- ⌨️ **Klavye Kısayolları** - Hızlı erişim (F5, Ctrl+S, Ctrl+N, vb.)
- 📊 **İlerleme Göstergesi** - Real-time tarama ilerlemesi
- 📝 **Logging Sistemi** - Detaylı işlem kayıtları
- 🎨 **Modern GUI** - Koyu tema, renkli çıktı

---

## 🛠️ Kurulum

### Gereksinimler

- Windows 7/8/10/11
- Python 3.8 veya üzeri
- 512 MB RAM (1 GB önerilir)

### Adımlar

```cmd
# 1. Depoyu klonlayın
git clone https://github.com/yourusername/USBManager.git
cd USBManager

# 2. Bağımlılıkları yükleyin
pip install -r requirements.txt

# 3. Uygulamayı başlatın
launchers\baslat.vbs
```

---

## 📖 Kullanım

### Yöntem 1: VBScript Launcher (Önerilen)

```cmd
# Konsol olmadan başlat
launchers\baslat.vbs
```

### Yöntem 2: Masaüstü Kısayolu Oluştur

```cmd
# Çift tıklama:
launchers\create_shortcut.bat

# Masaüstünde "USB Manager" ikonu oluşturulur
```

### Yöntem 3: Batch Script

```cmd
# Konsol 2 saniye görünür, sonra kapanır
launchers\baslat.bat
```

### Detaylı Kullanım Kılavuzu

Tüm özellikler için: [📚 Hızlı Başlangıç Kılavuzu](docs/QUICKSTART.md)

---

## 📁 Proje Yapısı

```
USBManager/
├── 📂 launchers/           # Başlatma scriptleri
│   ├── baslat.vbs          # VBScript launcher (önerilen) ⭐
│   ├── create_shortcut.ps1 # Masaüstü kısayolu oluşturucu
│   └── README.md           # Launcher kullanım kılavuzu
│
├── 📂 docs/                # Dokümantasyon
│   ├── README.md           # Ana dokümantasyon
│   ├── QUICKSTART.md       # Hızlı başlangıç
│   ├── CHANGELOG.md        # Değişiklik günlüğü
│   └── KONSOL_GIZLEME.md   # Konsol gizleme rehberi
│
├── 📂 src/                 # Kaynak kodlar
│   ├── USBManager.py       # Ana uygulama ⭐
│   ├── Secretfilescreator.py  # Legacy CLI tool
│   ├── flashreader.py      # Legacy scanner
│   └── __init__.py
│
├── 📂 assets/              # Statik varlıklar
│   └── tool.ico            # Uygulama ikonu
│
├── 📂 logs/                # Log dosyaları (otomatik)
│   └── usbmanager_*.log
│
├── 📄 LICENSE              # Proprietary license
├── 📄 COPYRIGHT            # Telif hakkı
├── 📄 requirements.txt     # Python bağımlılıkları
├── 📄 setup.py             # Paket kurulum scripti
└── 📄 .gitignore           # Git ignore kuralları
```

---

## 📚 Dokümantasyon

| Dosya | Açıklama |
|-------|----------|
| [📖 README.md](docs/README.md) | Kapsamlı kullanım rehberi |
| [🚀 QUICKSTART.md](docs/QUICKSTART.md) | Hızlı başlangıç kılavuzu |
| [📝 CHANGELOG.md](docs/CHANGELOG.md) | Versiyon geçmişi |
| [🖥️ KONSOL_GIZLEME.md](docs/KONSOL_GIZLEME.md) | Konsol penceresini gizleme |

---

## 🔑 Önemli Notlar

### Yönetici Yetkisi

Bazı özellikler için yönetici yetkisi gerekir:
- Sistem dosyası özniteliği ayarlama
- Gizli/sistem dosyalarını silme
- Dosya özniteliklerini değiştirme

### Desteklenen Dosya Sistemleri

- ✅ FAT32
- ✅ NTFS
- ✅ exFAT

---

## ⌨️ Klavye Kısayolları

| Kısayol | İşlev |
|---------|-------|
| `F5` veya `Ctrl+R` | Sürücüleri yenile |
| `Ctrl+S` | Taramayı başlat |
| `Ctrl+N` | Dosya oluştur |
| `Esc` | Taramayı durdur |
| `Delete` | Seçili dosyayı sil |
| `Ctrl+Q` | Çıkış |

---

## 🐛 Sorun Bildirme

Sorun mu yaşıyorsunuz?

1. [Log dosyalarını](logs/) kontrol edin
2. [Sorun Giderme](docs/QUICKSTART.md#sorun-giderme) bölümüne bakın
3. GitHub Issues'da yeni bir sorun açın

---

## 📊 Sistem Gereksinimleri

| Bileşen | Minimum | Önerilen |
|---------|---------|----------|
| **OS** | Windows 7 | Windows 10/11 |
| **Python** | 3.8 | 3.11+ |
| **RAM** | 512 MB | 1 GB |
| **Disk** | 15 MB | 50 MB |

---

## 🤝 Katkıda Bulunma

Bu proje proprietary lisans altındadır. Katkılar kabul edilmemektedir.

---

## 📜 Lisans

**Proprietary License** - Tüm hakları saklıdır.

Copyright © 2025 **Burak TEMUR ve Arda DEMİRHAN**

Bu yazılım ve kaynak kodları tüm hakları saklıdır. Yazarların açık yazılı izni olmaksızın kullanım, kopyalama, dağıtım veya değiştirme **yasaktır**.

Detaylar için [LICENSE](LICENSE) dosyasına bakın.

---

## 👨‍💻 Yazarlar

- **Burak TEMUR**
- **Arda DEMİRHAN**

---

## 🙏 Teşekkürler

- Python Software Foundation
- psutil Developers
- Windows API Documentation
- tkinter Community

---

<div align="center">

**Made with ❤️ by Burak TEMUR ve Arda DEMİRHAN**

[⬆ Başa Dön](#-usb-manager)

</div>
