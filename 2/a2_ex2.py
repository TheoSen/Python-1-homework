# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 16:15:14 2023

@author: TheoS
"""

# Exercise 2

prevNumber = 0

while True :
    userInput = input("Enter number or 'x': ")
    # if inout is 'x'
    if userInput == 'x' :
        #check whether previous number exists
        if prevNumber == 0:
            print("Empty Sequence")
        else:
            print("All numbers had the same digit in the ones place")
        break
    # if input is not 'x'
    else:
        # transfer input to integer
        userInput = int(userInput)
        # check whether previous number exists
        if prevNumber != 0: 
            #check the ones place from the two numbers
            if prevNumber%10 != userInput%10 :
                #if not equals
                print(f"{prevNumber} and {userInput} differ in the ones place")
                # set checkInput to Flase in order to break from the while loop
                break
        # save current input
        prevNumber = userInput