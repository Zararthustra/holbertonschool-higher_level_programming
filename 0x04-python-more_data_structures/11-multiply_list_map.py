#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    new = my_list.copy()
    new = list(map((number).__mul__, new))
    return (new)
