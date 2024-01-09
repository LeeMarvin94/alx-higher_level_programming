#!/usr/bin/python3
import sys

print('{:d} arguments.'.format(len(sys.argv) - 1))
for i in range(len(sys.argv[1:])):
        print('{:d}: {}'.format(i + 1, sys.argv[i + 1]))   
