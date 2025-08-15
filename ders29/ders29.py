# # now let's look at O(1)


# def add_items(n):
#     return n + n


# print(add_items(10))

# # O(1 )

# # onceki yaptigimiz orneklerde n sayimiz arttikca
# # bizim denklemimiz de buyuyordu ama bu durumda sadece
# # toplamini yaptigimiz n buyuyor ve yaptigimiz islem sayisi
# # aslinda sabit (tek bir kere toplama islemi yapacagiz)
# -------------------------------
# Linear search

# array = [2,14,22,28,36,48,62,75,88,94]

# def linear_search(array,target):
#     for i in range(len(array)):
#         if array[i] == target:
#             return i
#     return "Not Found"

# print(linear_search(array=array,target=94))

# # T(n) = O(n) # Worst Case ,finding 94
# # T(n) = O(1) # Best Case, finding 2


# -------------------------------
# binary search


# def binary_search(lst:list,target:int) -> int:
#     left = 0
#     right = len(lst) -1
#     mid = 0

#     while left <= right:
#         mid = (right+left)//2
#         if target > lst[mid]:
#             left = mid+1
#         elif target < lst[mid]:
#             right = mid - 1
#         else:
#             return mid
#     return None


# # T(n) = O(log n) # Worst Case
# # T(n) = O(1) # Best Case

# array = [2,14,22,28,36,48,62,75,88,94]

# print(binary_search(array,48))

# -------------------------------
# custome search 

# array = [56,98,-100,985,285]
# names = ["fatih","adil","emir","taha","mess"]


# def minimum(lst):
#     min_value = lst[0]
#     for item in lst:
#         if item < min_value:
#             min_value = item
#     return min_value


# def custome_sort(lst):
#     a = []
#     for _ in range(len(lst)):
#         min_value = minimum(lst)
#         a.append(min_value)
#         lst.remove(min_value)
    
#     return a

# print(custome_sort(array))
# print(custome_sort(names))


# T(n) : n*(n+n+n) = n*(3n) = n^2
