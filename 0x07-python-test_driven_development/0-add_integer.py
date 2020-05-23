#!/usr/bin/python3
'''add integer function'''


def add_integer(a, b=98):
    '''function that add 2 integer'''
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
