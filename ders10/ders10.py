# alist = ["kazak","ceren","kucuk","nova"]


# def is_palindorme(word):
#     return word == word[::-1]


# for word in alist:
#     print(is_palindorme(word))

# ---------------------------

# alist = ["mikail","damla"]

# # alist.append("sena","sedat") # --> Hata verir

# alist.append(['sena','sedat','sevval'])

# # alist.extend(['sena','sedat','sevval'])

# ---------------------------

# blist = alist.copy()
# clist = blist[::] # clist = blist[:]
# alist.append("sena")
# blist.append('sedat')
# print(f"alist:{alist}")
# print(f"blist:{blist}")
# print(f"clist:{clist}")

# print()

# alist = [] # alist.clear()
# print(f"alist:{alist}")

# ---------------------------# ---------------------------

# lst = ["nova","damla","ahmet","soner","nova","damla"]
# # print(lst.count('damla'))

# def custome_count(lst,target):
#     sayac = 0
#     for kelime in lst:
#         if target == kelime:
#             sayac += 1
#     return f"found {sayac} from {target} in the list."

# print(custome_count(lst,'sena'))

# ---------------------------# ---------------------------

# lst = ["nova","damla","ahmet","soner","nova","damla"]

# print(lst.index("damla",2))
# # print(lst.index("damla",2,4)) # Hata verir

# ---------------------------# ---------------------------

# fruits = ['apple', 'banana', 'cherry']

# fruits.insert(0, "orange")

# print(fruits)
# ---------------------------# ---------------------------

# fruits = ['apple', 'banana', 'cherry']

# x = (fruits.pop(0))
# print(x)

# ---------------------------# ---------------------------

# fruits = ['apple', 'banana', 'cherry']

# fruits.remove('banana')
# print(fruits)

# ---------------------------# ---------------------------

# lst = ['ceren','sevval','sedat','sena','damla','mikail']

# lst.sort()

# print(lst)

# lst.reverse()
# print(lst)

# ---------------------------# ---------------------------

# y = 10

# def modify_global():
#     global y
#     y = 20
#     print(y)

# print(y)
# modify_global()
# print(y)

# ---------------------------# ---------------------------

# z = 100

# def outer_function():
#     z = 10

#     def inner_function():
#         nonlocal z
#         z = 40
#         print("inside inner function",z)

#     inner_function()
#     print("inside outer_function",z)
# outer_function()

# print(z)