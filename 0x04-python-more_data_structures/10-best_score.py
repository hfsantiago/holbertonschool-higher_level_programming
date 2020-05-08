#!/usr/bin/python3
def best_score(a_dictionary):
    temp = 0
    empty = ""
    if a_dictionary is None or a_dictionary == {}:
        return None
    for i in a_dictionary.keys():
        if a_dictionary[i] > temp:
            temp = a_dictionary[i]
            empty = i
    return empty
