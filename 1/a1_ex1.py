# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 18:06:21 2023

@author: TheoS
"""

#Exercise 1 

# creat boolean, int, float, string
bool = False
int = 502
float = 1.4
str = "Math"


#print boolean
#if bool is True:
    #print(bool)
#else:
print(not bool)
    
# The integer must have a minimum print width of 5 and must have leading zeros. • 
print(f"{int:05d}")


# The float must have a minimum print width of 10, and the number of decimals (precision) must be set to 3.

#print(f"{float:10.3f}")

# alternative solution fill with space if the length is < 10
print("{: >10.3f}".format(float))


# The string must be printed three times next to each other, i.e., if the string is A, then AAA must be printed.

print(str * 3)

#trying loop
#i= 0
#for i in range(3):  
    #print(str,end="")