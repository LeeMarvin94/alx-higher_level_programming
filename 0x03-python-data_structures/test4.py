#!/usr/bin/python3

new_in_list = __import__('4-new_in_list').new_in_list

my_list = [1, 4, 9, 16, 26]
print('Before replacement: my_list = {}'.format(my_list))
my_list = new_in_list(my_list, 4, 25)
print('After replacement: my_list = {}'.format(my_list))
