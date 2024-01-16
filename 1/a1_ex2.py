# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 19:21:14 2023

@author: TheoS
"""

#Exercise 2

#read 4 int input from the console

a = int(input("Enter a number for a: "))
b = int(input("Enter a number for b: "))
c = int(input("Enter a number for c: "))
d = int(input("Enter a number for d: "))

# a=20
# b=19
# c=17
# d=16

# The sum of a, b and d 

print(f"Sum of a, b and d: {a+b+d}" )

# The product of all four numbers 

print(f"Product of all four numbers: {a*b*c*d}" )

# The sum of a and b times the sum of c and d 

print(f"The sum of a and b times the sum of c and d: {(a+b)*(c+d)}") 

# The result of an integer division when dividing a by d 

if d == 0:
    print("error: d can not be 0")
    
else:
    print(f"a divided by d (int): {int(a/d)}")

# The result of a regular division when dividing a by d 
if d == 0:
    print("error: d can not be 0")
    
else:
    print(f"a divided by d (float): {float(a/d)}")

# The remainder of a division (modulo) when dividing a by b 

if b == 0:
    print("error: b can not be 0")
    
else:
    print(f"Remainder of a divided by b: {a%b}")

# c ^ (-a)

print(f"c to the power of -a: {c**(-a)}")

# b^(1/2)
if b < 0 :
    print("error: b must be a positive number")
else:
    print(f"Square root of b: {b**(1/2)}")

# complex equation
e = (b/3) * (b**(a+d/2)-1) + c
print(f"Complex equation: {e}")