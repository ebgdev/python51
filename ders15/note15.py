# musteriler = {
#     1000000001: {
#         'name': 'John',
#         'sur_name': 'Doe',
#         'age': 17,
#         'married': False
#     },
#     1000000002: {
#         'name': 'Jane',
#         'sur_name': 'Smith',
#         'age': 16,
#         'married': True
#     },
#     1000000003: {
#         'name': 'Alice',
#         'sur_name': 'Brown',
#         'age': 22,
#         'married': False
#     },
#     1000000004: {
#         'name': 'Bob',
#         'sur_name': 'Johnson',
#         'age': 45,
#         'married': True
#     },
#     1000000005: {
#         'name': 'Charlie',
#         'sur_name': 'Williams',
#         'age': 30,
#         'married': True
#     }
# }

# --------------------------------------

# # print(musteriler[1000000001]['age'])

# def find_avg_age(d):
#     total = 0
#     for value in d.values():
#         total += value['age']
#     return total/len(d)

# print(find_avg_age(musteriler))

# --------------------------------------


# def find_married(d):
#     m = []
#     for info in d.values():
#         if info['married']:
#             m.append(info['name'])
#     return m 

# print(find_married(musteriler))

# --------------------------------------

# def count_gr_18(d):
#     count = 0
#     for info in d.values():
#         if info['age'] >= 18:
#             count += 1
#     return f"\nNumber of people older than 18: {count}"


# print(count_gr_18(musteriler))

# --------------------------------------

# def group_by_name_first_letter(d):
#     result = {}
#     for info in d.values():
#         if info['name'][0] not in result:
#             result[info['name'][0]] = [] #olusturma
#         result[info['name'][0]].append(info['name'])
#     return result

# print(group_by_name_first_letter(musteriler))

