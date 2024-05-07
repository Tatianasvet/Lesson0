import random


def number():
    list_ = list(range(3, 20))
    case = random.choice(list_)
    return case


case = int(number())
print("Ваше число:", case)
