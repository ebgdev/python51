# def add_ten(x=10):
#     return x+10

# print((lambda x:x+10)(10))


# lst = [1,2,3,4,5]
# iteratif = [(lambda x: x*2)(x)for x in lst]
# print(iteratif)

# uzeri_2 = [(lambda x:x**2)(x) for x in lst]
# print(uzeri_2)

# ---------------
# 1.yontem
# uzeri_3 = map(lambda x:x**3,lst)
# for item in uzeri_3:
#     print(item)
# 2.yontem
# uzeri_3 = list(map(lambda x:x**3,lst))
# print(uzeri_3)

# ---------------
# lst = [1,2,3,4,5]

# def is_even(x):
#     return x % 2 == 0

# foo = list(map(is_even,lst))
# print(foo)

# ---------------

# lst = [1,2,3,4,5,6,7,8,9,10]

# def select_evens(lst):
#     result = []
#     for item in lst:
#         if item % 2 == 0:
#             result.append(item)
#     return result
# print(select_evens(lst))


# evens = list(filter(lambda x:x%2==1,lst))
# print(evens)

# -----------------------------------

# lst = [1,2,3,4,5,6,7,8,9,10]

# uzeri_2 = list(map(lambda x: x*x,lst))
# print(uzeri_2)

# elli_ustu = list(filter(lambda x: x>=50 , uzeri_2))
# print(elli_ustu)

# -----------------------------------

# lst = ["mikail","damla","kadir","sedat"]

# new_list = list(map(lambda x: x+" python ogreniyor",lst))
# print(new_list)

# -----------------------------------

# mixed_data = [12,'hello',3.5,42,'world',99,0.1,'0.1','python',23]

# integers = list(filter(lambda x: type(x) == int,mixed_data))
# multi_10 = list(map(lambda x:x*10,integers))
# print(integers)
# print(multi_10)

# -----------------------------------
# Tuple
# orderd and immutable
# orderd --> ben hangi sirada girdiysem eleman hep o sirada (index) tutulur
# immutable --> degistirilmez

# my_tuple = (1,-10,3,5)
##  my_tuple[0] = -500 --> Hata aliriz
# print(my_tuple[0])


# tek elemanli tuple
# my_tuple = (1,)
# print(type(my_tuple))

# lst = [1]
# tple = (1,)


# print(len(dir(lst))) #liste methodlarin sayisi 
# print(len(dir(tple))) # tuple methodlarinin sayisi

# my_tuple = ("mikail","damla","kadir")
# new_list = list(my_tuple)
# new_list.append('sedat')
# my_tuple = tuple(new_list)
# print(my_tuple)

# -----------------------------
# import sys

# her biri bilgisayar da ne kadar yer kapliyor

# lst = [i for i in range(1,1000001)]
# atple = tuple(lst)

# print("lst: ",sys.getsizeof(lst))
# print("tuple: ",sys.getsizeof(atple))