# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 15:33:21 2023

@author: TheoS
"""
# Write a function sub_summarize(nested: list, sub_sums: list) -> int
# that calculates the sum of the input list nested and sums of sub lists 
# arbitrarily nested in the input list (you can assume correct arguments). 
# The sums are stored in the list sub_sums. Use recursion to implement this
# function.
def sub_summarize(nested: list, sub_sums: list) -> int :
    sum = 0
    
    # loop through nested
    for elem in nested:
        # if the 'elem' is int, add that 'elem' into 'sum'
        if isinstance(elem,int):
            sum += elem
        # if the 'elem' is a list, calculate the sub_sum then add into 'sum'
        else:
            sum += sub_summarize(elem, sub_sums)
    # save sum into sub_sums list       
    sub_sums.append(sum)
    # return the current sum 
    return sum

# nested = [1, 2, 3, [4, [5, 6], 7], 8, [9, 10],[11,[12,13],14]]
# sub_sums = []
# sub_summarize(nested, sub_sums)
# print(sub_sums)
