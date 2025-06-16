# soru1:

# lst = [5, 2, 9, 1]
# sorted_lst = []

# while lst:
#     smallest = lst[0]
#     for i in range(1, len(lst)):
#         if lst[i] < smallest:
#             smallest = lst[i]
#     lst.remove(smallest)
#     sorted_lst.append(smallest)

# print(sorted_lst)


# ----------------------------------------

# soru2:

lst = [3, 1, 2, 3, 4, 1, 5]
i = 0
while i < len(lst):
    if lst[i] in lst[:i]:
        lst.pop(lst.index(lst[i],i))
    else:
        i += 1
print(lst)
