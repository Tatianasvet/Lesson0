class House:
    def __init__(self):
        self.numberOfFloors = 0

        # Простой метод
    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(self.numberOfFloors)

        # Специальный метод
    def __set__(self, floors):
        self.numberOfFloors = floors
        print(self.numberOfFloors)


h_1 = House()
h_2 = House()
h_1.setNewNumberOfFloors(10)
h_2.setNewNumberOfFloors(30)
h_1.__set__(2)
h_2.__set__(300)

