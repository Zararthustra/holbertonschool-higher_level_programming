#!/usr/bin/python3
for a in reversed(range(97, 123)):
    print('{}'.format(chr(a) if a % 2 == 0 else chr(a - 32)), end = "")
