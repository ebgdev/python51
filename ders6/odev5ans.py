kisiler = ["ahmet","onur","faruk","meltem","ayten"]
yaslar = [10,18,17,28,20]



# iki liste seklinde kisiler ve yaslari sirasiyla verilmistir
# yasi 18 ve ustu olan kisilerin isimlerini yazdiriniz

# beklenen cikti : 
# onur
# meltem
# ayten


for i in range(len(kisiler)):
    if yaslar[i] >= 18:
        print(kisiler[i])