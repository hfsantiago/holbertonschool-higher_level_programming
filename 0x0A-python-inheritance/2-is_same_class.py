#!/usr/bin/python3
'''Exact same object module'''


def is_same_class(obj, a_class):
    '''return TRUE if is an instance else
       False is in not instace
    '''
    if type(obj) == a_class:
        return True
    else:
        return False
