#!/usr/bin/python3
# python script for testing purposes

uppercase = __import__('8-uppercase').uppercase

my_string = "I've been here for a while now"
print('Before the uppercase call: {}'.format(my_string))
my_string = uppercase(my_string)
print('After the uppercase call: {}'.format(my_string))

