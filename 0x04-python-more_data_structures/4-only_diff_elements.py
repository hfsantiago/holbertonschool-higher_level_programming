#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    a = []
    for i in set_1:
        if i not in set_2:
            a.append(i)
    for j in set_2:
        if j not in a and j not in set_1:
            a.append(j)
    return a
