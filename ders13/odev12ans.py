# -1- lambda, map ve filter kullanarak fiyatı 1000 TL’den fazla olan ürünlerin isimlerini listeleyin.
# -2- Tüm ürünlerin fiyatlarının ortalamasını hesaplayın(hazir method kullanmadan).
# -3- En pahalı ve en ucuz ürünleri bulun.


products = [
    {"id": 101, "name": "Laptop", "price": 15000, "category": "Electronics"},
    {"id": 102, "name": "Mouse", "price": 300, "category": "Electronics"},
    {"id": 103, "name": "Shirt", "price": 150, "category": "Clothing"},
    {"id": 104, "name": "Keyboard", "price": 700, "category": "Electronics"},
    {"id": 105, "name": "Shoes", "price": 250, "category": "Clothing"},
    {"id": 106, "name": "Phone", "price": 8000, "category": "Electronics"},
]

# -----------------------------

# -1-
higher_than_1000 = list(map(lambda x:x['name'],filter(lambda x: x['price']>1000,products)))
print(higher_than_1000)

# -----------------------------

# -2-1
def find_avarage_price(lst):
    length = len(lst)
    total = 0
    for info in lst:
        total += info['price']
    return "%.2f" % (total/length)
print(find_avarage_price(products))

# -2-2
avg_price = sum([p["price"] for p in products]) / len(products)
print(avg_price)  # 4025.0

# -----------------------------


# -3-
def find_max_min_products(lst):
    min_value = float("inf")
    max_value = float("-inf")
    for info in lst:
        if info['price'] > max_value:
            max_value = info['price']
        if info['price'] < min_value:
            min_value = info['price']
    return f"min_value: {min_value} and max_value: {max_value}"

print(find_max_min_products(products))

