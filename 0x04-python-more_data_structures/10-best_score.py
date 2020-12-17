#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return (None)
    maxi = max(a_dictionary, key=lambda k: a_dictionary[k])
    return (a_dictionary[maxi])
