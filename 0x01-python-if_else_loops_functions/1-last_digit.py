#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = str(number)
digit = int(digit[-1])
if number < 0:
    digit = - digit

if digit > 5:
    print('Last digit of {} is {} and is greater than 5'.format(number, digit))
elif digit == 0:
    print('Last digit of {} is {} and is 0'.format(number, digit))
else:
    print(f"Last digit of {number} is {digit} and is less than 6 and not 0")
