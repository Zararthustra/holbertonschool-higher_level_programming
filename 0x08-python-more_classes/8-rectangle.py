#!/usr/bin/python3
"""
This is rectangle module
"""


class Rectangle:
    """
    create a rectangle class
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        constructor
            args:
                width: width value
                height: height value
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """
        str method
        """
        string = ""

        if self.width == 0 or self.height == 0:
            return string
        else:
            for i in range(self.height):
                for j in range(self.width):
                    string += str(Rectangle.print_symbol)
                if i != self.height - 1:
                    string += '\n'
            return string

    def __repr__(self):
        """
        repr method
        """
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """
        del method
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """
        getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter
            args:
                value: width value
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter
            args:
                value: height value
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """
        return rect area
        """
        return self.width * self.height

    def perimeter(self):
        """
        return rect perimeter
        """
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width + self.height) * 2

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the bigger
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
