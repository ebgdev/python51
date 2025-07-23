# soru1:
# DESIRED OUTPUT :
# [[10, 20, 30], [50, 60 70]]

# ------a------

# numbers = []

# with open("soru1.txt") as f:
#     temp = []
#     for line in f:
#         if line != "\n":
#             temp.append(line.strip())
#         else:
#             numbers.append(temp)
#             temp = []
#     numbers.append(temp)
#     print(numbers)


# ------b------

# with open("soru1.txt") as f:
#     groups = f.read().rstrip().split("\n\n")
#     print(groups)
#     nums = [list(map(int,group.split())) for group in groups]
#     print(nums)