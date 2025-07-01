import random
def mult(a,b):
    return a*b

def devide(a,b):
    return a/b

def cekilis(lst):
    # rand = random.randint(0,4)
    # return lst[rand]

    random.shuffle(lst)
    return random.choice(lst)


if __name__ == "__main__":
    print(cekilis(['apple','banana','kiwi','watermelon']))
    print("merhaba dunya!")