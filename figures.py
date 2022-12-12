import math


class Triangle:
    """
    This class creates triangle.
    Данный класс создаёт треугольник.
    """
    
    def __init__(self, sides):
        """
        This method creates a triangle.
        Этот метод создаёт треугольник.
        Args:
            sides: list of int or float sides of triangle
            sides: список целочисленных или десятичных чисел сторон треугольника 
        """
        
        self.sides = sides
      
    @property
    def sides(self):
        """
        Returns: sides of triangle.
        Возвращает стороны треугольника.
        """
        
        return self.__sides
  
    @sides.setter
    def sides(self, s):
        """
        Check sides and writes it into variable sides.
        Проверяем стороны и записываем в переменную sides.
        Returns:
            List[d or inr] - current value of sides.
            Список десятичных чисел - настоящее значение сторон.
        Raises:
            Error: if sides are not int or float or programm cant make triangle from
            this sides
            Error: Если стороны не целочисленные или десятичные или программа не может
            сделать из них треугольник
        """
        
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
        """
        Returns: perimeter of triangle.
        Возвращает периметр треугольника.
        """
        
        return sum(self.sides)

    def square(self):
        """
        Returns: square of triangle.
        Возвращает площадь треугольника.
        """
        
        h_per = self.perimetr() / 2
        side_a, side_b, side_c = float(self.sides[0]), float(self.sides[1]), float(self.sides[2])
        return round(math.sqrt(h_per * (h_per - side_a) * (h_per - side_b) * (h_per - side_c)), 2)


class Circle:
    """
    This class creates round.
    Данный класс создаёт круг.
    """
    
    def __init__(self, radius: float) -> None:
        self.radius = radius

    @property
    def radius(self):
        """
        Returns: sides of triangle.
        Возвращает стороны треугольника.
        """
        
        return self.__radius
        
    @radius.setter
    def radius(self, r):
        """
        Check radius and writes it into variable sides.
        Проверяем стороны и записываем в переменную sides.
        Returns:
            r - current value of radius.
            r - значение радиуса.
        Raises:
            Error: if radius are not plural or not int or float
            Error: Если радиус не положителен или не является числом
        """
        
        if not isinstance(r, (float, int)):
            raise Exception("Радиус задается числом")
        if r < 0:
            raise Exception("Отрицательный радиус....Серьезно?")
        self.__radius = r

    def len_circle(self):
        """
        Returns: lenght of circle.
        Возвращает длину круга.
        """
        
        return round(math.pi * self.radius ** 2, 2)
    
    def square(self):
        """
        Returns square of circle.
        Возвращает площадь круга.
        """
        
        return round(2 * math.pi * self.radius, 2)
