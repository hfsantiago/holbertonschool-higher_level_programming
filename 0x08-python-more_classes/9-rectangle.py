#!/usr/bin/python3
'''Rectangle module'''


class Rectangle:
    '''rectangle class'''
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        '''initialize rectangle value
           width and height
        '''
        self.width = width
        self.height = height
        type(self).number_of_instances = type(self).number_of_instances + 1

    @property
    def width(self):
        '''getter for width attribute'''
        return self.__width

    @width.setter
    def width(self, value):
        '''sets width parameter <VALUE>'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''getter for height attribute'''
        return self.__height

    @height.setter
    def height(self, value):
        '''sets height parameter <VALUE>'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        else:
            self.__height = value

    def area(self):
        '''Return area rectangle'''
        return self.__width * self.__height

    def perimeter(self):
        '''Return perimeter rectangle'''
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width * 2) + (self.height * 2)

    def __str__(self):
        '''string representation of rectangle'''
        symbol = str(self.print_symbol)
        a = ""
        if self.width == 0 or self.height == 0:
            return ""
        for h in range(self.__height):
            for w in range(self.__width):
                a = a + symbol
            if h != self.__height - 1:
                a = a + '\n'
        return a

    def __repr__(self):
        """
        returns a string representation of the rectangle to be able
        to recreate a new instance using eval()
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        '''methods that going to be deleted'''
        print("Bye rectangle...")
        type(self).number_of_instances = type(self).number_of_instances - 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''return the biggest rectangle'''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area() or rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        '''return a new rectangle instance with
           width == height == size
        '''
        return cls(size, size)
