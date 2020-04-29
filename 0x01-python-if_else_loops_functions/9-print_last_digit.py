#!/usr/bin/python3
def print_last_digit(number):
    id = abs(number) % 10
    print(id, end="")
    return(id)
