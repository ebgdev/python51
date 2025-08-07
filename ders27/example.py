
dersler = ["mat","fizik","kimya"]

kisi_sayisi = int(input("kisi sayisini girniz: "))

# 1.kisinin mat puanini girniz: 30
# 1.kisinin fizik puanini girniz: 40
# 1.kisinin kimya puanini girniz: 50

# 2.kisinin mat puanini girniz: 30
# 2.kisinin fizik puanini girniz: 40
# 2.kisinin kimya puanini girniz: 50

# 3.kisinin mat puanini girniz: 30
# 3.kisinin fizik puanini girniz: 40
# 3.kisinin kimya puanini girniz: 50

# 1.kisinin ortalamasi: xxx
# 2.kisinin ortalamasi: xxx
# 3.kisinin ortalamasi: xxx

# sinif ortalamasi: xxx


# ----------------------------------
sinif = []
sinif_toplami = 0

for kisi in range(kisi_sayisi): # range(3) -> range(0,3) , 0,1,2
    kisi_dersleri = []
    for ders in dersler:
        puan = int(input(f"{kisi+1} kisinin {ders} puanini giriniz: "))
        kisi_dersleri.append(puan)
        sinif_toplami += puan
    sinif.append(kisi_dersleri)

sinif_ortalamasi = (sinif_toplami/(kisi_sayisi*len(dersler)))
print(f"sinif_ortalamasi: {sinif_ortalamasi}")

for i in range(len(sinif)):
    print(f"{i+1}.kisinin ortalamasi: {sum(sinif[i])/len(dersler)}")