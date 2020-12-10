#!/usr/bin/python3
import sys
n = len(sys.argv)
arg = sys.argv
if n == 1:
    print("0 arguments.")
if n == 2:
    n -= 1
    print("1 argument:")
    print("{}: {}".format(n, arg[n]))
if n > 2:
    print("{} arguments:".format(n - 1))
    for n in range(1, n):
        print("{}: {}".format(n, arg[n]))
