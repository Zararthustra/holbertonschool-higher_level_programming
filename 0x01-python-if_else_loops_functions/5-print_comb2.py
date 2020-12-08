#!/usr/bin/python3
for a in range (0, 99):
    print('{:d}{:d}, '.format(int(a / 10), int(a % 10)), end = "")
print('99')
