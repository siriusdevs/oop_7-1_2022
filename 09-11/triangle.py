import math


class Triangle:

    def __init__(self, side_a: float, side_b: float, side_c: float) -> None:
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        if not self.is_valid():
            raise NotValidTriangle

    def perimetr(self) -> float:
        return round((self.side_a + self.side_b + self.side_c), 2)


    def area(self) -> float:
        p = (self.side_a + self.side_b + self.side_c) / 2
        return round((p * (p - self.side_a) * (p - self.side_b) * (p - self.side_c)), 2)


    def is_valid(self) -> bool:
        sides = sorted([self.side_a, self.side_b, self.side_c])
        for side in sides:
            if not isinstance(side, float|int):
                return False 
            if side <= 0:
                return False
        if sides[0] > sides[1] + sides[2]: 
            return False 
        return True


class NotValidTriangle(Exception):

    pass 


class NotValidCircle(Exception):

    pass 


class Circle:

    def __init__(self, radius: float) -> None:
        self.radius = radius 
        if not self.is_valid():
            raise NotValidCircle


    def length(self) -> float:
        return round(2 * math.pi * self.radius)
    

    def area(self) -> float:
        return round(math.pi * self.radius)
    

    def is_valid(self) -> bool:
        if isinstance(self.radius, float | int):
            return self.radius > 0



triangle = Triangle(12, 10, 20)
print('Perimetr:', triangle.perimetr(), 'Area:', triangle.area())


circle = Circle(5)
print('length:', circle.length(), 'Area:', circle.area())
