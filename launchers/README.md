# 🚀 USB Manager - Başlatıcı Klasörü

Bu klasör, USB Manager uygulamasını başlatmak için gerekli dosyaları içerir.

---

## 🎯 Hızlı Başlangıç

### Yöntem 1: Doğrudan Başlat ⭐ (ÖNERİLEN)

**En basit ve hızlı yöntem:**

```
Çift tıklama: baslat.vbs
```

**Özellikleri:**
- ✅ Konsol penceresi hiç görünmez
- ✅ Direkt GUI açılır
- ✅ Profesyonel ve sessiz başlatma
- ✅ Tek adımda çalışır

---

### Yöntem 2: Masaüstü Kısayolu Oluştur

**İlk kurulumda önerilir:**

```cmd
# Çift tıklama:
create_shortcut.bat
```

**Ne Yapar:**
- Masaüstünde "USB Manager" kısayolu oluşturur
- İkon ataması yapar (tool.ico)
- pythonw.exe ile çalışacak şekilde ayarlar
- Konsol olmadan başlatma
- PowerShell execution policy sorunu yok

**Ne Yapar:**
- Masaüstünde "USB Manager" kısayolu oluşturur
- İkon ataması yapar (tool.ico)
- pythonw.exe ile çalışacak şekilde ayarlar
- Konsol olmadan başlatma

---

## 📝 Dosyalar

| Dosya | Açıklama | Kullanım |
|-------|----------|----------|
| `baslat.vbs` | Ana başlatıcı (konsol yok) | Çift tıklama |
| `create_shortcut.bat` | Masaüstü kısayolu oluşturucu | Çift tıklama |
| `README.md` | Bu dosya | Dokümantasyon |

---

## 🎯 Nasıl Çalışır?

### `baslat.vbs` - VBScript Başlatıcı

```vbscript
' 1. Ana proje dizinini otomatik bulur
' 2. src/ klasörüne gider
' 3. pythonw.exe ile GUI'yi başlatır (konsol yok)
' 4. WindowStyle=0 (gizli pencere)
' 5. Script sonlanır
```

### `create_shortcut.bat` - Kısayol Oluşturucu

```batch
# 1. PowerShell komutlarını inline çalıştırır
# 2. Masaüstü yolunu bulur
# 3. "USB Manager.lnk" kısayolu oluşturur
# 4. pythonw.exe hedef olarak ayarlar
# 5. Çalışma dizinini src/ yapar
# 6. tool.ico ikonunu atar
# 7. Kısayolu kaydeder
# 8. ExecutionPolicy bypass otomatik
```

---

## 🐛 Sorun Giderme

### VBScript çalışmıyor

```cmd
# Manuel çalıştır:
cscript baslat.vbs

# Veya tam yol:
"C:\Windows\System32\cscript.exe" baslat.vbs
```

### pythonw bulunamıyor

```cmd
# Python PATH'e eklenmemiş
# Kontrol:
where pythonw

# Eğer bulunamazsa Python'u yeniden yükle ve "Add to PATH" seçeneğini işaretle
```

---

## 🔧 Teknik Detaylar

### pythonw.exe vs python.exe

```
python.exe   → Konsol penceresi açar (CLI uygulamalar için)
pythonw.exe  → Konsol yok (GUI uygulamalar için) ✅
```

### VBScript Run Parametreleri

```vbscript
WshShell.Run "komut", WindowStyle, WaitOnReturn

WindowStyle:
  0 = Gizli pencere     ✅ (USB Manager kullanıyor)
  1 = Normal pencere
  2 = Minimize
  3 = Maximize

WaitOnReturn:
  True  = Komut bitene kadar bekle
  False = Beklemeden devam et  ✅
```

---

## 📚 Öneriler

1. **Günlük Kullanım:** `baslat.vbs` - Çift tıklama
2. **İlk Kurulum:** `create_shortcut.bat` - Masaüstü kısayolu oluştur
3. **Paylaşım:** `baslat.vbs` dosyasını önerin (en basit)

---

**Proje:** USB Manager v1.0.0  
**Yazarlar:** Burak TEMUR ve Arda DEMİRHAN  
**Platform:** Windows
