import random
def loterre(mon, thue):
    tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    win1 = random.choice(tickets)
    tickets.remove(win1)
    win2 = random.choice(tickets)
    print(mon, thue)
    return win1, win2

win1, win2 = loterre('mon', 'thue')
print(win1, win2)
