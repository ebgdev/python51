ages = [12,18,19,20,3,0,30,16]


carpi_2_m = [(lambda x:x*2)(x) for x in ages]
print(carpi_2_m)

carpi_2 = list(map(lambda x:x*2,ages))
print(carpi_2)

greater_18 = list(filter(lambda x:x>18,ages))
print(greater_18)


karma = list(map(lambda x:x*2,filter(lambda x:x>18,ages)))
print(karma)