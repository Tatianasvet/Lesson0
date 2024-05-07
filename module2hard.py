import random


def number():
    list_ = list(range(3, 20))
    case = random.choice(list_)
    return case

key =[]
case = int(number())
print("Ваше число:", case)

for i in range(1, case):
    j = i+1
    for j in range(j, case):

        if case % (i+j) == 0:
            k = i,j
            key.append(k)
print("Ваш код:", *key)





