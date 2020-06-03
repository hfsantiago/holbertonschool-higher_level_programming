#!/usr/bin/python3
'''MyInt module'''


class MyInt(int):
    '''class MyInt'''
    def __new__(cls, *args, **kwargs):
        '''create a new instance'''
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        '''it was != is now =='''
        return int(self) != other

    def __ne__(self, other):
        '''it was == is now !='''
        return int(self) == other
