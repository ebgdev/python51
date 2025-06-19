# lst = [1,-11,33,-25,50,20]

# def find_avg(lst):
#     total = 0
#     for num in lst:
#         total += num
#     return round(total / len(lst),2)

# print(find_avg(lst))

# -----------------------

# import statistics

# lst = [1,-11,33,-25,50,20]
# print(statistics.mean(lst))

# -----------------------

# import statistics

# lst = [1,-11,33,-25,50,20]
# print(round(statistics.mean(lst),3))

# -----------------------

# import statistics

# lst = [1,-11,33,-25,50,20]
# print("%.2f" %(statistics.mean(lst)))

# -----------------------

# lst = [1,-11,33,-25,50,20]

# # beklenen cikti: [2,-22,66,-50,100,40]

# new_list = list(map(lambda x:x*2,lst))
# print(new_list)

# -----------------------

# lst = [1,-11,33,-25,50,20]

# # beklenen cikti: [2,-22,66,-50,100,40]

# def mult_with_2(x):
#     return 2*x

# new_list = list(map(mult_with_2,lst))
# print(new_list)

# -----------------------

# def mult_with_2(x):
#     return 2*x

# new_list = list(map(mult_with_2,lst))
# print(new_list)


# pozitif = list(filter(lambda x: x>0,lst))
# print(pozitif)

# -----------------------

# lst = [1,-11,33,-25,50,20]

# def mult_with_2(x):
#     return 2*x

# new_list = list(map(mult_with_2,lst))
# print(new_list)


# pozitif = list(filter(lambda x: x>0,lst))
# print(pozitif)

# pozitif sayilarin x2 lerini:

# pozitif_x_2 = list(map(lambda x: x*2,filter(lambda x:x>0,lst)))
# print(pozitif_x_2)

# -----------------------

# lst = [1,-11,33,-25,50,20]

# def find_min_max_price(lst):
#     min_value = min(lst)
#     max_value = max(lst)
#     return min_value,max_value


# print(find_min_max_price(lst))

# -----------------------

# import time
# def is_prime(num:int) -> bool:
#     """This function gets an int value and checks if the value is prime or not"""
#     count = 0
#     if num < 2:
#         return False

#     for i in range(2,round(num**1/2)):
#         if num % i == 0:
#             return False
#     return True

# t1 = time.time()
# print(is_prime(7000003))
# t2 = time.time()
# print(t2-t1)


# ---------------------------------

# lst = ['kazak','kucuk','nova','ada','emre']

# -----------------

# palindormes = list(filter(lambda x: x == x[::-1],lst))
# print(palindormes)

# ------------------

# def find_palindormes(lst):
#     new_list = []
#     for word in lst:
#         if word == word[::-1]:
#             new_list.append(word)
#     return new_list


# print(find_palindormes(lst))