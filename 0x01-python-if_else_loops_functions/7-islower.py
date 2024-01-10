#!/usr/bin/python3
# python function that checks for lowercase caracteres

def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
