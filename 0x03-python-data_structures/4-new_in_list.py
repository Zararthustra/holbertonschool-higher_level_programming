#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        list = my_list.copy()
        if 0 <= idx < len(my_list):
            list[idx] = element
        return (list)
