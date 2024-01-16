#!/usr/bin/python3
# computes a to the power of b and returns the value

def pow(a, b):
    result = 1;
    for i in range(b):
        result = result * a
    return result
