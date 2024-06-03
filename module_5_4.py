class Building:
    total = 0

    def __init__(self):
        Building.total += 1

    # def __str__(self):
    #     return f'{self.name}'

# Building_list = []
for i in range(40):
    B = Building()
    # Building_list.append(B)

for i in range(Building.total):
    print(f'B {i + 1}')


print('total', Building.total)
