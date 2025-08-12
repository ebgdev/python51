# ---- Özel İstisnalar ----
class InvalidAgeError(ValueError): pass
class DuplicateNameError(Exception): pass

FILE = "isimler.txt"

def add_student(name, age):
    name = name.strip().title()
    try:
        age = int(age)
    except ValueError:
        raise InvalidAgeError("Yaş sayı olmalı.")
    if not (0 <= age <= 120):
        raise InvalidAgeError("Yaş 0–120 arası olmalı.")
    if any(n == name for n, _ in list_students()):
        raise DuplicateNameError("İsim zaten kayıtlı.")
    with open(FILE, "a", encoding="utf-8") as f:
        f.write(f"{name},{age}\n")

def list_students():
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            return [(n, int(a)) for n, a in 
                    (line.strip().split(",") for line in f if "," in line)]
    except FileNotFoundError:
        return []

def age_score(age):
    try:
        return 100 / int(age)
    except ZeroDivisionError:
        raise ValueError("Age cannot be zero")
    except ValueError:
        raise InvalidAgeError("Yaş sayı olmalı.")

def main():
    while True:
        secim = input("[1] Ekle [2] Listele [3] Puan [0] Çık: ")
        if secim == "1":
            try:
                add_student(input("Ad: "), input("Yaş: "))
            except (InvalidAgeError, DuplicateNameError) as e:
                print("Hata:", e)
            else:
                print("Kayıt eklendi.")
            finally:
                print("İşlem bitti.\n")
        elif secim == "2":
            for i, (n, a) in enumerate(list_students(), 1):
                print(f"{i}. {n} — {a}")
        elif secim == "3":
            try:
                print("Puan:", age_score(input("Yaş: ")))
            except Exception as e:
                print("Hata:", e)
        elif secim == "0":
            break
        else:
            print("Geçersiz seçim.")

if __name__ == "__main__":
    main()
