import math

class Triangle():
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def p_(self):
        p = self.side1 + self.side2 + self.side3
        return p

    def s_(self):
        per = self.p_()
        s = round((per*(per-self.side1)*(per-self.side2)*(per-self.side3))**0.5, 2)
        return s

class Circle():
    def __init__(self, r):
        self.r = r

    def s_(self):
        ra = self.r
        s = round(math.pi*ra*ra, 2)
        return s

    def l_(self):
        ra = self.r
        l = round(math.pi*2*ra, 2)
        return l

triangle = Triangle(3, 4, 5)

print(triangle.s_())