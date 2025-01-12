### **README.md**
```markdown
# Kullanıcı Yönetim Sistemi

Bu proje, kullanıcıların kaydolabileceği, giriş yapabileceği, çıkış yapabileceği ve mevcut kullanıcı bilgilerini görüntüleyebileceği bir **kullanıcı yönetim sistemi** sunar. Proje, kullanıcı bilgilerini bir JSON dosyasında saklar ve Python'un **OOP** (Nesne Yönelimli Programlama) özelliklerini kullanır.

---

## 🚀 Özellikler

- **Kullanıcı Kaydı (Register):**
  - Yeni kullanıcılar sisteme kaydedilebilir.
  - Kullanıcı bilgileri (kullanıcı adı, şifre, e-posta) JSON dosyasına kaydedilir.

- **Giriş Yapma (Login):**
  - Kayıtlı kullanıcılar kullanıcı adı ve şifre ile giriş yapabilir.

- **Çıkış Yapma (Logout):**
  - Giriş yapan kullanıcı, sistemden çıkış yapabilir.

- **Kimlik Bilgilerini Görüntüleme (Identity):**
  - Giriş yapan kullanıcının bilgileri (kullanıcı adı) görüntülenebilir.

---

## 📂 Proje Yapısı

```plaintext
kullanici_yonetim/
│
├── users.json           # Kullanıcı bilgilerini saklayan dosya
├── main.py              # Ana program
└── README.md            # Proje açıklamaları
```

---

## 🔧 Kurulum ve Çalıştırma

### 1. Python Yükleme
Bu proje **Python 3.x** ile çalışır. Lütfen bilgisayarınızda Python'un kurulu olduğundan emin olun.

### 2. Projeyi Klonlama
Proje dosyalarını bilgisayarınıza klonlayın:
```bash
git clone https://github.com/username/kullanici_yonetim.git
cd kullanici_yonetim
```

### 3. Programı Çalıştırma
Aşağıdaki komutla programı başlatabilirsiniz:
```bash
python main.py
```

---

## 🛠️ Kullanım

1. **Register (Kayıt Olma):**
   - Kullanıcı adı, şifre ve e-posta bilgileri girilerek yeni bir kullanıcı oluşturulur.
   - Bilgiler `users.json` dosyasına kaydedilir.

2. **Login (Giriş Yapma):**
   - Kullanıcı adı ve şifre bilgileri ile giriş yapılır.

3. **Logout (Çıkış Yapma):**
   - Giriş yapan kullanıcı sistemden çıkış yapar.

4. **Identity (Kimlik Görüntüleme):**
   - Giriş yapan kullanıcının bilgileri görüntülenir.

5. **Exit (Çıkış):**
   - Programdan çıkış yapar.

---

## 🔑 Örnek Kullanım

### Kullanıcı Kaydı:
```plaintext
username: johndoe
password: 123456
email: johndoe@example.com
```

### Giriş Yapma:
```plaintext
username: johndoe
password: 123456
```

### Kimlik Bilgisi:
```plaintext
username: johndoe
```

---

## 📌 Notlar

- Kullanıcı bilgileri `users.json` dosyasına JSON formatında kaydedilir.
- Eğer `users.json` dosyası yoksa program yeni bir dosya oluşturur.

---

## 📝 Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasına bakabilirsiniz.

---

## ✨ İletişim

Herhangi bir soru veya öneriniz varsa, lütfen [email@example.com](mailto:email@example.com) adresinden iletişime geçin.
```
