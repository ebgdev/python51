# 1 - kullanicidan taban ve yukseklik alinacak (input ile)
# 2 - ucgenin alani hesaplanacak
# 3 - sonuc(alan) , int degere cevrilecek (int() veya (//) kullanilabilir)
# 4 - bu deger cift mi yoksa tek mi kontrol edilecek


# -----------------beklenen-cikti----------------

# taban giriniz: 5
# yukseklik giriniz: 3
# ucgenin alani tektir:  17


# -------------------------------------------------------------------------------------------------------------------------------------


taban = int(input("taban giriniz: "))
yukseklik = int(input("yukseklik giriniz: "))


alan = (taban * yukseklik)//2  # --> asaga dogru yuvarlayarak int'e cevirmis oluyoruz

if alan % 2 == 0:
    print(alan, "alan cifttir")
else:
    print(alan, "alan tektir")