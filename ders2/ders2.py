# -------------bool()-------------

## bool data type: True or False

# kapi = True
# print(type(kapi))  # --> <class 'bool'>

# if kapi:
#     print("hosgeldiniz")
# else:
#     print("kapi kapali")

# Note: bu kodun ciktisi "hosgeldiniz" olucak cunku sart saglaniyor

# print(bool("")) # --> False
# print(bool("1")) # --> True
# print(bool("0")) # --> True
# print(bool("test")) # --> True

## Bos string disinda diger her string True degeri verir (sonraki derslerde devami var)
# ------------------------

# sehir = "trabzon"

# if sehir == "samsun":
#     print(55)
# elif sehir == "istanbul":
#     print(34)
# else:
#     print("sehir tanimli degil")

# -------------if-elif-else-----------
## kosul/sart --en--> condition
## eger kosul dogruysa (True) iceri girer ve code calisir
## ** Dikkat: her if gordugumuz yerde yeni block baslar.

# if condition:
#   run the code
# elif condition:
#   run the code
# elif condition:
#   run the code
# else:
#   otherwise this code will run 

# -------------if-elif-else-Turkce----------

# eger kosul:
#   kosul saglanirsa code calisir
# egerde kosul:
#     calisacak kod
# egerde kosul:
#     calisacak kod
# aksi_taktirde:
#     bunu yap

# ----------------------------



# mod operatoru:

# sayi = 5

# if sayi % 2 == 0:
#     print(sayi,"sayisi cifttir")
# else:
#     print(sayi,"sayisi tektir")


# ------------------------
## if-else-elif blogu sadece bir kere calisir.
## if else elif block only run once.

# sehir = "trabzon"

# if sehir == "samsun":
#     print("55")
#     sehir = "trabzon"
# elif sehir == "trabzon":
#     print("61")
#     sehir = "adana"
# elif sehir == "adana":
#     print("01")
#     sehir = "izmir"
# else:
#     print("sehir bulunamadi.")

# print("sehirin son durumu: ",sehir)


# ------------------------
## Dikkat: input() her zaman degeri bir string olarak alir
## eger sayi olarak kullanmak istiyorsak once int() ile tam sayiya cevirmemiz gerekiyor.


# sayi = int(input("bir sayi giriniz:"))

# if sayi % 2 == 0:
#     print(sayi,"sayi cifttir")
# else:
#     print(sayi,"sayi tektir")


# ------------------------

# fizik = int(input("fizik puani girniz: "))
# mat = int(input("mat puani girniz: "))
# kimya = int(input("kimya puani giriniz: "))


# toplam = fizik + mat + kimya
# print("ortalama: ",toplam/3)

# ------------------------

# degisken --> variable
# deger atama --en--> Assigning value
# ornek : name = "erfan"

# ------------------------

# print(5 < 7)           # --> less than sign
# print(5 > 7)           # --> greater than sign
# print(8 == 8.0)        # --> equal sign
# print(8 >= 8)          # --> greater equal sign
# print(8 != 8)          # --> not equal sign

# ----------------------------
# cd --> change directory
# ornek : Dosyamizin adresi :  Desktop/Python/ders2/file_name.py
# cd Desktop/Python/ders2/ders2.py
# python file_name.py