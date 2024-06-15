from math import pi
class Figure:
    sides_count = 0

    def __init__(self,  color, *sides):
        self.__sides = []
        self.__color = [None, None, None]
        self.filled = False
        if isinstance(color, list | tuple) and len(color) == 3:
            self.set_color(color[0], color[1], color[2])
        if self.sides_count == len(sides) and self.__is_valid_sides(*sides):
            self.set_sides(*sides)
        else:
            for i in range(self.sides_count):
                self.__sides.append(1)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
            if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
                return True
        return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
            self.filled = True
        else:
            print("неверный цвет")

    def set_sides(self, *sides):
        if self.__is_valid_sides(*sides):
            self.__sides.clear()
            for j in sides:
                self.__sides.append(j)
        else:
            print("invalid sides")

    def get_sides(self):
        return self.__sides

    def __is_valid_sides(self, *sides):
        if len(sides) == self.sides_count:
            for side in sides:
                if not (isinstance(side, int) and side > 0):
                    return False
            return True
        else:
            return False

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_radius()

    def set_sides(self, *sides):
        super().set_sides(*sides)
        self.__radius = self.get_radius()

    def get_radius(self):
        return self.get_sides()[0] / (2 * pi)

    def get_square(self):
        return pi * self.__radius**2

class Triangle(Figure):
    pass


class Cube(Figure):
    pass


circle1 = Circle((200, 200, 100), 31415926536)  # (Цвет, стороны)
print(circle1.get_color())
print(circle1.get_sides())
print(len(circle1))
print(circle1.get_radius())
circle1.set_sides(10)  # Изменится
print(len(circle1))
print(circle1.get_square())
