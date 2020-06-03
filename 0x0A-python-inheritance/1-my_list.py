#!/usr/bin/python3
'''My list module'''


class MyList(list):
    '''class MyList'''
    def print_sorted(self):
        '''print ascending sort'''
        print(sorted(self))
