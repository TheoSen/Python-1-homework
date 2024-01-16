# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 01:05:20 2023

@author: TheoS
"""

def clip(*values, min_=0, max_=1) -> list:
    if len(values) == 0:
        return []
    sub_list = []
    for elem in values:
        if elem < min_ :
            sub_list.append(min_)
        elif elem > max_:
            sub_list.append(max_)
        else:
            sub_list.append(elem)
            
    return sub_list
    


new_list = clip(-1,0.5 ,min_=-2)

print(new_list)