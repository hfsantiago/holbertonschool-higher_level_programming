#!/usr/bin/python3
'''Square-2 module'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''square class'''
    def __init__(self, size):
        '''initialize constructor size'''
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        '''return area'''
        return self.__size ** 2

    def __str__(self):
        '''string representation of object'''
        return "[{}] {}/{}".format(self.__class__.__name__,
                                   self.__size, self.__size)
