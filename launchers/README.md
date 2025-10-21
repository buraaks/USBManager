# 📂 Launchers Klasörü - Kullanım Rehberi

Bu klasör, USB Manager uygulamasını başlatmak için farklı yöntemler içerir.

---

## 🎯 Önerilen Kullanım

### ⭐ En İyi: `baslat_gizli.vbs`

**Konsol olmadan, tamamen gizli başlatma**

```
# Çift tıklama:
baslat_gizli.vbs
```

**Özellikleri:**
- ✅ Konsol penceresi hiç görünmez
- ✅ Direkt GUI açılır
- ✅ Profesyonel görünüm
- ✅ Sessiz başlatma

---

## 📝 Tüm Başlatıcılar

### 1. `baslat_gizli.vbs` ⭐ (ÖNERİLEN)

**VBScript - Tamamen Gizli Başlatma**

- Konsol: ❌ Yok
- GUI: ✅ Var
- Kullanım: Çift tıklama
- Platform: Windows

### 2. `baslat.bat`

**Batch Script - 2 Saniye Konsol**

- Konsol: ⚠️ 2 saniye görünür
- GUI: ✅ Var
- Kullanım: Çift tıklama veya cmd
- Debug: ✅ Mesajlar görünür

### 3. `create_shortcut.ps1`

**PowerShell - Masaüstü Kısayolu Oluşturucu**

```powershell
# PowerShell ile çalıştır:
.\create_shortcut.ps1
```

**Ne Yapar:**
- Masaüstünde "USB Manager" kısayolu oluşturur
- İkon ataması yapar
- pythonw.exe ile çalışacak şekilde ayarlar

### 4. `baslat_src.bat` (Legacy)

**Eski src/ Launcher - Geriye Uyumluluk**

### 5. `baslat_gizli_src.vbs` (Legacy)

**Eski src/ VBScript - Geriye Uyumluluk**

---

## 🔄 Karşılaştırma

| Launcher | Konsol | Hız | Kolay | Önerilen |
|----------|--------|-----|-------|----------|
| `baslat_gizli.vbs` | ❌ | ⚡⚡⚡ | ✅✅✅ | ⭐⭐⭐⭐⭐ |
| `baslat.bat` | ⚠️ 2sn | ⚡⚡ | ✅✅ | ⭐⭐⭐ |
| Kısayol | ❌ | ⚡⚡⚡ | ✅✅✅ | ⭐⭐⭐⭐⭐ |

---

## 🎓 Nasıl Çalışır?

### VBScript Launcher (`baslat_gizli.vbs`)

```vbscript
' 1. Launcher dizinini bul
' 2. Proje kök dizinine git
' 3. src klasörüne geç
' 4. pythonw.exe ile GUI'yi başlat (konsol yok)
' 5. Script sonlanır
```

### Batch Launcher (`baslat.bat`)

```batch
REM 1. Launcher dizininden src'ye git
REM 2. Gereksinimleri kontrol et
REM 3. 2 saniye mesaj göster
REM 4. pythonw.exe ile GUI başlat
REM 5. Batch penceresi kapan
```

---

## 🐛 Sorun Giderme

### VBScript çalışmıyor

```cmd
# Manuel çalıştır:
cscript baslat_gizli.vbs

# Veya tam yol:
"C:\Windows\System32\cscript.exe" baslat_gizli.vbs
```

### pythonw bulunamıyor

```cmd
# Python PATH'e eklenmemiş
# Kontrol:
where pythonw

# Tam yol ile:
"C:\Python310\pythonw.exe" ..\src\USBManager.py
```

---

## 📋 Öneriler

1. **Günlük Kullanım:** `baslat_gizli.vbs`
2. **Masaüstü Erişim:** Önce `create_shortcut.ps1` çalıştır
3. **Debug:** `baslat.bat` (mesajları görebilirsiniz)

---

**Proje:** USB Manager v1.0.0  
**Yazarlar:** Burak TEMUR ve Arda DEMİRHAN  
**Platform:** Windows
