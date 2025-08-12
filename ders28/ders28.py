# --------------------------------------------

# my_list = [1,2,3,4,5,6,7,8,9]

# bu ders kapsaminda 3 tane latin karakterini gorecegiz
# - omega          :  Ω  :   Best Case
# - theta          :  θ  :   Avrage Case
# - omicron(big o) :  O  :   Worst Case


# --------------------------------------------


# def print_numbers(n):
#     counter = 0
#     for i in range(n):
#         counter += 1
#         print(counter)

# print_numbers(10)


# --------------------------------------------

# Drop Constants
# carpanlari atabiliriz.

# def print_numbers(n):
#     counter = 0
#     for i in range(n):
#         counter += 1
#         print(counter)

#     for i in range(n):
#         counter += 1
#         print(counter)


# print_numbers(10)
# so in this example we do run the code n + n times: 2n
# O(2n) and then we simplify the notation and drop the constant(sabit)
# so we get O(n)

# --------------------------------------------

# now let's look at O(n^2)


# def print_numbers(n):
#     counter = 0
#     for i in range(n):
#         for j in range(n):
#             counter += 1
#             print(i, j, counter)


# print_numbers(10)

# O(n*n) = O(n^2)

# --------------------------------------------

# now guess what should be this


# def print_numbers(n):
#     counter = 0
#     for i in range(n):
#         for j in range(n):
#             for k in range(n):
#                 counter += 1
#                 print(i, j, k, counter)


# print_numbers(10)


# --------------------------------------------

# # Drop Non-Dominants


# def print_numbers(n):
#     counter = 0
#     for i in range(n):
#         for j in range(n):
#             counter += 1
#             print(i, j, counter)

#     for k in range(n):
#         counter += 1
#         print(k, counter)


# print_numbers(10)

# # O(n^2) + O(n) = O(n^2 + n)
# # burada bizim icin O(n) cok da onemli sayilmadiginda dolayi
# # burayida sadelestirebiliriz boylece bizim denklemimiz:

# # O(T):  O(n^2) olacaktir.
