#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_list2 = my_list.copy()
    for  item in my_list2:
        if item == search:
            my_list2[my_list2.index(item)] = replace
    return (my_list2)
