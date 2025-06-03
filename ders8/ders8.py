
# liste = ['ceren','sevval','sena']
# astr = 'kadir'


# liste uzerinde reversed()
# -----
# new_list = reversed(liste)
# # print(list(new_list))


# for name in new_list:
#     print(name)

# string uzerinde reversed()
# -----

# new_name = reversed(astr)
# print(new_name)

# for char in new_name:
#     print(char)


# ------------------------------ 

# def topla(lst):
#     # [11,22,33,44,55,66]
#     total = 0
#     for sayi in lst:
#         total += sayi # total = total + sayi
#     return total


# print(topla([11,22,33,44,55,66]))

# ----------------------------------

# lst = [11,22,33,44,55,66]

# def isIn(lst,target):
#     for num in lst:
#         if num == target:
#             return True
#     return False


# print(isIn(lst,44)) # True
# print(isIn(lst,140)) # False


# ----------------------------------

# lst = [11,22,33,44,55,66,77]

# def length(lst):
#     count = 0
#     for eleman in lst:
#         count += 1
#     return count  

# print(length(lst))

# ----------------------------------

# list unpacking

# mercedes , vw, bmw = ['smart','bently','mini']
# print(mercedes)
# print(vw)
# print(bmw)

# ---------------

# mercedes , *vw, bmw = ['smart','lamborgini','bently','skoda','audi','bugatti','mini']
# print(mercedes)
# print(vw)
# print(bmw)

# ---------------
# list slicing - liste dilimlemek

# alist[start:end:step]

# lst = [11,22,33,44,55,66,77,88,99]
# print(lst[::2])
# print(lst[::-1])

# ---------------

# def isPalindorme(kelime):
#     if kelime == kelime[::-1]:
#         return True
#     else:
#         return False

# ----------------------------   

# def isPalindorme(kelime):
#     if kelime == kelime[::-1]:
#         return True
#     return False

# ----------------------------   

# def isPalindorme(kelime):
#     return kelime == kelime[::-1]

# -------------

# print(isPalindorme('kadir')) # False
# print(isPalindorme('kazak')) # True


# ----------------------------  

# # Ic Ice listeler -- Nested Lists

# liste = [[1,2,3],[4,5],[6]]

# # print(liste[0])
# # print(liste[2][0])

# for lst in liste:
#     for num in lst:
#         print(num)


# ----------------------------  

lst = [0,33,44,-2,13,66,77,1,88,99,-100]

# value = -100
def find_min(lst):
    min_value = lst[0] # -100
    for value in lst:
        if value < min_value:
            min_value = value
            
    return min_value
print(find_min(lst))