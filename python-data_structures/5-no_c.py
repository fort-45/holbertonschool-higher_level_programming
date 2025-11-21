#!/usr/bin/python3


def no_c(my_string):
    new_chars = []
    for char in my_string:
        if char != 'c' and char != 'C':
            new_chars.append(char)
    new_string = "".join(new_chars)
    return new_string
