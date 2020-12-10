#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import *
    n = len(sys.argv)
    if n != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    arg = sys.argv
    a = int(arg[1])
    b = int(arg[3])
    op = arg[2]
    if op == '+':
        print("{} {} {} = {}".format(a, op, b, add(a, b)))
    elif op == '-':
        print("{} {} {} = {}".format(a, op, b, sub(a, b)))
    elif op == '*':
        print("{} {} {} = {}".format(a, op, b, mul(a, b)))
    elif op == '/':
        print("{} {} {} = {}".format(a, op, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
