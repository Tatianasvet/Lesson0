import random
def number():
    tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    win = random.choice(tickets)
    return win
win = int(number())
print(win)

