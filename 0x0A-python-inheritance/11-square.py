#!/usr/bin/python3
class BaseGeometry:
    def area(self):
        """ Raises: Exception: if area is not implemented. """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Raises:
                TypeError: if value is not int
                ValueError: if int is less or equal to zero
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
