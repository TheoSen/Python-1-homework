# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 15:31:59 2023

@author: TheoS
"""

def sort(elemts: list, ascending: bool = True):
    temp_ele = 0
    i = 1
    # loop through list
    while i < len(elemts):
        #compare next elemts to the previous elements
        j = i
        while j > 0 and elemts[j] < elemts[j-1]:
            # save current 
            temp_ele = elemts[j]
            # save prev into current
            elemts[j] = elemts[j-1]
            # put current into prev position
            elemts[j-1] = temp_ele
            j -= 1
        i += 1
    
    # if it required descending sort, just reverse the already ascending sorted list
    if ascending is False:
        i = 0
        # only have to do i many times, which i is half the size of the list 
        # e.g. for size 5 list only have to swap twice which is 5//2 = 2
        while i < len(elemts)//2:
            # save current value
            temp_ele = elemts[i]
            # swap the value at the another end, which is at (len-1-i) positoin
            elemts[i] = elemts[len(elemts)-1-i]
            # swap temp to the end value
            elemts[len(elemts)-1-i] = temp_ele
            
            i += 1
            
            
        
some_list = [1, 3, 0, 4, 5, 6, 7]
sort(some_list, False)
print(some_list)