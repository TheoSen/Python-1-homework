# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 18:00:44 2023

@author: TheoS
"""

# Exercise 4
from sys import exit

# read input
num_Line = int(input("Enter number of lines: "))

#debug
# num_Line = 3

#check line > 3
if num_Line <= 2:
    print("Invalid number of lines")
    exit(0)
    
# for x lines intotal x '-' needed at top and end
# length of '|' equals x-2 , also x-2 spaces needed in between
# num_vLine : vertical Line
# num_Line : horizontal Line
i = j = k = 0
num_vLine = num_Line - 2

# print first '-' line
while i < num_Line:
    print("-", end = "")
    i += 1

# print '|' and space 
while j < num_vLine:
    print()
    print("|", end = "")
    while k < num_vLine:
        print(" ", end = "")
        k += 1
    print("|", end = "")
    #reset k for futher vertical Line
    k = 0
    j += 1
print()   
#reset i for second horizontal Line 
i = 0
# print second '-' line
while i < num_Line:
    print("-", end = "")
    i += 1