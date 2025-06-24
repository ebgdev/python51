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

# def find_greater_1000(lst):
#     n = []
#     for info in products:
#         if info['price'] >1000:
#             n.append(info['name'])
#     return n

# print(find_greater_1000(products))

# ---------------------------------

# products = [
#     {"id": 101, "name": "Laptop", "price": 15000, "category": "Electronics"},
#     {"id": 106, "name": "Phone", "price": 8000, "category": "Electronics"},
# ]


# n = list(map(lambda x:x['name'],filter(lambda x:x['price']>1000,products)))
# print(n) 

# --------------------------------


# def find_avg_price(lst):
#     total = 0
#     for info in lst:
#         total += info['price']
#     return round(total/len(products),3)


# print(find_avg_price(products))

# --------------------------------

# def find_min_max_price(lst):
#     min_value = products[0]['price']
#     max_value = products[0]['price']

#     for info in lst:
#         if info['price'] > max_value:
#             max_value = info['price']

#         if info['price'] < min_value:
#             min_value = info['price']
#     return (min_value,max_value)

# print(find_min_max_price(products))