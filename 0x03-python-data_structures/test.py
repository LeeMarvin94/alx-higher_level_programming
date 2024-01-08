#!/usr/bin/python3

replace_in_list = __import__('2-replace_in_list').replace_in_list

my_list = [1, 4, 9, 3, 25]
idx = 3

print('Before replacement: my_list = {}'.format(my_list))
my_list = replace_in_list(my_list, idx, 16)
print('After replacement: my_list = {}'.format(my_list))
