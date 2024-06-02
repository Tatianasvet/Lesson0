class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType

b_1 = Building(16, 'office')
b_2 = Building(16, 'living house')
b_3 = Building(9, 'living house')
b_4 = Building(9, 'office')
b_5 = Building(16, 'office')

print(b_1 == b_2)
print(b_1 == b_3)
print(b_1 == b_4)
print(b_1 == b_5)
