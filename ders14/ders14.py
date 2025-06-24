# my_set = set()

# my_dict = {}

# my_dict['sevval'] = {'name':'sevval unceli','age':20,'mezun':False}

# print(my_dict['sevval']['age'])

# my_list = [['sevval unceli',20,False]]

# print(my_list[0][1])

# ----------------------

# ogrenciler = {'sevval':20,'sedat':30,'sena':20,'damla':20}

# ogrenciler['mikail'] = 30
# ogrenciler.update({'kadir':20})

# print(ogrenciler)

# ----------------------
# # merge

# d1 = {'a':1,'b':2}
# d2 = {'b':3,'c':4}


# def merge_dicts(d1,d2):
#     # d1.update(d2)
#     d2.update(d1)
#     return d2

# print(merge_dicts(d1,d2))

# ----------------------

# ogrenciler = {'sevval':20,'sedat':30,'sena':18,'damla':20}

# print(ogrenciler.get('senaa',"Key NotFound"))

# print(list(ogrenciler.items()))

# print(list(ogrenciler.values()))

# print(list(ogrenciler.keys()))

# removed_item = ogrenciler.pop('sena')
# print(removed_item)

# removed_item_2 = ogrenciler.popitem()
# print(removed_item_2)
# print(ogrenciler)


# ----------------------

ogrenciler = {'sevval':20,'sedat':30,'sena':18,'damla':20}

# total = 0
# for yas in ogrenciler.values():
#     total += yas

# total = sum(list(ogrenciler.values()))
# print(total)

# ---------

# for name , age in ogrenciler.items():
#     print(f"My name is : {name} and I'm {age} years old.")

# ---------


# for item in ogrenciler:
#     print(item)

# ---------

for item in ogrenciler:
    print(item,ogrenciler[item])