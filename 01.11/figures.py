import math


class Triangle:
    def __init__(self, sides):
        self.sides = sides
    
    @property
    def sides(self):
        return self.__sides
        
    @sides.setter
    def sides(self, s):
        if len(s) != 3:
            raise Exception("Введено неверное количество сторон")
        try:
            side_a, side_b, side_c = float(s[0]), float(s[1]), float(s[2])
        except:
            raise ValueError("Sides must be float or int")
        if not (side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a):
            raise Exception("Стороны не валидны")
        if side_a < 0 or side_b < 0 or side_c < 0:
            raise Exception("Отрицательных сторон не бывает челлл")
        else:
            self.__sides = [side_a, side_b, side_c]
    
    def perimetr(self):
        return sum(self.sides)

    def square(self):
        h_per = self.perimetr() / 2
        side_a, side_b, side_c = float(self.sides[0]), float(self.sides[1]), float(self.sides[2])
        return round(math.sqrt(h_per * (h_per - side_a) * (h_per - side_b) * (h_per - side_c)), 2)

class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius

    @property
    def radius(self):
        return self.__radius
        
    @radius.setter
    def radius(self, r):
        if not isinstance(r, (float, int)):
            raise Exception("Радиус задается числом")
        if r < 0:
            raise Exception("Отрицательный радиус....Серьезно?")
        self.__radius = r

    def len_circle(self):
        return round(math.pi * self.radius ** 2, 2)
    
    def square(self):
        return round(2 * math.pi * self.radius, 2)

print(Circle(2).square())