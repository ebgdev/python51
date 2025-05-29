# ----------------------------# ----------------------------# ---------------------------
# odemeler = [
#     10,20,30
# ]

# # ----------------------------

# i = 0
# total = 0
# while i < len(odemeler): # 0 1 2
#     total += odemeler[i]
#     i+=1

# print('total sum: ',total)
# print(f"total sum: {total}")

# ----------------------------

# print(sum(odemeler))

# ----------------------------

# toplam = 0

# for i in range(len(odemeler)): # range(3)--> range(0,3) --> 0 1 2
#     toplam = toplam + odemeler[i] # toplam = 60

# print(toplam)

# ----------------------------

# total = 0
# for item in odemeler: #  odemeleri --> 10,20,30
#     total += item 

# print(total)

# ----------------------------# ----------------------------# ----------------------------


# odemeler = [
#     10,20,30,11,22,33
# ]

# # print(len(odemeler))

# size = 0

# for num in odemeler:
#     size += 1

# print(size)


# ----------------------------------------

odemeler = [10,20,30,11,22,33]
isimler = ['soner','taha','ceren','kadir']


# def size(lst):
#     # lst = [10,20,30,11,22,33]
#     sayac = 0
#     for item in lst:
#         sayac += 1
#     print(f"listenin uzunlugu: {sayac}")



# size(odemeler)
# size(isimler)

# ---------------------------

# def custome_sum(lst):
#     # lst =  [10,20,30,11,22,33]
#     total = 0
#     for item in lst:
#         total += item
#     return(f"our list sum is : {total}")



# print(custome_sum(odemeler))



# ---------------------------
isimler = ['soner','taha','ceren','kadir']

def findInList(lst,target):
    for name in lst:
        if name == target:
            return(f"Target Found : {target}")
            
    return(f"Target Not Found : {target}")

print(findInList(isimler,'kadir'))


print(max(odemeler))