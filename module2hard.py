import random


def number():
    list_ = list(range(3, 20))
    case = random.choice(list_)
    return case

key = []
run = int(number())
print("your number:", run)

for i in range(1, run):
    j = i+1

    for j in range(j, run):

        if run % (i+j) == 0:
            k_1 = i
            key.append(k_1)
            k_2 = j
            key.append(k_2)

print("your code:", *key)
