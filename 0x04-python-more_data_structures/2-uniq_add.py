#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list = set(my_list)
    add = 0
    for x in my_list:
        add += x
    return (add)
