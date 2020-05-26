#!/usr/bin/python3
'''Rectangle Module'''


class Rectangle:
    '''rectangle class'''
    def __init__(self, width=0, height=0):
        '''initialize rectangle value
           width and height
        '''
        self.__width = width
        self.__height = height

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
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        '''Return area rectangle'''
        return self.__width * self.__height

    def perimeter(self):
        '''return perimeter rectangle'''
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        '''string representation of a rectangle'''
        a = ""
        for h in range(self.__height):
            for w in range(self.__width):
                a = a + '#'
            if h != self.__height - 1:
                a = a + '\n'
        return a

    def __repr__(self):
        '''return a string representation
           of rectangle to recreate a new
           instance.
        '''
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        '''methods thats going to be deleted'''
        print("Bye rectangle...")
