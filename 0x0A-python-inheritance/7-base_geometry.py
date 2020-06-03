#!/usr/bin/python3
'''Same class or inherit from module'''


class BaseGeometry():
    '''empty class BaseGeometry'''
    pass

    def area(self):
        '''that raises an Exception with the message area()
           is not implemented
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''if value is not an integer: raise a TypeError exception,
           with the message <name> must be an integer
           if value is less or equal to 0: raise a ValueError exception
           with the message <name> must be greater than 0
        '''

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
