#!/usr/bin/python3
'''Sqaure module'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''class square'''
    def __init__(self, size):
        '''initialize constructor size'''
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''return area'''
        return self.__size ** 2
