#!/usr/bin/python3
'''class print_square'''


def print_square(size):
    if type(size) != int and type(size) != float:
        raise TypeError("size must be an integer")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    [print('#' * size) for i in range(size)]
