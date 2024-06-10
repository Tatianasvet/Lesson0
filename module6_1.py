class Car:
    price = 1000000
    def horse_powers(self):
        return 300

class Nissan(Car):
    price = 2000000
    def horse_powers(self):
        return 400

class Kia(Car):
    price = 1500000
    def horse_powers(self):
        return 350

car_1 = Car()
car_2 = Nissan()
car_3 = Kia()
print(car_1.price, car_1.horse_powers())
print(car_2.price, car_2.horse_powers())
print(car_3.price, car_3.horse_powers())