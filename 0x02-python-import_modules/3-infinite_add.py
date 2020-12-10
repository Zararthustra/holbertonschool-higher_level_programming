#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv)
    add = 0
    for n in range(1, n):
        add += int(sys.argv[n])
    print(add)
