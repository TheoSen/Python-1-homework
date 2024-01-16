# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 23:28:11 2023

@author: TheoS
"""

# Exercise 1

def split_list(lst: list, num_sublists: int) -> list:
    if num_sublists == 0:
        return lst

    min_size = len(lst) // num_sublists
    max_size = min_size + 1
    
    sub_list = []
    
    j = 0
    
    for i in range(num_sublists):
        temp_list = []
        # print(f'big loop {i} started')
        
          
        for x in range(max_size):
            if j < len(lst):
                temp_list.append(lst[j])
                j += num_sublists
                # print(f'j: {j}')
                # print(f'temp: {temp_list}')
                # print(f'loop {j} ended')
                # print()
        sub_list.append(temp_list)
        
        j = i + 1
        
    return sub_list



list = [0,1,2,3,4,5,6,7,8,9,10]
num = 7

new_list = split_list(list,num)

print(new_list)


