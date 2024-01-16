# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 16:58:53 2023

@author: TheoS
"""

# Exercise 3
from sys import exit

while True:
    
    start_Input = int(input("Start: "))
    stop_Input = int(input("Stop: "))
    step_Input = int(input("Step: "))
    if  start_Input < 0 or stop_Input < 0 or step_Input < 0 :
        print("Invalid input")
        exit(0)
    else:
        break
# Debug
# start_Input = 1
# stop_Input = 10
# step_Input = 4

i = 0
count_Evennum = 0
sum_Oddnum = 0

for value in range(start_Input, stop_Input, step_Input):
   # print only the first five iteration number 
   if i < 5:
       print(f"Number in iteration {i} = {value}")
       i += 1
   # even number
   if (value % 2) == 0 :
       count_Evennum += 1
   # odd number
   else:
       sum_Oddnum += value
# print result
print(f"Even number count = {count_Evennum}")
print(f"Sum of odd numbers = {sum_Oddnum}")