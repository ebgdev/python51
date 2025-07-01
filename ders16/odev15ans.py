words = ['apple', 'banana', 'grape', 'apricot', 'berry', 'cherry']
# # output: {'a': ['apple', 'apricot'], 'b': ['banana', 'berry'], 'g': ['grape'], 'c': ['cherry']}

# ------------------------

# def group_by_first_letter(lst):
#     result = {}
#     for item in lst:
#         if item[0] not in result: # sadece anahtarlari kontrol eder.
#             result[item[0]] = []
#         result[item[0]].append(item)
#     print(result)
# group_by_first_letter(words)

# ------------------------

# def group_by_first_letter(lst):
#     result = {}
#     for item in lst:
#         if item[0] not in result:
#             result[item[0]] = [item]
#         else:
#             result[item[0]].append(item)
#     return result
# print(group_by_first_letter(words))