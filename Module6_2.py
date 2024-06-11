class Vehicle:

    def __init__(self):
        self.vehicle_type = "none"


class Car:
    price = 1000000

    def horse_powers(self):
        return 200


class Nissan(Car, Vehicle):

    def __init__(self, vehicle_type):
        self.price = 2000000
        self.vehicle_type = vehicle_type

    def horse_powers(self):
        return 150

car = Nissan("car")
print(car.vehicle_type, car.price)
