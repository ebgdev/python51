urunler = {
    'Laptop': 12000,
    'Kulaklik': 750,
    'Telefon': 8000,
    'Akilli Saat': 2000,
    'Tablet': 3500,   
}

# result = [('Kulaklik': 750),('Laptop': 12000)]

def fiyat_sirala_artan(urunler):
    result = [list(urunler.items())[0]]
    for name, price in list(urunler.items())[1:]:
        flag = True
        for i,item in enumerate(result):
            if price <= item[1]:
                result.insert(i,(name,price))
                flag = False
                break
        if flag:
            result.append((name,price))
    return dict(result)
zip


print(fiyat_sirala_artan(urunler))