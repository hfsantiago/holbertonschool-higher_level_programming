#!/usr/bin/python3
def remove_char_at(str, n):
    aux = ""
    for i in range(0, len(str)):
        if i != n:
            aux += str[i]
    return aux
