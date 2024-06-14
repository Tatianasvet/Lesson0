class Figure:
    def __init__(self,  color, sides):
        self.__sides = sides
        self.__color = (None, None, None)
        self.filled = False
        if isinstance(color, list | tuple) and len(color) == 3:
            self.set_color(color[0], color[1], color[2])


    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
            if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
                return True
        return False


    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)
            self.filled = True
        else:
            print("неверный цвет")


class Circle(Figure):
    pass


class Triangle(Figure):
    pass


class Cube(Figure):
    pass


f = Figure('разные', 'красивый')
print(f.filled, f.get_color())
f.set_color(255, 0, 0)
print(f.filled, f.get_color())
