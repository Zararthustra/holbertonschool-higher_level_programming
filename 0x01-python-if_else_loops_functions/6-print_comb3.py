#!/usr/bin/python3
for a in range(0, 10):
    print('{:d}{:d}, '.format(int(a / 10), int(a % 10)), end = "")
for a in range(12, 80):
    if a / 10 < a % 10:
        print('{:d}{:d}, '.format(int(a / 10), int(a % 10)), end = "")
print('89')
