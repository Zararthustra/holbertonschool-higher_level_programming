#!/usr/bin/python3
"""
N queen module -  N queens have to be placed on
an NxN chess board in a way that none of the N
queens is in check by any other queen
"""
import sys


argv_len = len(sys.argv)
if argv_len != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except (TypeError, ValueError):
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)
