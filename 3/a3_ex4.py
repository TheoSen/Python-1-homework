# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 16:12:29 2023

@author: TheoS
"""

# Exercise 4

# read input
input_str = input("Enter comma-separated string: ")

# debug
# input_str = "abc,1,1,12,hello,1,5,1,5"
# input_str = "test"
# input_str = "test,python,python,1,2,4,5,5,1,10,9,2,3,3,3,1"

string_split = input_str.split(",")

str_list = []
int_list = []

for elem in string_split:
    if elem.isdecimal():
        int_list.append(int(elem))
    else:
        str_list.append(elem)
        
dict = {}

for int in int_list:
    if int in dict:
        dict[int] += 1
    else:
        dict[int] = 1
        
# output
print(f'integers: {int_list}')
print(f'counts: {dict}')
print(f'rest: {str_list}')
        
        