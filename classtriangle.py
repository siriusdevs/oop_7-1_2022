"""Find the area and the perimeter of triagle."""


class Triangle:

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def area(self):
        p = (self.side1 + self.side2 + self.side3) / 2
        area_2 = p * (p - self.side1) * (p - self.side2) * (p - self.side3)
        for i in range(int(area_2 / 2)):
            if i ** 2 == area_2:
                return i


triangle = Triangle(3, 4, 5)
print('Perimeter:', triangle.perimeter())
print('Area:', triangle.area())
