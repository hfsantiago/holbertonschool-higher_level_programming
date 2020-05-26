#!/usr/bin/python3
'''Rectangle module'''


class Rectangle:
    '''Rectangle class'''
    def __init__(self, width=0, height=0):
        '''initialize rectangle with value
           width and heigth
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''getter for width attribute'''
        return self.__width

    @width.setter
    def width(self, value):
        '''sets width with parameter <VALUE>'''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''getter for heigth attribute'''
        return self.__height

    @height.setter
    def height(self, value):
        '''sets heigth with parameter <VALUE>'''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
