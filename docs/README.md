# 🔧 USB Manager - USB Flash Sürücü Yönetim Aracı

Modern ve kullanıcı dostu USB flash sürücü yönetim ve güvenlik aracı.

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-Proprietary-red)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey)

---

## 📋 İçindekiler

- [Proje Hakkında](#-proje-hakkında)
- [Özellikler](#-özellikler)
- [Kurulum](#-kurulum)
- [Hızlı Başlangıç](#-hızlı-başlangıç)
- [Kullanım Kılavuzu](#-kullanım-kılavuzu)
- [Proje Yapısı](#-proje-yapısı)
- [Teknik Detaylar](#️-teknik-detaylar)
- [Sorun Giderme](#-sorun-giderme)
- [Kullanım Senaryoları](#-kullanım-senaryoları)
- [Özellik Karşılaştırması](#-özellik-karşılaştırması)
- [Telif Hakkı ve Lisans](#️-telif-hakkı-ve-lisans)

---

## 📖 Proje Hakkında

**USB Manager** is a Python-based tool for advanced USB drive file management and security. This application integrates all functionalities from legacy scripts (`Secretfilescreator.py` and `flashreader.py`) into a modern GUI interface, while maintaining backward compatibility with the legacy tools.

### 🎯 Amaç ve Kullanım Alanları

- **Güvenlik Token'ları Oluşturma**: USB sürücülerde gizli kimlik doğrulama dosyaları
- **Güvenlik Taraması**: Şüpheli gizli dosyaları tespit etme
- **Yedekleme Yönetimi**: Şifrelenmiş yedek dosyalarını saklama
- **Sistem Yönetimi**: USB sürücü güvenlik denetimi
- **Dosya Güvenliği**: Önemli dosyaları gizli ve korumalı saklama

### 💡 Neden USB Manager?

- ✅ **Kullanımı Kolay**: Modern GUI ile sezgisel arayüz
- ✅ **Güvenilir**: Windows API kullanarak doğrudan sistem seviyesinde işlem
- ✅ **Hızlı**: Asenkron tarama ile yüksek performans
- ✅ **Kapsamlı**: Dosya oluşturma, tarama, silme, kopyalama - hepsi tek yerde
- ✅ **Türkçe**: Tam Türkçe dil desteği

---

## ✨ Özellikler

### 📝 Dosya Oluşturma ve Yönetimi

- **Çok satırlı metin desteği**: Flash sürücüde birden fazla satır içeren dosyalar oluşturun
- **Özelleştirilebilir dosya adı**: İstediğiniz dosya adını belirleyin
- **Gelişmiş dosya öznitelikleri**:
  - 🔒 **Gizli (Hidden)**: Windows Explorer'da görünmez dosyalar
  - ⚙️ **Sistem (System)**: Sistem dosyası olarak işaretleme
  - 📖 **Salt okunur (Read-only)**: Değiştirilemez dosyalar
- **Türkçe karakter desteği**: ğüşıöçİĞÜŞÖÇ karakterleri sorunsuz kullanım

### 🔍 Gelişmiş Dosya Tarama

- **Otomatik tarama**: USB sürücüdeki tüm gizli ve sistem dosyalarını bulun
- **İçerik önizleme**: Metin dosyalarının içeriğini doğrudan görüntüleyin
- **Binary dosya tespiti**: Binary ve metin dosyalarını akıllıca ayırt edin
- **Gerçek zamanlı ilerleme**: Tarama sırasında anlık sonuçlar ve istatistikler
- **Durdurma özelliği**: İstediğiniz zaman taramayı duraklatın
- **Detaylı rapor**: Her dosya için boyut, tarih ve öznitelik bilgisi

### 💾 USB Sürücü Yönetimi

- **Otomatik algılama**: Takılan USB flash sürücüleri anında tespit
- **Volume etiket gösterimi**: USB sürücü adlarını görüntüleme
- **Detaylı bilgi**: Her sürücü için:
  - 💿 Toplam kapasite
  - 📊 Kullanılan alan
  - 📈 Boş alan
  - 📁 Dosya sistemi (FAT32, NTFS, exFAT)
- **Çoklu sürücü desteği**: Birden fazla USB sürücüyle aynı anda çalışma
- **Yenileme**: Sürücü listesini manuel olarak güncelleme

### 🗑️ Gelişmiş Dosya İşlemleri

- **Güvenli silme**: 
  - Dosya özniteliklerini otomatik kaldırma
  - Onay penceresi ile güvenli silme
  - Silme işlemi öncesi uyarı
- **Dosya özellikleri görüntüleme**:
  - Dosya adı ve konumu
  - Boyut bilgisi (B, KB, MB)
  - Oluşturulma ve değiştirilme tarihi
  - Gizli/Sistem/Salt okunur durumu
- **USB'ler arası kopyalama**:
  - Dosyaları farklı USB sürücülere kopyalama
  - Üzerine yazma kontrolü
  - İlerleme göstergesi
- **Rapor kaydetme**: 
  - Tarama sonuçlarını TXT dosyası olarak kaydetme
  - Tarih damgalı otomatik adlandırma
  - Tam dosya yolu ve öznitelik bilgisi

### 🎨 Modern ve Kullanışlı Arayüz

- **Koyu tema**: Göz yormayan profesyonel karanlık tema
- **Renkli çıktı**: Farklı mesaj türleri için renk kodlaması:
  - 🔵 Mavi: Bilgi mesajları
  - 🟡 Sarı: Bulunan dosyalar
  - 🟢 Yeşil: Başarılı işlemler
  - 🔴 Kırmızı: Hatalar
  - 🟠 Turuncu: Uyarılar
- **Sekmeli yapı**: Dosya oluştur / Gizli dosya tara sekmeleri
- **Durum çubuğu**: Anlık işlem durumu ve bildirimler
- **Responsive tasarım**: Farklı ekran boyutlarına uyumlu
- **İkon desteği**: Profesyonel uygulama ikonu

### 🔐 Güvenlik Özellikleri

- **Yönetici yetki kontrolü**: Sistem işlemleri için güvenli yetkilendirme
- **Onay mekanizmaları**: Kritik işlemler için kullanıcı onayı
- **Güvenli dosya silme**: Öznitelikleri kaldırarak tam silme
- **İzolasyon**: Sadece seçili sürücüde işlem yapma

---

## 🚀 Kurulum

### Sistem Gereksinimleri

- **İşletim Sistemi**: Windows 7, 8, 10, 11 (32-bit veya 64-bit)
- **Python**: 3.8, 3.9, 3.10, 3.11, 3.12 veya 3.13
- **RAM**: Minimum 512 MB (1 GB önerilir)
- **Disk Alanı**: ~15 MB
- **İzinler**: Yönetici (Administrator) yetkileri (tam işlevsellik için)

### Bağımlılıklar

Proje sadece **1 harici kütüphane** kullanır:

```
psutil>=5.9.0
```

### Kurulum Adımları

#### Yöntem 1: Manuel Kurulum (Önerilen)

1. **Projeyi indirin**:
   ```bash
   git clone https://github.com/yourusername/USBManager.git
   cd USBManager
   ```

2. **Bağımlılıkları yükleyin**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Uygulamayı başlatın**:
   ```bash
   cd src
   python USBManager.py
   ```

#### Yöntem 2: Batch Script ile (Kolay)

Windows üzerinde:
```
cd src
baslat.bat
```

Batch scripti otomatik olarak:
- ✅ Bağımlılıkları kontrol eder
- ✅ Eksik paketleri yükler
- ✅ Uygulamayı başlatır

#### Yöntem 3: Paket Olarak Kurulum

Geliştirme modu kurulumu:
```bash
pip install -e .
```

---

## 🎯 Hızlı Başlangıç

### 1️⃣ Dosya Oluşturma (İlk Adımlar)

```
ADIM 1: USB sürücünüzü takın
ADIM 2: Uygulamayı başlatın (baslat.bat veya python USBManager.py)
ADIM 3: Üst menüden USB sürücünüzü seçin
ADIM 4: "📝 Dosya Oluştur" sekmesine gidin
ADIM 5: Dosya adını girin (örn: secret.dat)
ADIM 6: İçeriğinizi yazın
ADIM 7: Özellikleri seçin: ✓ Gizli ✓ Sistem ✓ Salt okunur
ADIM 8: "✅ Dosyayı Oluştur" butonuna tıklayın
```

**Başarı Mesajı**:
```
✅ Dosya başarıyla oluşturuldu!
📁 Konum: E:\secret.dat
📝 Boyut: 128 karakter
```

### 2️⃣ Gizli Dosya Tarama (İlk Adımlar)

```
ADIM 1: Taranacak USB sürücüyü seçin
ADIM 2: "🔍 Gizli Dosya Tara" sekmesine gidin
ADIM 3: "▶️ Taramayı Başlat" butonuna tıklayın
ADIM 4: Sonuçları sağ panelde izleyin
ADIM 5: İsteğe bağlı: "💾 Raporu Kaydet"
```

**Tarama Çıktısı Örneği**:
```
═══════════════════════════════════════
  🔍 GİZLİ DOSYA TARAMASI BAŞLATILDI
═══════════════════════════════════════

📁 [1] E:\a3f9c7b2.dat
   📄 İçerik örneği:
   USB-AUTH-2442C3D3
   
📁 [2] E:\System Volume Information\...
   📦 Binary dosya

✅ Tarama tamamlandı. Toplam 2 gizli dosya bulundu.
```

---

## 📖 Kullanım Kılavuzu

### 🖥️ Arayüz Düzeni

```
┌──────────────────────────────────────────────────────────────┐
│           🔧 USB Flash Sürücü Yönetim Merkezi                │
├─────────────────────┬────────────────────────────────────────┤
│                     │                                        │
│  📌 SOL PANEL       │  📋 SAĞ PANEL                          │
│                     │                                        │
│  ┌─ Sürücü Seçimi  │  ┌─ Bulunan Dosyalar                   │
│  │  ▼ E:\ (16 GB)  │  │  Tarama Sonuçları                   │
│  │  🔄 Yenile      │  │  Dosya Listesi                      │
│  └─────────────── │  └──────────────────────────            │
│                     │                                        │
│  ┌─ Sekmeler       │  ┌─ Dosya İşlemleri                    │
│  │  📝 Dosya Oluştur│ │  🗑️ Seçili Dosyayı Sil              │
│  │  🔍 Gizli Tara   │  │  👁️ Dosya Özellikleri               │
│  └─────────────── │  │  📋 USB'ye Kopyala                  │
│                     │  │  💾 Raporu Kaydet                   │
│                     │  └──────────────────────────            │
└─────────────────────┴────────────────────────────────────────┘
│  ✅ Durum: Hazır - Son işlem: Başarılı                        │
└──────────────────────────────────────────────────────────────┘
```

### 📝 Dosya Oluşturma - Detaylı Rehber

#### Temel Kullanım

1. **Sürücü Seçimi**
   - Üst bölümden USB sürücünüzü seçin
   - Sürücü bilgileri otomatik görüntülenir:
     ```
     💾 Boş: 14.52 GB | Kullanılan: 1.48 GB | Dolu: %9.2
     ```
   - Sürücü görünmüyorsa "🔄 Yenile" butonuna basın

2. **Dosya Adı Belirleme**
   - Dosya adı alanına istediğiniz adı yazın
   - Varsayılan: `a3f9c7b2.dat`
   - Örnek adlar:
     - `license.key`
     - `auth-token.dat`
     - `secret-notes.txt`
     - `config.ini`

3. **İçerik Yazma**
   - Çok satırlı metin kutusuna içeriğinizi yazın
   - Türkçe karakterler desteklenir
   - Maksimum dosya boyutu sınırı yok
   
   **İçerik Örnekleri**:
   
   ```
   Örnek 1 - Basit Token:
   USB-AUTH-2442C3D3
   
   Örnek 2 - Lisans Bilgisi:
   PRODUCT-KEY: XXXX-XXXX-XXXX-XXXX
   LICENSED-TO: Burak
   EXPIRY-DATE: 2026-12-31
   ACTIVATION: ACTIVE
   
   Örnek 3 - Notlar:
   Önemli Toplantı Notları
   =======================
   
   Tarih: 25 Ekim 2025
   Yer: Konferans Salonu
   
   Gündem:
   1. Proje durumu
   2. Gelecek planlar
   3. Bütçe görüşmesi
   ```

4. **Dosya Öznitelikleri**
   
   - ☑️ **Dosyayı gizle**: 
     - Windows Explorer'da dosya görünmez
     - "Gizli öğeleri göster" seçeneği açıksa görünür
     - Güvenlik ve gizlilik için önerilir
   
   - ☑️ **Sistem dosyası yap**:
     - Dosya sistem dosyası olarak işaretlenir
     - Ek koruma katmanı
     - Yanlışlıkla silinmeyi önler
   
   - ☑️ **Salt okunur**:
     - Dosya sadece okunabilir
     - Değiştirilemez, güncellenemez
     - Veri bütünlüğü için önerilir

5. **Oluşturma**
   - "✅ Dosyayı Oluştur" butonuna tıklayın
   - Başarı mesajını bekleyin
   - Hata durumunda sorun giderme bölümüne bakın

### 🔍 Gizli Dosya Tarama - Detaylı Rehber

#### Tarama Süreci

1. **Hazırlık**
   - Taranacak USB sürücüyü takın
   - Sürücüyü üst menüden seçin
   - "🔍 Gizli Dosya Tara" sekmesine geçin

2. **Taramayı Başlatma**
   - "▶️ Taramayı Başlat" butonuna tıklayın
   - Tarama otomatik olarak başlar
   - Durum çubuğu güncellenir:
     ```
     🔍 E:\ taranıyor...
     ```

3. **Sonuçları İzleme**
   - Bulunan dosyalar gerçek zamanlı olarak listelenir
   - Her dosya için gösterilen bilgiler:
     - 📁 Dosya yolu
     - 📄 İçerik önizlemesi (metin dosyaları için)
     - 📦 Binary/Metin durumu
     - 💾 Dosya boyutu

4. **Tarama Kontrolü**
   - **Durdurma**: "⏹️ Durdur" butonu ile istediğiniz zaman durdurun
   - **Temizleme**: "🧹 Temizle" ile çıktıyı temizleyin
   - **Filtreleme**: Üst taraftaki filtre alanını kullanın

#### Renk Kodlaması

Tarama çıktısında farklı mesaj türleri renklendirilerek gösterilir:

- 🔵 **Mavi (Bilgi)**: Genel bilgi mesajları
  ```
  🔍 Tarama başlatıldı: E:\
  ```

- 🟡 **Sarı (Bulunan Dosya)**: Tespit edilen gizli dosyalar
  ```
  📁 [1] E:\secret.dat
  ```

- 🟢 **Yeşil (Başarı)**: Tamamlanan işlemler
  ```
  ✅ Tarama tamamlandı. 5 dosya bulundu.
  ```

- 🔴 **Kırmızı (Hata)**: Hatalar ve sorunlar
  ```
  ❌ Hata: Erişim reddedildi
  ```

- 🟠 **Turuncu (Uyarı)**: Uyarı mesajları
  ```
  ⚠️ Okunamadı: İzin hatası
  ```

### 🗑️ Dosya Silme İşlemleri

#### Güvenli Silme Adımları

1. **Dosya Seçimi**
   
   İki yöntemle dosya seçebilirsiniz:
   
   **Yöntem 1: Combobox'tan seçim**
   - Sağ paneldeki "Dosya Seçimi" açılır menüsünü kullanın
   - Listeden silmek istediğiniz dosyayı seçin
   ```
   [1] secret.dat - E:\secret.dat
   [2] config.ini - E:\config.ini
   ```
   
   **Yöntem 2: Çıktı alanından seçim**
   - Tarama sonuçlarında dosya yolunu fareyle seçin
   - Seçili metin mavi ile vurgulanır

2. **Silme Komutu**
   - "🗑️ Seçili Dosyayı Sil" butonuna tıklayın
   - Onay penceresi açılır

3. **Onay**
   ```
   ⚠️ Bu dosyayı kalıcı olarak silmek istediğinizden emin misiniz?
   
   📁 E:\secret.dat
   
   Bu işlem geri alınamaz!
   
   [Hayır]  [Evet]
   ```
   - "Evet" → Dosya silinir
   - "Hayır" → İşlem iptal edilir

4. **Silme İşlemi**
   - Dosya öznitelikleri otomatik kaldırılır
   - Dosya kalıcı olarak silinir
   - Başarı mesajı gösterilir:
   ```
   ✅ Dosya başarıyla silindi:
   E:\secret.dat
   ```

⚠️ **ÖNEMLİ UYARILAR**:
- Silme işlemi GERİ ALINAMAZ
- Dosya Geri Dönüşüm Kutusu'na GİTMEZ
- Önemli dosyaları silmeden önce YEDEK alın
- Yanlış dosyayı silmemeye DİKKAT edin

### 👁️ Dosya Özellikleri Görüntüleme

1. **Dosya Seçimi**
   - Combobox veya çıktı alanından dosya seçin

2. **Özellikleri Göster**
   - "👁️ Dosya Özelliklerini Göster" butonuna tıklayın

3. **Görüntülenen Bilgiler**
   ```
   📁 Dosya Özellikleri
   ==================================================
   
   📄 Dosya: a3f9c7b2.dat
   📂 Konum: E:\
   💾 Boyut: 128 B (0.12 KB)
   
   🔒 Gizli: Evet
   ⚙️ Sistem Dosyası: Evet  
   📖 Salt Okunur: Evet
   
   📅 Oluşturulma: 2025-10-21 14:30:15
   📅 Değiştirilme: 2025-10-21 14:30:15
   📅 Son Erişim: 2025-10-21 15:45:22
   ```

### 📋 USB'ye Kopyalama

1. **Kaynak Dosya Seçimi**
   - Kopyalanacak dosyayı seçin

2. **Kopyalama Komutu**
   - "📋 USB'ye Kopyala" butonuna tıklayın
   - Hedef sürücü seçim penceresi açılır

3. **Hedef Sürücü Seçimi**
   ```
   📋 Dosyayı kopyalamak için hedef USB sürücüyü seçin:
   
   Kaynak: secret.dat
   
   Hedef Sürücüler:
   ○ E:\ - USB DISK (14.52 GB)
   ○ F:\ - BACKUP (32.00 GB)
   ○ G:\ - DATA (8.00 GB)
   
   [✅ Kopyala]  [❌ İptal]
   ```

4. **Üzerine Yazma Kontrolü**
   - Aynı isimde dosya varsa:
   ```
   ⚠️ Hedef konumda aynı isimde dosya var:
   F:\secret.dat
   
   Üzerine yazmak istiyor musunuz?
   
   [Hayır]  [Evet]
   ```

5. **Kopyalama**
   - İlerleme gösterilir
   - Başarı mesajı:
   ```
   ✅ Dosya başarıyla kopyalandı!
   
   📁 Kaynak: E:\secret.dat
   📁 Hedef: F:\secret.dat
   ```

### 💾 Rapor Kaydetme

1. **Tarama Yapın**
   - Önce bir gizli dosya taraması yapın
   - Sonuçların çıktı alanında göründüğünden emin olun

2. **Rapor Kaydet**
   - "💾 Raporu Kaydet" butonuna tıklayın
   - Dosya kaydetme penceresi açılır

3. **Konum ve İsim Belirleme**
   - Kaydetmek istediğiniz klasörü seçin
   - Dosya adı girin (Varsayılan: `usb_tarama_raporu.txt`)
   - Örnek: `C:\Users\Burak\Desktop\usb_tarama_raporu_2025-10-21.txt`

4. **Kaydetme**
   - "Kaydet" butonuna tıklayın
   - Başarı mesajı:
   ```
   ✅ Rapor kaydedildi:
   C:\Users\Burak\Desktop\usb_tarama_raporu.txt
   ```

**Rapor İçeriği Örneği**:
```
═══════════════════════════════════════
  🔍 GİZLİ DOSYA TARAMASI RAPORU
═══════════════════════════════════════

Tarih: 2025-10-21 15:45:00
Sürücü: E:\ - USB DISK

📁 [1] E:\a3f9c7b2.dat
   📄 İçerik örneği:
   USB-AUTH-2442C3D3
   
📁 [2] E:\secret.txt
   📄 İçerik örneği:
   Gizli notlar...

✅ Tarama tamamlandı. Toplam 2 gizli dosya bulundu.
```

---

## 📁 Proje Yapısı

### Güncel Dosya Hiyerarşisi

```
USBManager/
├── src/                          # 📂 Kaynak kod dosyaları
│   ├── USBManager.py             # 🖥️ Ana GUI uygulaması (31 KB)
│   │                             #    ✅ Modern, tam özellikli
│   │                             #    ✅ Telif hakkı korumalı
│   │                             #    ✅ ÖNERİLİR
│   ├── Secretfilescreator.py     # 📝 Legacy CLI dosya oluşturucu (2.5 KB)
│   │                             #    Geriye dönük uyumluluk için
│   ├── flashreader.py            # 🔍 Legacy CLI tarama aracı (8 KB)
│   │                             #    Temel tarama işlevselliği
│   ├── baslat.bat                # 🚀 Windows başlatma scripti (0.5 KB)
│   │                             #    Otomatik bağımlılık kontrolü
│   └── __init__.py               # 📦 Python paketi tanımı (0.6 KB)
│                                 #    Versiyon ve yazar bilgisi
├── assets/                       # 🎨 Statik varlıklar
│   └── tool.ico                  # 🔧 Uygulama ikonu (66.1 KB)
│                                 #    512x512 çözünürlük
├── requirements.txt              # 📋 Python bağımlılıkları (0.01 KB)
│                                 #    Sadece: psutil>=5.9.0
├── setup.py                      # ⚙️ Paket kurulum scripti (2.1 KB)
│                                 #    PyPI uyumlu yapılandırma
├── COPYRIGHT                     # ©️ Telif hakkı bildirimi (0.3 KB)
│                                 #    Yasal koruma metni
├── LICENSE                       # 📜 Proprietary License (1.5 KB)
│                                 #    Tüm haklar saklı
├── .gitignore                   # 🚫 Git ignore kuralları (0.4 KB)
│                                 #    Build ve cache dosyaları
└── README.md                     # 📖 Bu dokümantasyon dosyası
                                  #    Kapsamlı kullanım kılavuzu
```

### Dosya Rolleri ve Açıklamaları

#### 🖥️ Ana Uygulama - `USBManager.py`

**Önerilen ve tam özellikli GUI uygulaması**

✅ **Özellikler**:
- Modern tkinter tabanlı arayüz
- Çift sekmeli yapı (Dosya Oluştur / Gizli Tara)
- Gerçek zamanlı tarama ile asenkron işlem
- Dosya combobox seçimi
- USB'ye kopyalama özelliği
- Detaylı dosya özellikleri gösterimi
- Rapor kaydetme
- Renkli çıktı sistemi
- Volume etiket desteği
- Durum çubuğu

**Kullanım**:
```bash
cd src
python USBManager.py
```

#### 📝 Legacy Tool - `Secretfilescreator.py`

**Basit CLI tabanlı dosya oluşturucu**

✅ **Özellikler**:
- Komut satırı arayüzü
- Temel dosya oluşturma
- Dosya özniteliği ayarlama
- Tek satır token desteği

**Kullanım**:
```bash
python Secretfilescreator.py
```

**Ne zaman kullanılır**:
- Otomasyon scriptlerinde
- Batch işlemlerinde
- GUI gerektirmeyen senaryolarda

#### 🔍 Legacy Tool - `flashreader.py`

**Basit CLI tabanlı tarama aracı**

✅ **Özellikler**:
- Komut satırı tarama
- Gizli dosya tespiti
- İçerik önizleme
- Rapor kaydetme

**Kullanım**:
```bash
python flashreader.py
```

**Ne zaman kullanılır**:
- Hızlı komut satırı taraması
- Sunucu ortamlarında
- Otomasyon görevlerinde

#### 🚀 Başlatma Script - `baslat.bat`

**Otomatik kurulum ve başlatma**

✅ **Özellikler**:
- Python kurulum kontrolü
- psutil yükleme kontrolü
- Otomatik bağımlılık yükleme
- Hata yakalama ve kullanıcı bilgilendirme
- USBManager.py'yi otomatik başlatma

**İçerik**:
```
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
```

**Kullanım**:
- Çift tıklama ile başlatma
- Yeni kullanıcılar için kolay kurulum

---

## 🛠️ Teknik Detaylar

### Kullanılan Teknolojiler ve Kütüphaneler

#### Python Standart Kütüphaneleri

- **os**: Dosya ve dizin işlemleri
- **threading**: Asenkron tarama işlemleri
- **tkinter**: GUI framework
  - `ttk`: Themed widgets
  - `scrolledtext`: Kaydırmalı metin alanı
  - `messagebox`: Dialog pencereleri
  - `filedialog`: Dosya seçim diyalogları
- **subprocess**: Windows komut çalıştırma
- **shutil**: Dosya kopyalama işlemleri
- **ctypes**: Windows API erişimi
  - `wintypes`: Windows veri tipleri

#### Harici Kütüphaneler

- **psutil** (>=5.9.0)
  - Disk bölümlerini listeleme
  - Disk kullanım istatistikleri
  - Çıkarılabilir disk tespiti
  - Cross-platform disk yönetimi

### Windows API Fonksiyonları

#### 1. GetVolumeInformationW

**Amaç**: USB sürücü etiket bilgisini alma

```python
kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
GetVolumeInformationW = kernel32.GetVolumeInformationW
GetVolumeInformationW.argtypes = [
    wintypes.LPCWSTR,  # lpRootPathName
    wintypes.LPWSTR,   # lpVolumeNameBuffer
    wintypes.DWORD,    # nVolumeNameSize
    wintypes.LPDWORD,  # lpVolumeSerialNumber
    wintypes.LPDWORD,  # lpMaximumComponentLength
    wintypes.LPDWORD,  # lpFileSystemFlags
    wintypes.LPWSTR,   # lpFileSystemNameBuffer
    wintypes.DWORD     # nFileSystemNameSize
]
```

**Kullanım**:
- Volume adı (etiket) okuma
- Seri numarası alma
- Dosya sistemi bilgisi

#### 2. GetFileAttributesW

**Amaç**: Dosya özniteliklerini okuma

```python
GetFileAttributesW = kernel32.GetFileAttributesW
GetFileAttributesW.argtypes = [wintypes.LPCWSTR]
GetFileAttributesW.restype = wintypes.DWORD
```

**Kullanım**:
- Gizli dosya tespiti
- Sistem dosyası kontrolü
- Öznitelik bilgisi okuma

#### 3. SetFileAttributesW

**Amaç**: Dosya özniteliklerini değiştirme

**Kullanım**:
- Dosyayı gizli yapma
- Sistem dosyası işaretleme
- Salt okunur ayarlama

**Öznitelik Bayrakları**:
```python
FILE_ATTRIBUTE_HIDDEN = 0x2   # Gizli
FILE_ATTRIBUTE_SYSTEM = 0x4   # Sistem
FILE_ATTRIBUTE_READONLY = 0x1 # Salt okunur
```

### Desteklenen Dosya Sistemleri

| Dosya Sistemi | Destek | Özellikler |
|---------------|--------|------------|
| **FAT32** | ✅ Tam | En yaygın USB format |
| **NTFS** | ✅ Tam | Windows native, gelişmiş özellikler |
| **exFAT** | ✅ Tam | Büyük dosya desteği |
| FAT16 | ⚠️ Kısmi | Eski format, sınırlı |
| Ext4 | ❌ | Linux dosya sistemi |
| HFS+ | ❌ | macOS dosya sistemi |

### Varsayılan Konfigürasyon

`USBManager.py` içindeki varsayılan ayarlar:

```python
# Dosya Oluşturma Varsayılanları
DEFAULT_FILENAME = "a3f9c7b2.dat"
DEFAULT_TOKEN = "USB-AUTH-2442C3D3"

# Tarama Ayarları
MAX_READ_BYTES = 4096  # Dosya önizleme için maksimum byte

# Dosya Öznitelikleri
FILE_ATTRIBUTE_HIDDEN = 0x2
FILE_ATTRIBUTE_SYSTEM = 0x4

# GUI Renkleri
colors = {
    'bg': '#f0f0f0',
    'primary': '#2196F3',
    'success': '#4CAF50',
    'danger': '#f44336',
    'warning': '#FF9800',
    'dark': '#212121',
    'light': '#ffffff'
}
```

### Threading ve Asenkron İşlemler

**Neden Threading?**
- GUI donmasını önleme
- Gerçek zamanlı çıktı gösterimi
- Kullanıcı etkileşimini sürdürme
- Tarama işlemini durdurabilme

**Kullanım**:
```python
self._scan_thread = threading.Thread(
    target=self._scan_worker, 
    args=(root_path,), 
    daemon=True
)
self._scan_thread.start()
```

**Durdurma Mekanizması**:
```
self._stop_event = threading.Event()
# Taramayı durdur
self._stop_event.set()
```

### Güvenlik Özellikleri

1. **Yönetici Yetki Kontrolü**
   - Sistem dosyası işlemleri için gerekli
   - Kullanıcı bilgilendirmesi

2. **Onay Mekanizmaları**
   - Dosya silme onayı
   - Üzerine yazma onayı
   - Tehlikeli işlem uyarıları

3. **Veri Doğrulama**
   - Dosya varlık kontrolü
   - Yol doğrulama
   - UTF-8 encoding kontrolü

---

## 🆘 Sorun Giderme

### Sık Karşılaşılan Sorunlar ve Çözümleri

#### Sorun 1: "Hiçbir USB sürücü bulunamadı"

**Belirti**:
```
❌ Hiçbir USB sürücü bulunamadı
```

**Olası Nedenler**:
- USB sürücü düzgün takılmamış
- Sürücü formatı desteklenmiyor
- Sürücü bozuk veya tanınmıyor
- Windows sürücü sorunu

**Çözümler**:

1. **USB'yi yeniden takın**:
   ```
   1. USB'yi çıkarın
   2. 3 saniye bekleyin
   3. USB'yi tekrar takın
   4. Uygulamada "🔄 Yenile" butonuna basın
   ```

2. **Dosya sistemini kontrol edin**:
   - Windows Explorer → Sürücüye sağ tık → Özellikler
   - Dosya sistemi FAT32, NTFS veya exFAT olmalı
   - Değilse formatlamayı düşünün (veri kaybı olur!)

3. **Disk Yönetimi'nden kontrol**:
   ```
   Windows + X → Disk Yönetimi
   USB sürücünün "Sağlıklı" durumda olduğunu kontrol edin
   ```

4. **Başka bir USB portu deneyin**:
   - USB 2.0 ve USB 3.0 portlarını deneyin
   - Hub kullanıyorsanız direkt PC'ye takın

#### Sorun 2: "Dosya oluşturulamadı"

**Belirti**:
```
❌ Dosya oluşturulamadı:
[WinError 5] Access is denied
```

**Olası Nedenler**:
- Yazma koruması aktif
- Yeterli izin yok
- Disk dolu
- Dosya adı geçersiz

**Çözümler**:

1. **Yazma korumasını kontrol edin**:
   ```
   - USB'de fiziksel yazma koruma anahtarı olabilir
   - Anahtarı "açık" konuma getirin
   ```

2. **Yönetici olarak çalıştırın**:
   ```
   baslat.bat üzerine sağ tık
   → "Yönetici olarak çalıştır"
   ```

3. **Disk alanını kontrol edin**:
   ```
   USB özelliklere bakın:
   Boş: XX GB göründüğünden emin olun
   ```

4. **Dosya adını kontrol edin**:
   ```
   Geçersiz karakterler: < > : " / \ | ? *
   Geçerli örnek: secret.dat
   Geçersiz örnek: secret?.dat
   ```

5. **Antivirüs yazılımını kontrol edin**:
   ```
   Geçici olarak devre dışı bırakın
   USB Manager'ı beyaz listeye ekleyin
   ```

#### Sorun 3: "Dosya silinemedi"

**Belirti**:
```
❌ Dosya silinemedi:
[WinError 32] The process cannot access the file
```

**Olası Nedenler**:
- Dosya başka programda açık
- Sistem dosyası koruması
- İzin sorunu

**Çözümler**:

1. **Dosyayı kullanan programları kapatın**:
   ```
   Ctrl + Shift + Esc → Görev Yöneticisi
   Şüpheli işlemleri sonlandırın
   ```

2. **Yönetici yetkileriyle çalıştırın**:
   ```
   Uygulamayı kapat
   baslat.bat → Sağ tık → Yönetici olarak çalıştır
   ```

3. **Dosya özniteliklerini manuel kaldırın**:
   ```cmd
   cmd → Yönetici olarak çalıştır
   attrib -h -s -r "E:\dosya.dat"
   del "E:\dosya.dat"
   ```

4. **USB'yi güvenli çıkar ve tekrar tak**:
   ```
   Sistem tepsisi → USB'yi güvenli çıkar
   USB'yi tekrar tak
   Tekrar deneyin
   ```

#### Sorun 4: Tarama çok yavaş

**Belirti**:
```
🔍 E:\ taranıyor... (5 dakikadır devam ediyor)
```

**Olası Nedenler**:
- Çok fazla dosya var
- Yavaş USB 2.0 sürücü
- Büyük dosyalar
- Parçalanmış disk

**Çözümler**:

1. **Sabırlı olun**:
   ```
   Büyük sürücülerde (32 GB+) tarama uzun sürebilir
   Bu normal bir durumdur
   ```

2. **Taramayı durdurun**:
   ```
   "⏹️ Durdur" butonunu kullanın
   Zaten bulunan dosyalar listede görünür
   ```

3. **Daha küçük sürücü kullanın**:
   ```
   İlk test için 8 GB veya daha küçük sürücü deneyin
   ```

4. **USB 3.0 kullanın**:
   ```
   USB 3.0 portlar (mavi renk) daha hızlıdır
   USB 3.0 sürücü kullanın
   ```

#### Sorun 5: "import psutil" hatası

**Belirti**:
```
ModuleNotFoundError: No module named 'psutil'
```

**Çözüm**:

1. **Manuel yükleme**:
   ```bash
   pip install psutil
   ```

2. **Requirements ile yükleme**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Python versiyonunu kontrol**:
   ```bash
   python --version
   # 3.8 veya üzeri olmalı
   ```

4. **pip güncellemesi**:
   ```bash
   python -m pip install --upgrade pip
   pip install psutil
   ```

#### Sorun 6: İkon görünmüyor

**Belirti**:
- Pencere ikonu varsayılan Python ikonu

**Çözüm**:

1. **İkon dosyasını kontrol edin**:
   ```
   assets/tool.ico dosyasının var olduğundan emin olun
   ```

2. **Yol kontrolü**:
   ```python
   # USBManager.py içinde
   icon_path = os.path.join(
       os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 
       "assets", 
       "tool.ico"
   )
   ```

3. **İkon yeniden yükleyin**:
   ```
   Uygulamayı kapatıp yeniden başlatın
   ```

#### Sorun 7: Türkçe karakterler bozuk

**Belirti**:
- ğüşıöçİĞÜŞÖÇ → ����

**Çözüm**:

1. **Encoding ayarını kontrol edin**:
   ```python
   # UTF-8 encoding kullanıldığından emin olun
   with open(filepath, "w", encoding="utf-8") as f:
   ```

2. **Windows kod sayfası**:
   ```cmd
   chcp 65001
   ```

3. **Metin editörü ayarları**:
   ```
   Notepad++, VS Code gibi editörlerde
   Encoding → UTF-8 (BOM'suz)
   ```

---

## 🎓 Kullanım Senaryoları

### Senaryo 1: Güvenlik Token Oluşturma

**Amaç**: USB sürücüde gizli kimlik doğrulama token'ı oluşturun

**Adımlar**:
```
1. USB sürücünü takın
2. USBManager'ı başlatın
3. Sürücüyü seçin (örn: E:\)
4. "📝 Dosya Oluştur" sekmesine geçin
5. Dosya adı: auth-token.dat
7. İçerik:
   TOKEN: 7f9c2b4e-auth-2025-uuid
   USER: Burak
   EXPIRY: 2026-12-31
   LEVEL: ADMIN
7. Seçenekler:
   ✅ Dosyayı gizle
   ✅ Sistem dosyası yap
   ✅ Salt okunur
8. "✅ Dosyayı Oluştur" tıklayın
```

**Sonuç**: Gizli, değiştirilemez güvenlik token'ı oluşturuldu.

### Senaryo 2: USB Güvenlik Taraması

**Amaç**: Şüpheli gizli dosyaları tespit edin

```
1. Bilinmeyen USB'yi takın
2. "🔍 Gizli Dosya Tara" sekmesine geçin
3. "▶️ Taramayı Başlat"
4. Bulunan dosyaları inceleyin
5. Şüpheli dosyaları:
   - "👁️ Dosya Özellikleri" ile kontrol edin
   - Gerekirse "🗑️ Sil"
6. "💾 Raporu Kaydet" - Kanıt için
```

### Senaryo 3: Gizli Not Defteri

**Dosya**: `notes.txt`
**İçerik**:
```
Gizli Toplantı Notları
======================

Tarih: 25 Ekim 2025
Katılımcılar: A, B, C

Gündem:
1. Proje X durumu
2. Bütçe planlaması
3. Gelecek adımlar

Kararlar:
- Proje onaylandı
- Ek bütçe tahsis edildi
```
**Ayarlar**: ✅ Gizli, ❌ Sistem, ❌ Salt okunur

---

## 📊 Özellik Karşılaştırması

### Legacy vs Modern

| Özellik | Secretfilescreator.py | flashreader.py | USBManager.py |
|---------|---------------------|----------------|---------------|
| **Dosya oluşturma** | ✅ Temel | ❌ | ✅ Gelişmiş |
| **Çok satırlı metin** | ❌ | ❌ | ✅ |
| **Gizli dosya tarama** | ❌ | ✅ Temel | ✅ Gelişmiş |
| **İçerik önizleme** | ❌ | ✅ | ✅ |
| **Dosya silme** | ❌ | ✅ | ✅ Güvenli |
| **USB bilgisi** | ✅ Basit | ✅ Basit | ✅ Detaylı |
| **Modern GUI** | ❌ CLI | ❌ CLI | ✅ |
| **Renkli çıktı** | ❌ | ❌ | ✅ |
| **Sekmeli arayüz** | ❌ | ❌ | ✅ |
| **Dosya özellikleri** | ❌ | ❌ | ✅ |
| **Rapor kaydetme** | ❌ | ✅ | ✅ Gelişmiş |
| **USB'ye kopyalama** | ❌ | ❌ | ✅ |
| **Dosya seçimi** | ❌ | ❌ | ✅ Combobox |
| **Volume etiket** | ❌ | ❌ | ✅ |
| **Asenkron tarama** | ❌ | ❌ | ✅ |
| **Durdurma özelliği** | ❌ | ❌ | ✅ |
| **Durum çubuğu** | ❌ | ❌ | ✅ |
| **İkon desteği** | ❌ | ❌ | ✅ |

**Sonuç**: USBManager.py tüm özellikleri tek uygulamada birleştirir ve modern GUI ile kullanım kolaylığı sağlar.

---

## ©️ Telif Hakkı ve Lisans

### Copyright

**Copyright (c) 2025 Burak. All rights reserved.**

Bu yazılım ve kaynak kodları **tüm hakları saklıdır**. Yazılımın kopyalanması, dağıtılması, gösterilmesi, değiştirilmesi veya herhangi bir şekilde kullanılması yazarın açık yazılı izni olmaksızın **yasaktır**.

This software is **proprietary** and confidential. Unauthorized copying, distribution, modification, or use of this software is strictly **prohibited** without explicit written permission from the author.

### Kullanım Koşulları

#### ✅ İzin Verilen

- **Kişisel kullanım** (Personal use only)
  - Kendi USB sürücülerinizde kullanım
  - Öğrenme ve eğitim amaçlı inceleme
  - Kişisel veri yönetimi

#### ❌ Yasak Olan

- **Ticari kullanım** (Commercial use prohibited)
- **Dağıtım** (Distribution prohibited)
- **Değiştirme** (Modification prohibited)
- **Tersine Mühendislik** (Reverse engineering prohibited)

### Yasal Uyarı

İzinsiz kullanım, kopyalama, dağıtım veya değiştirme **yasal işlem gerektirir**.

### Lisans Dosyaları

- **[LICENSE](LICENSE)** - Tam lisans metni
- **[COPYRIGHT](COPYRIGHT)** - Telif hakkı bildirimi

---

## 👨‍💻 Geliştirici

**Yazar** - 2025

Burak TEMUR ve Arda DEMİRHAN

---

## 🙏 Teşekkürler

- Python Software Foundation
- psutil Geliştiricileri
- Windows API Dokümantasyonu
- tkinter Topluluğu

---

## 🚀 Gelecek Özellikler

- [ ] Toplu dosya silme
- [ ] Gelişmiş filtreleme
- [ ] Dosya içeriği düzenleme
- [ ] Şifreleme desteği
- [ ] Çoklu dil desteği
- [ ] Tema özelleştirme

---

## 📞 Destek

Herhangi bir sorun yaşarsanız:
1. Bu README dosyasını okuyun
2. Sorun giderme bölümünü inceleyin
3. Gerekirse geliştirici ile iletişime geçin

---

## 📝 Sürüm Geçmişi

### v1.0.0 (2025-10-21)

- ✅ İlk sürüm yayınlandı
- ✅ Modern GUI eklendi
- ✅ Telif hakkı koruması
- ✅ Kapsamlı dokümantasyon

---

## ⚙️ Sistem Gereksinimleri

- **İşletim Sistemi**: Windows 7/8/10/11
- **Python**: 3.8 veya üzeri
- **RAM**: Minimum 512 MB
- **Disk Alanı**: ~15 MB

---

## 🎉 İyi Kullanımlar!

```
╔══════════════════════════════════════════╗
║  🔧 USB Manager - v1.0.0                 ║
║  Modern USB Yönetim Aracı                ║
║                                          ║
║  Made with ❤️ by Burak                   ║
║  © 2025 - Tüm hakları saklıdır          ║
╚══════════════════════════════════════════╝
```

---

**Son Güncelleme**: 2025-10-21  
**Versiyon**: 1.0.0  
**Lisans**: Proprietary  
**Platform**: Windows

---

> **Not**: Bu uygulama Windows işletim sisteminde çalışmak üzere tasarlanmıştır. Tam işlevsellik için yönetici yetkileri gereklidir.
