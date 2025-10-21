# 📁 USB Manager - Proje Yapısı

```
USBManager/
│
├── 📂 launchers/              # Başlatma scriptleri
│   ├── baslat.vbs             # VBScript launcher (gizli) ⭐
│   ├── create_shortcut.bat    # Masaüstü kısayolu oluşturucu
│   └── README.md              # Launcher kullanım kılavuzu
│
├── 📂 docs/                   # Dokümantasyon
│   ├── README.md              # Ana dokümantasyon (detaylı)
│   ├── QUICKSTART.md          # Hızlı başlangıç kılavuzu
│   ├── CHANGELOG.md           # Versiyon geçmişi
│   └── KONSOL_GIZLEME.md      # Konsol gizleme rehberi
│
├── 📂 src/                    # Kaynak kodlar
│   ├── USBManager.py          # Ana GUI uygulaması ⭐
│   ├── Secretfilescreator.py  # Legacy CLI file creator
│   ├── flashreader.py         # Legacy CLI scanner
│   └── __init__.py            # Python paket tanımı
│
├── 📂 assets/                 # Statik varlıklar
│   └── tool.ico               # Uygulama ikonu (512x512)
│
├── 📂 logs/                   # Log dosyaları (otomatik)
│   └── usbmanager_YYYYMMDD.log
│
├── 📄 README.md               # Proje ana README
├── 📄 PROJECT_STRUCTURE.md    # Bu dosya
├── 📄 LICENSE                 # Proprietary lisans
├── 📄 COPYRIGHT               # Telif hakkı bildirimi
├── 📄 requirements.txt        # Python bağımlılıkları
├── 📄 setup.py                # Paket kurulum scripti
└── 📄 .gitignore              # Git ignore kuralları
```

---

## 📋 Klasör Açıklamaları

### 📂 `launchers/` - Başlatıcılar

**Amaç:** Uygulamayı farklı yöntemlerle başlatmak

**İçerik:**
- VBScript launchers (gizli başlatma)
- Batch scriptler (konsol ile)
- PowerShell script (kısayol oluşturucu)
- Legacy launcher'lar (geriye uyumluluk)

**Kullanım:**
```cmd
launchers\baslat_gizli.vbs  # Önerilen
```

---

### 📂 `docs/` - Dokümantasyon

**Amaç:** Tüm kullanıcı dokümantasyonu

**İçerik:**
- Ana README (kapsamlı)
- Hızlı başlangıç kılavuzu
- Değişiklik günlüğü
- Özel rehberler

**Erişim:**
```
docs\README.md           # Ana kılavuz
docs\QUICKSTART.md       # Hızlı başlangıç
docs\CHANGELOG.md        # Versiyon geçmişi
```

---

### 📂 `src/` - Kaynak Kodlar

**Amaç:** Tüm Python kaynak kodları

**İçerik:**
- Ana GUI uygulaması
- Legacy CLI araçları
- Python paket tanımları

**Ana Dosya:**
```python
src\USBManager.py  # Modern GUI (ÖNERİLEN)
```

**Legacy Araçlar:**
```python
src\Secretfilescreator.py  # CLI file creator
src\flashreader.py         # CLI scanner
```

---

### 📂 `assets/` - Statik Varlıklar

**Amaç:** İkonlar ve görsel varlıklar

**İçerik:**
- Uygulama ikonu (512x512)
- Gelecekte: Ekran görüntüleri, logolar

---

### 📂 `logs/` - Log Dosyaları

**Amaç:** Otomatik log kayıtları

**Format:**
```
logs/usbmanager_20251021.log
```

**İçerik:**
- Uygulama işlemleri
- Hata mesajları
- Uyarılar
- Sistem bilgileri

**.gitignore'da:** ✅ İgnore edilir

---

## 📄 Kök Dizin Dosyaları

### `README.md` (Ana)

**Amaç:** Proje genel tanıtım  
**İçerik:**
- Hızlı başlangıç
- Özellikler özeti
- Kurulum adımları
- Proje yapısı özeti

### `LICENSE`

**Amaç:** Yasal koruma  
**Tip:** Proprietary  
**Yazarlar:** Burak TEMUR ve Arda DEMİRHAN

### `COPYRIGHT`

**Amaç:** Telif hakkı bildirimi  
**İçerik:** Copyright notice

### `requirements.txt`

**Amaç:** Python bağımlılıkları  
**İçerik:**
```
psutil>=5.9.0
```

### `setup.py`

**Amaç:** Paket kurulum scripti  
**Kullanım:**
```bash
pip install -e .        # Development mode
pip install .           # Normal install
```

### `.gitignore`

**Amaç:** Git ignore kuralları  
**İçerik:**
- `__pycache__/`
- `*.pyc`
- `logs/`
- `build/`, `dist/`
- vb.

---

## 🎯 Dosya Sayıları

| Kategori | Dosya Sayısı |
|----------|--------------|
| **Launcher** | 6 |
| **Docs** | 4 |
| **Source Code** | 4 |
| **Config** | 5 |
| **Assets** | 1 |
| **TOPLAM** | 20 |

---

## 📊 Dosya Boyutları (Yaklaşık)

| Klasör | Boyut |
|--------|-------|
| `launchers/` | ~10 KB |
| `docs/` | ~150 KB |
| `src/` | ~100 KB |
| `assets/` | ~66 KB |
| `logs/` | ~5 KB/gün |
| **TOPLAM** | ~330 KB |

---

## 🔍 Dosya Bulma Rehberi

### "Uygulamayı nasıl başlatırım?"

```
launchers\baslat.vbs
```

### "Kullanım kılavuzu nerede?"

```
docs\README.md
docs\QUICKSTART.md
```

### "Ana uygulama kodu nerede?"

```
src\USBManager.py
```

### "Log dosyaları nerede?"

```
logs\usbmanager_*.log
```

### "Değişiklik geçmişi nerede?"

```
docs\CHANGELOG.md
```

---

## 🗂️ Önceki vs Yeni Yapı

### ❌ Önceki (Karmaşık)

```
USBManager/
├── baslat.bat
├── baslat_gizli.vbs
├── create_shortcut.ps1
├── QUICKSTART.md
├── KONSOL_GIZLEME.md
├── CHANGELOG.md
├── README.md
├── src/
│   ├── baslat.bat
│   ├── baslat_gizli.vbs
│   └── ...
└── ...
```

**Sorunlar:**
- 📁 Kök dizinde çok fazla dosya
- 🔀 Launcher'lar dağınık
- 📚 Dokümantasyon karışık

### ✅ Yeni (Organize)

```
USBManager/
├── launchers/    # Tüm başlatıcılar
├── docs/         # Tüm dokümantasyon
├── src/          # Tüm kodlar
├── assets/       # Tüm varlıklar
└── [config files]
```

**Avantajlar:**
- ✅ Temiz kök dizin
- ✅ Kategorize dosyalar
- ✅ Kolay navigasyon
- ✅ Profesyonel yapı

---

## 📌 En Önemli Dosyalar

1. **`launchers\baslat_gizli.vbs`** - Uygulamayı başlat
2. **`docs\README.md`** - Ana kılavuz
3. **`src\USBManager.py`** - Ana kod
4. **`README.md`** - Proje tanıtım
5. **`LICENSE`** - Yasal bilgi

---

**Proje:** USB Manager v1.0.0  
**Yazarlar:** Burak TEMUR ve Arda DEMİRHAN  
**Platform:** Windows  
**Son Güncelleme:** 2025-10-21
