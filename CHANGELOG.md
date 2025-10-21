# 📝 Değişiklik Günlüğü (Changelog)

## [1.0.0] - 2025-10-21

### ✨ Yeni Özellikler

#### 🔒 Güvenlik İyileştirmeleri
- **Input Validation**: Dosya adı ve içerik validasyonu eklendi
  - Geçersiz karakterlerin kontrolü
  - Dosya boyutu limiti (max 10 MB)
  - Windows reserved isimlerin kontrolü
  - Path traversal koruması

- **Admin Yetki Kontrolü**: Başlangıçta yönetici yetkisi kontrolü
  - `is_admin()` fonksiyonu eklendi
  - Kullanıcıya bilgilendirme mesajı gösteriliyor
  - Sınırlı yetki durumunda uyarı

#### 🛠️ Windows API İyileştirmeleri
- **SetFileAttributesW API**: Dosya özniteliklerini doğrudan API ile ayarlama
  - Daha hızlı işlem
  - Daha güvenilir
  - Subprocess fallback mekanizması

#### 📊 Performans Optimizasyonları
- **Batch Tarama**: Dosyalar 100'lük gruplar halinde işleniyor
- **İlerleme Bildirimi**: Her 500 dosyada bir güncelleme
- **Tarama İstatistikleri**:
  - Toplam taranan dosya sayısı
  - Bulunan gizli dosya sayısı
  - Tarama süresi
  - Dosya/saniye hızı

#### 🎨 Kullanıcı Arayüzü Geliştirmeleri
- **Menü Çubuğu**: Dosya ve Yardım menüleri eklendi
- **Klavye Kısayolları**:
  - F5 / Ctrl+R: Sürücüleri yenile
  - Ctrl+S: Taramayı başlat
  - Ctrl+N: Dosya oluştur
  - Esc: Taramayı durdur
  - Delete: Seçili dosyayı sil
  - Ctrl+Q: Çıkış

- **İlerleme Çubuğu**: Tarama ilerlemesini görsel olarak gösterir
  - Indeterminate mode (başlangıç)
  - Progress label ile detaylı bilgi
  - Tamamlanma yüzdesi

- **Hakkında Diyalogu**: Uygulama bilgileri
- **Klavye Kısayolları Diyalogu**: Kısayol listesi

#### 📝 Logging Sistemi
- **Detaylı Loglama**:
  - Tüm işlemler log dosyasına kaydediliyor
  - Günlük bazlı log dosyaları (`logs/usbmanager_YYYYMMDD.log`)
  - Hata, uyarı ve bilgi seviyelerinde loglama
  - Console ve dosyaya eşzamanlı yazma

#### 📚 Dokümantasyon
- **Docstring**: Fonksiyonlara detaylı açıklamalar eklendi
- **Type Hints**: Bazı fonksiyonlara tip belirteçleri
- **README**: Yazar bilgileri güncellendi
- **CHANGELOG**: Bu dosya oluşturuldu

### 🔧 Düzeltmeler

- **setup.py**: README.md yolu düzeltildi (docs/ → kök dizin)
- **LICENSE**: Yazar bilgisi güncellendi (Burak TEMUR ve Arda DEMİRHAN)
- **COPYRIGHT**: Yazar bilgisi güncellendi

### 🗂️ Yapısal İyileştirmeler

- **.gitignore**: Yeni ignore kuralları eklendi
  - logs/
  - backups/
  - coverage dosyaları
  - .whl dosyaları

### 📦 Bağımlılıklar

Yeni modüller:
- `logging`: Loglama sistemi
- `datetime`: Tarih/saat işlemleri
- `time`: Performans ölçümü
- `re`: Regex validasyonu
- `sys`: Sistem bilgisi

### 🐛 Bilinen Sorunlar

- İlerleme çubuğu tarama sırasında gerçek yüzdeyi göstermiyor (indeterminate mode)
- Çok büyük sürücülerde (>100GB) tarama yavaş olabilir

### 🔜 Gelecek Planlar

v1.1.0 için planlanan özellikler:
- Konfigürasyon dosyası desteği
- Çok dilli destek (i18n)
- Unit testler
- Otomatik yedekleme özelliği
- Gelişmiş filtreleme
- Dosya içeriği düzenleme

---

## Versiyon Numaralandırma

Bu proje [Semantic Versioning](https://semver.org/) kullanmaktadır.

- **MAJOR**: Geriye dönük uyumsuz değişiklikler
- **MINOR**: Geriye dönük uyumlu yeni özellikler
- **PATCH**: Geriye dönük uyumlu hata düzeltmeleri

---

**Yazarlar**: Burak TEMUR ve Arda DEMİRHAN  
**Lisans**: Proprietary  
**Platform**: Windows 7/8/10/11
