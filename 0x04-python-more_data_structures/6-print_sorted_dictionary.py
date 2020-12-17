#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dic = sorted(a_dictionary.keys())
    for x in dic:
        print("{}: {}".format(x, a_dictionary[x]))
