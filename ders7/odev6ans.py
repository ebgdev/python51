odemeler = [
    100,60,80,85,30,47,200,100.0001,200,20,73,202,
    100,60,90,58,302,47,120,500,20.1,210,76,201,
    ]


reverse_list = []
i = 0
while len(reverse_list) < 10:
    if odemeler[-(i+1)] >= 100:
        reverse_list.append(odemeler[-(i+1)])
    i+=1
print(reverse_list)

