#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
'''
This code is to check 
1. the last number and
1. Wether it is less than 6
2. wether it is zero
'''
last_digit = abs(number) % 10
if (number < 0):
    last_digit = -last_digit
if (last_digit > 5):
    print("Last digit of", number, "is", last_digit, "and is greater than 5")
if (last_digit == 0):
    print("Last digit of", number, "is", last_digit, "and is 0")
if ((last_digit < 6) and (last_digit != 0)):
    print("Last digit of", number, "is", last_digit,
          "and is less than 6 and not 0")
