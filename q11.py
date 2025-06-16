# 11. Create a Rectangle and Circle class with methods to calculate area and perimeter. Use inheritance and method overriding.

from math import pi
class Shape:
    def area(self):
        print("Area of a shape")
    def perimeter(self):
        print("perimeter of a shape")


class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def area(self):
        print(f"Area of ractangle is : {self.length*self.breadth}")
    def perimeter(self):
        print(f"Perimeter of reactangle is : {2*(self.length+self.breadth)}")

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        print(f"Area of a circle is : {pi*(self.radius**2)}")

    def perimeter(self):
        print(f"Perimeter of a circle is : {2*pi*self.radius}")


rectangle = Rectangle(2,4)
circle = Circle(2)