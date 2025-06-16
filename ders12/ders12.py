# -----------------------------------# Set - Kumeler#---------------------------------#
# Distinct And unorderd
# Benzersiz ve Sirasiz

# aset = {'mikail','damla','sena','sevval','ceren'}
# bset = {'damla','sevval'}

# # aset.add('kadir')
# # aset.remove('damla')
# # aset.discard('sena')
# # aset.pop()
# print(aset)

# print(aset.union(bset)) # birlesim
# print(aset|bset)

# print(aset.intersection(bset)) # ortak  
# print(aset & bset)

# print(aset.difference(bset)) # fark
# print(aset - bset)

# print(bset.issubset(aset)) # al kumesi mi ?
# print(aset.issuperset(bset)) # ust kumesi mi ?

# ---------------------------

# Degistirilmez
# fs = frozenset(['mikail','damla','sena','sevval','ceren'])
# # fs.add('anil')
# print(fs)

# ---------------------------

# listeden tekrar eden elemanlari nasil atabiliriz ?

# array = [1,2,1,13,24,13,35,64,76,35]
# aset = list(set(array))
# print(aset)



# -----------------------------------# Dictionary - Sozlukler#---------------------------------#

# Orderd , key:value , mutable
# Siralilar (3.7 later), anahtar:deger , degistirilebilirler

# my_dict = {"name":'nova',"name":'sevval',"ogrenci":"sevval"}
# print(my_dict['name'])

# -----------------

# my_dict = {"country":"Turkiye","population":90,"language":"Turkish"}

# # print(my_dict["languagee"]) # Hata verir: KeyError
# print(my_dict["language"])


# print(my_dict.get("languagee","Anahtar Bulunamadi")) # Get metodu hata almamamizi saglar.

# ----------------------

# my_set = set() # bos bir kume nasil acilir 
# my_dict = {} # bos bir dictionary nasil acilir 

# print(type(my_dict))

# ----------------------

# my_dict = {"mikail":20,"damla":18,"sena":18,"sedat":20,"sevval":18,"ceren":18}

# toplam = my_dict["mikail"] + my_dict.get("mikail",0)
# keys = list(my_dict.keys())
# keys.append("kadir")
# print(keys)

# total_age = 0
# for person in keys:
#     # total_age += my_dict[person]
#     total_age += my_dict.get(person,0)

# print(total_age)

# ----------------------

# my_dict = {"country":"Turkiye","population":90,"language":"Turkish"}
# print(list(my_dict.keys()))

# ----------------------
my_dict = {"mikail":20,"damla":18,"sena":18,"sedat":20,"sevval":18,"ceren":18}

# print(my_dict.values())
# print(my_dict.items())


# total = 0
# for age in my_dict.values():
#     total += age
# print(total)

# ---------------------

total = 0
for key,value in my_dict.items():
    # print(f"isim: {key},yas: {value}")
    total += value
print(total)