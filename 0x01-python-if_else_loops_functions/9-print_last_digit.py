#!/usr/bin/python3
# Prints the last digit of a number

def print_last_digit(number):
    number_str = str(number)
    last_digit = number_str[-1]
    print('{:d}'.format(int(last_digit)), end= '')
    return int(last_digit)
