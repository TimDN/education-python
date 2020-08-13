from abc import ABC, abstractmethod

class Shape(ABC): # abstract class
    def __init__(self, color):
        self.__color = color

    @abstractmethod
    def get_area(self): # abstract method
        pass # is empty so must use pass keyword

    @property # base class method
    def color(self):
        return self.__color

class Triangle(Shape):
    def __init__(self, base, height, color):
        super().__init__(color)
        self.__base = base
        self.__height = height

    def get_area(self):
        return (self.__base / 2) * self.__height

class Rectangle(Shape):
    def __init__(self, length, width, color):
        super().__init__(color)
        self.__length = length
        self.__width = width

    def get_area(self):
        return self.__length * self.__width

def print_shape(shape):
    print(shape.get_area(), shape.color)

tri = Triangle(3, 4, "Red")
rect = Rectangle(5, 4, "Blue")

print_shape(tri) # prints 6.0 Red
print_shape(rect) # prints 20 Blue

