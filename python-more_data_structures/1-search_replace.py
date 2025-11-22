#!/usr/bin/python3


def search_replace(my_list, search, replace):
    for char in my_list:
        new_list = []
        if char == search:
            new_list,append(replace)
        else:
            new_list.append(char)
