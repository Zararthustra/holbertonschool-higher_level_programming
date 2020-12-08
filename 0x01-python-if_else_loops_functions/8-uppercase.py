#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str) - 1):
            print('{}'.format(chr(ord(str[i]) - 32) if ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z') else str[i]), end = "")
    print(chr(ord(str[i + 1]) - 32))
