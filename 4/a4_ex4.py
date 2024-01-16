# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 15:09:06 2023

@author: TheoS
"""
# mistake:
# ex4 -20P 1. ndigits is an optional argumennt and not a positional argument 2. Code 
# raises ValueError: Invalid format specifier and fails all unittests

def round_(number, ndigits: int) :
    if ndigits is None:
        return int(f'{number:.0f}')
    else:
        for i in range(ndigits):
            return f'{number:.0if}'
    
# print(273.44357831999997)
# for i in range(7):
    
#   print(f'round to {i} precision: {round(273.44357831999997,i)}')
