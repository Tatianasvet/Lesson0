class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        self.new_floor = new_floor
        if self.number_of_floors < new_floor or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for item in range(1, int(new_floor) + 1):
                print(item)


hause_1 = House('ЕКБ', 24)
hause_2 = House('АСБ', 9)
hause_1.go_to(4)
hause_2.go_to(10)
