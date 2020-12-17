#!/usr/bin/python3
def roman_to_int(roman_string):
    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    add = 0
    if roman_string is None or isinstance(roman_string, bytes):
        return (0)
    if len(roman_string) > 1:
        for i in range(len(roman_string)):
            if i > 0 and dic[roman_string[i - 1]] < dic[roman_string[i]]:
                add -= 2 * dic[roman_string[i - 1]] 
            add += dic[roman_string[i]]
        return (add)
    return (dic[roman_string])
