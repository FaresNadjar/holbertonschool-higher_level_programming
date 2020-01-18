#!/usr/bin/python3


class Rectangle:

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __str__(self):
        if 0 in [self.__width, self.__height]:
            return ""
        chain = self.__width * "#"
        return (chain + "\n") * (self.__height - 1) + chain

    def __repr__(self):
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return (self.__height * self.__width)

    def perimeter(self):
        if 0 in [self.__height, self.__width]:
            return 0
        return (2 * (self.__height + self.__width))
