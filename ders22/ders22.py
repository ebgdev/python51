# class Book:
#     def __init__(self,id, author):
#         self.id = id
#         self.author = author


#     def __str__(self):
#         return f"kitabin yazari: {self.author}"
    

#     def __repr__(self):
#         return f"<__main__.Book> object id:{self.id} , author: {self.author}"
    


# clean_code = Book('Clean Code','Uncle Bob')

# print(repr(clean_code))


# ------------------- dynamic version ----------------------

# class Book:
#     def __init__(self, id, author):
#         self.id = id
#         self.author = author

#     def __str__(self):
#         return f"kitabin yazari: {self.author}"

#     def __repr__(self):
#         return f"<{self.__class__.__module__}.{self.__class__.__name__}> object id:{self.id} , author: {self.author}"

# clean_code = Book('Clean Code','Uncle Bob')

# print(repr(clean_code))


# -----------------------------------------


# open()

# f = open("names.txt")
# print(f.read(11))
# print(f.read())
# f.close()


# ---------------------

# f = open("names.txt")
# print(f.read(11))
# f.seek(0) # 
# print(f.read())
# f.close()


# ----------next-keyword----------

# file = open("names.txt")

# for i in range(12):
#     print(i,next(file))

# file.close()

# ------------------------------

# with open("names.txt",'r') as file:
#     output = file.readlines()

# print("otomatik bir sekilde dosya close (kapandi) yapildi.")
# arr = []
# print(output)
# for name in output:
#     arr.append(name.removesuffix('\n'))


# print(arr)
# -----------

# print("mikail\n")
# print("ceren")
# print("damla\n")


# ---------------------------------

# with open("names.txt") as f:
#     for name in f:
#         print(name)


# ---------------------------------

# readline methodu tek bir satir okur.
# with open("names.txt") as f:
#     print(f.readline())



# ---------------------------------
# # remove '\n' from end of elements on original array

# with open("names.txt",'r') as file:
#     output = file.readlines()
    

# for i in range(len(output)):
#     output[i] = output[i].removesuffix("\n")

# print(output)