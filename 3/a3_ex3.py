# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 17:40:56 2023

@author: TheoS
"""

# Exercise 3
# some_iterable = [1, 1, 1, 2, 3]
# new_set = {elem for elem in some_iterable}
# new_dict = {str(elem): elem * 10 for elem in some_iterable}

# read input
a = input("Enter comma-separated elements: ")

#debug
# a=['test,test,test']
# a=["test"]
# a=["a,b,ab,hello,holle,ba"]

split_input = a.split(",")

# flat the list
# split_input = [j for i in split_input for j in i]

dict = {}
# loop through each str
for elem in split_input:
    i = 0
    # loop through each char in str
    for char in elem:
        # add hast value of each char
        i += ord(char)
    # save into dictionary
    if elem in dict:
        assert dict[elem] == i
    else:
        dict[str(elem)]= i
    
for x in dict:
    print(f"'{x}' -> {dict[x]}")
 