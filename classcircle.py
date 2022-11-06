"""Find the area and the length of circle."""


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def length_of_circle(self):
        import math
        pi = math.pi
        return round(2 * pi * self.radius, 2)

    def area(self):
        import math
        pi = math.pi
        return round(pi * self.radius ** 2, 2)


circle = Circle(3)
print('Length of circle:', circle.length_of_circle())
print('Area:', circle.area())
