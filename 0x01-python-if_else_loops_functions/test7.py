#!/usr/bin/python3
#For testing purposes

islower = __import__('7-islower').islower

name = 'Lee Marvin'

for i in name:
    if i == ' ':
        continue
    if islower(i) == True:
        print('{} is lower'.format(i))
    else:
        print('{} is not lower'.format(i))
