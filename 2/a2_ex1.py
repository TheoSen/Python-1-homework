# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 15:44:13 2023

@author: TheoS
"""

# Exercise 1

from sys import exit


# read input
subsDuration = int(input("Please enter the duration of your subscrpition (in months): "))

# debug var
# subsDuration = 14
# postCode = 4120

# For a negative number or 0, print an error message ("Invalid subscription duration") 
# terminate the program by calling exit(0)

if subsDuration <= 0:
    print("Invalid subscription duration")
    exit(0)
    # subs less than 6 months
elif subsDuration <6:
    priceMonthly = 6.5
    # subs less than a year
elif subsDuration < 12:
    priceMonthly = 5.9 
    # more than a year
else:
    # read the customer’s postal code must be 4 digits
    postCode = int(input("Please enter your postal code: "))
    if len(str(postCode)) != 4:
        print("Invalid postal code")
        exit(0)
    else:
        # the monthly price is 4.xx, where xx is the middle two digits of the postal code.
        priceMonthly = 4.00 + postCode%1000/1000
# cal total price 
totalPrice = subsDuration * priceMonthly
    
# print result
print(f"The price per month is {priceMonthly:.2f}")
print(f"The full price for {subsDuration} is {totalPrice:.2f}")
    