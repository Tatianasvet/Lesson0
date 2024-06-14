class Figure:
    def __init__(self,sides,color,filled):
        self.__sides = sides
        self.__color = color
        self.filled = filled

    def get_color(self):
        return self.__color

    def __is_valid_color(self,r,g,b):
        if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
            return True
        else:
            return False
    def set_color(self,r,g,b):
        if self.__is_valid_color(r, g, b):
            self.__color = (r, g, b)
        else:
            print("не верный цвет")


class Circle(Figure):
    pass
class Triangle(Figure):
    pass
class  Cube(Figure):
    pass

f = Figure('разные', 'красивый', 'да')
print(f.filled, f.get_color())
f.set_color([33, 6, 90])
print(f.filled, f.get_color())
