# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 13:53:46 2023

@author: TheoS
"""

# Exercise 1

# input

nRow = int(input("Number of rows: "))
nCol = int(input("NUmber of cols: "))

# debug
# nRow = 10
# nCol = 10

# creat the matrix
a = []

for i in range(nRow):
    a.append([0])
    # creat/reset the row for insert
    b = []
    for j in range(nCol):
        # creat one row with the length of how many columen
        if i is j:
            b.append(1)
        else:        
            b.append(0)
    # add b row into the columen i of a
    a[i] = b
    i += 1
    
# output
# print header
print("   ", end = "")
for i in range(nCol):
    print(f'{i} ', end = "")
print()

#print '-' line
print("  ",end = "")
for i in range(nCol):
    print("--",end = "")
print()

#print the matrix
for i in range(len(a)):
    print(f'{i}|', end = '')
    for j in range(len(a[i])):
        print(f' {a[i][j]}', end = "")
    print()
    