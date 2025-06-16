# 12. Create an abstract class Shape with method area() and implement it in Square and Triangle classes.

from abc import ABC , abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):

    def __init__(self,side):
        self.side = side

    def area(self):
        print(f"Area of square is {self.side**2}")

class Trinagle(Shape):

    def __init__(self,height,base):
        self.height=height
        self.base=base
    
    def area(self):
        print(f"Ares of triangle is : {(1/2)*self.base * self.height}")

sqr = Square(2)
tri = Trinagle(12,9)