# ------------------

# nums = [2,7,11,6,15,3]
# target = 9
# # beklenen cikti: [2,7],[6,3]

# def twoSum(lst,target):
#     cevaplar = []
#     i = 0
#     while i < len(lst)-1:
#         j = i+1
#         while j < len(lst):
#             if lst[i] + lst[j] == target:
#                 cevaplar.append([lst[i],lst[j]])
#             j+=1
#         i+=1
#     return cevaplar

# print(twoSum(nums,target))

# ------------------

matrix1 = [
    [1,2,3],
    [4,7,8],
    [0,0,-1]
]

matrix2 = [
    [4,5,1],
    [6,1,-10],
    [1,1,7]
]

matrix3 = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]

# --------------------------

# for i in range(len(matrix1)):
#     for j in range(len(matrix1[i])):
#         matrix3[i][j] = matrix1[i][j] + matrix2[i][j]

# print(matrix3)

# --------------------------

i = 0
while i < len(matrix3):
    j = 0
    while j < len(matrix3[i]):
        matrix3[i][j] = matrix1[i][j] + matrix2[i][j]
        j += 1
    i+=1

print(matrix3)

# --------------------------