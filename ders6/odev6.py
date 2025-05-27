# Aşağıda bir ödeme sistemi üzerinden yapılan tüm ödemeler bir liste olarak verilmiştir:

odemeler = [
    100,60,80,85,30,47,200,100.0001,200,20,73,202,
    100,60,90,58,302,47,120,500,20.1,210,76,201,
    ]

# Bu listedeki ödemeler, zaman sırasına göre ilk ödemeden son ödemeye doğru sıralanmıştır.

# 📌 Görev:
# 100 TL ve üzerindeki ödemelerden, en son yapılan 10 tanesini ekrana yazdıran bir Python programı yazınız.

# 🎯 Kurallar:
# Yalnızca 100 TL ve üzerindeki ödemeler dikkate alınacaktır.

# Liste sondan başa doğru (en yeni ödeme en başta olacak şekilde) incelenmelidir.

# Çıktı, en son yapılan uygun 10 ödemenin bir listesidir.

# Ödemeler, bulundukları sıraya göre tersten yazdırılmalıdır.


# yukarida sistemimize yapilan tum odemeleri goruntulemekteyiz
# 100 lira ve uzerinde olan son 10 odemeyi istemekteyiz 
# ✅ Beklenen Çıktı Örneği: [201, 210, 500, 120, 302, 100, 202, 200, 100.0001, 200]

reverse_list = []
i = 0
while len(reverse_list) < 10:
    if odemeler[-(i+1)] >= 100:
        reverse_list.append(odemeler[-(i+1)])
    i+=1
print(reverse_list)


