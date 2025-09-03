# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

# ODEV

# prices1 = [7,1,5,3,6,4]
# prices2 = [0,1,5,3,6,4]
# prices3 = [1,5,9,6,4,7,0,3]

# def cal_profit(lst):
#     max_profit = 0
#     for i in range(len(lst)-1):
#         for j in range(i+1,len(lst)):
#             # if lst[j] - lst[i] > max_profit:
#             #     max_profit = lst[j] - lst[i]
#             max_profit = max(max_profit,lst[j] - lst[i])

#     return max_profit

# print(cal_profit(prices3))


# this is not a good way to solve the problem ❌
# try to come with a solution of Tn less than n^2 ✅

# -----------------------------------------------

from itertools import permutations

def generate_permutations(arr):
    counter = 0
    perm_list = list(permutations(arr))
    

    for perm in perm_list:
        counter += 1 
        print(perm)
    return f"islem sayisi: {counter}"

arr = [1,2,3,4,5]
print(generate_permutations(arr))

# 5! = 5 x 4 x 3 x 2 x 1 = 120