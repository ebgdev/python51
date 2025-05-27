# kisiler = ["ahmet","onur","faruk","meltem","ayten"]

# size = len(kisiler)
# print(size)

# for i in range(size): # range(0,5) --> 0 1 2 3 4
#     print(kisiler[i])

# =======================

# i = 0
# while i < size:
#     print(kisiler[i])
#     i= i+1


# =======================


# ogrenci_yaslari = [20,30,40,25,35,45]

# gr_30 = []

# counter = 0
# i = 0
# while i < len(ogrenci_yaslari):
#     if ogrenci_yaslari[i] >= 10:
#         gr_30.append(ogrenci_yaslari[i])
#         print(counter)
#         counter += 1
#     # i = i+1
# print(gr_30)


# print("merhaba ogrenciler")

# =======================

# kisiler = ["ahmet","onur","faruk","meltem","ayten"]

# for i in range(len(kisiler)):
#     print(i,kisiler[i])

# print('-------------')

# for i,name in enumerate(kisiler):
#     print(i,name)


# =======================
# # fibo seri
# array = [0,1]

# for i in range(10):
#     array.append(array[-1]+array[-2])

# print(array)

# =======================

# kisiler = ["ahmet","onur","faruk","meltem","ayten"]

# # kisiler.reverse()
# # print(kisiler)

# reverse_list = []
# for i in range(len(kisiler)): # range(5) --> range(0,5) --> 0 1 2 3 4 
#     reverse_list.append(kisiler[-(i+1)])


# print("orijinal liste: ",kisiler)
# print("ters cevirdigimiz liste: ",reverse_list)


# =======================

# kisiler = ["ahmet","onur","faruk","meltem","ayten"]

# reverse_list = []
# i = 0
# while i < len(kisiler):
#     reverse_list.append(kisiler[-(i+1)])
#     i+=1
# print(reverse_list)