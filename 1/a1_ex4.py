# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 20:23:34 2023

@author: TheoS
"""

#Exercise 4

#Format
i= 0
for i in range(50):  
    print("=",end="")

print("")
print("PC Parts Store - Order")
#Format
i= 0
for i in range(50):  
    print("=",end="")
print("")

#read 3 int input
cableCnt = int(input("Number of cables: "))
monitorCnt = int(input("Number of monitors: "))
keyboardCnt = int(input("Number of keyboards: "))

# cableCnt = 25
# monitorCnt = 5
# keyboardCnt = 20

# Print
cableCost = float(cableCnt * 9.90)
monitorCost = float(monitorCnt * 249.99)
keyboardCost = float(keyboardCnt * 27.50)

#The number of ordered items must have a minimum print width of 3 (3d)
#All float results must be printed with 2 decimal places (.02f)
print(f"{cableCnt:3d} cables (9.90 EUR each) = {cableCost:.02f} EUR")
print(f"{monitorCnt:3d} monitors (249.99 EUR each) = {monitorCost:.02f} EUR")
print(f"{keyboardCnt:3d} keyboards (27.50 EUR each) = {keyboardCost:.02f} EUR")

#Format
i= 0
for i in range(50):  
    print("-",end="")
print("")

#Sum
totalCost = cableCost+monitorCost+keyboardCost
print(f"Total: {totalCost:.02f} EUR")

#Format
i= 0
for i in range(50):  
    print("=",end="")
print("")