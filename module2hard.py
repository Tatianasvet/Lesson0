import random


def number():
    list_ = list(range(3, 20))
    case = random.choice(list_)
    return case


case = int(number())
print("Ваше число:", case)

for i in range(1, (case//2 +1)):
    j = i+1
    for j in range(j, (case//2 +1)):
        print(i, j)



