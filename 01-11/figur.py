import math



class Triangle:
    def __init__(self, a: float, b: float, c: float) -> None:
        self.a = a
        self.b = b
        self.c = c

    def perimetr(self)-> float:
        return self.a + self.b + self.c


    def area(self)-> float:
        p = (self.a + self.b + self.c) / 2
        s = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return s


class Circle:
    def __init__(self, r: float)-> None:
        self.r = r


    def area_circle(self)-> float:
        return round(math.pi * (self.r**2), 1)
    
    
    def perimetr_circle(self)-> float:
        return round(2 * math.pi * self.r, 1)
        


triangle = Triangle(6, 12, 10)
circle = Circle(3)
print("Площадь круга", round(circle.area_circle(), 1))
print("Длина окружности", round(circle.perimetr_circle(), 1))
print("Периметр треугольника", triangle.perimetr())
print("Площадь треугольника", round(triangle.area(), 1))
