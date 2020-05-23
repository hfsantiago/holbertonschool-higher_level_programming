#!/usr/bin/python3
"""text_indentation class"""


def text_indentation(text):
    """
    function that prints text with 2 new lines after the characters
    '.', '?' and ':'
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    flag = False
    special = ['.', '?', ':']
    for i in text:
        if flag is False:
            if i == " ":
                continue
            else:
                flag = True
        if flag is True:
            if i in special:
                print(i)
                print()
                flag = False
            else:
                print(i, end="")
