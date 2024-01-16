# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 16:24:24 2023

@author: TheoS
"""

# Exercise 2

b = []
c = True

while c is True:
    # read input
    a = input("Enter element or 'x' when done: ")
    if a != 'x':
        b.append(a)
    else:
        c = False
        
        # output # 1
        print(f"all: {b}")
        
        # when there is no element in b
        if len(b) == 0:
            print(b)
        else:
            # sort b first in ascending order
            b.sort()
            # creat empty list d to save element from b
            d = []
            # insert first element from b
            d.append(b[0])
            # save first element from d to e1 (previous element)
            e1 = d[0]
            for element in b:
                # if the previous element is not the same as current element from b
                if e1 != element:
                    # insert current element from b into d
                    d.append(element)
                # set previous element as current b element    
                e1 = element
            # output # 2
            print(f"unqiue (sorted): {d}")
        break
    