# Dosya: isimler.txt

# Her satır: İsim,Yaş (ör. Adil,22)

# Fonksiyonlar:

# add_student(name, age)

# age → 0–120 arası tam sayı olmalı; değilse InvalidAgeError

# Aynı isim ikinci kez eklenirse DuplicateNameError

# Başarılıysa append ile dosyaya ekler

# list_students() → [(isim, yaş), ...] döndürür

# Dosya yoksa []

# age_score(age) → 100 / age

# age == 0 → ValueError("Age cannot be zero")

# Geçersiz sayı → InvalidAgeError

# ------------------

# Özel istisnalar:
# class InvalidAgeError(ValueError): pass
# class DuplicateNameError(Exception): pass

# ------------------

# CLI menü:
# [1] Ekle [2] Listele [3] Puan [0] Çık

# En az bir yerde try/except, bir yerde else veya finally kullanımı zorunlu

# Davranış: Yanlış girişlerde çökmeden anlamlı hata basar; dosya yoksa listeleme boş döner

# ------------------

# Beklenen Çıktı (Örnek Oturumlar)

# 1) Geçersiz yaş girişi
# [1] Ekle [2] Listele [3] Puan [0] Çık: >> 1
# Ad: >> adil
# Yaş: >> abc
# Hata: Yaş sayı olmalı.
# İşlem bitti.


# 2) Aralık dışı yaş
# [1] Ekle [2] Listele [3] Puan [0] Çık: >> 1
# Ad: >> adil
# Yaş: >> 130
# Hata: Yaş 0–120 arası olmalı.
# İşlem bitti.

# 3) Başarılı ekleme
# [1] Ekle [2] Listele [3] Puan [0] Çık: >> 1
# Ad: >> adil
# Yaş: >> 22
# Kayıt eklendi.
# İşlem bitti.

# 4) Listeleme (dosyada 1 kayıt varken)
# [1] Ekle [2] Listele [3] Puan [0] Çık: >> 2
# 1. Adil — 22


# 5) Aynı ismi tekrar ekleme (duplikat)
# [1] Ekle [2] Listele [3] Puan [0] Çık: >> 1
# Ad: >> ADIL
# Yaş: >> 23
# Hata: İsim zaten kayıtlı.
# İşlem bitti.


# 6) Puan hesaplama — sıfıra bölme
# [1] Ekle [2] Listele [3] Puan [0] Çık: >> 3
# Yaş: >> 0
# Hata: Age cannot be zero


# 7) Puan hesaplama — geçerli değer
# [1] Ekle [2] Listele [3] Puan [0] Çık: >> 3
# Yaş: >> 25
# Puan: 4.0