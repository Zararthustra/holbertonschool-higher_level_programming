#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = number % 10
if number >= 0:
    if digit > 5:
        print('Last digit of {} is {} and is greater than 5'
              .format(number, digit))
    elif digit < 6 and digit > 0:
        print('Last digit of {} is {} and is less than 6 and not 0'
              .format(number, digit))
    elif digit == 0:
        print('Last digit of {} is 0 and is {}'
              .format(number, digit))
if number < 0:
    digit = -number % 10
    if digit == 0:
        print('Last digit of {} is 0 and is {}'.format(number, digit))
    else:
        print('Last digit of {} is {} and is less than 6 and not 0'
              .format(number, -digit))
