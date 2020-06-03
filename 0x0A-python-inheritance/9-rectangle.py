#!/usr/bin/python3
'''Full Rectangle module'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''rectangle class'''
    def __init__(self, width, height):
        '''initialize constructor
           width and height
        '''
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        '''return area'''
        return self.__width * self.__height

    def __str__(self):
        '''str method to print rectangle description'''
        return "[{}] {}/{}".format(self.__class__.__name__,
                                   self.__width, self.__height)
