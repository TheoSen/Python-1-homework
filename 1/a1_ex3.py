# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 19:59:47 2023

@author: TheoS
"""

#Exercise 3
# read three float input
length = float(input("Length (meters): "))
width  = float(input("Width (meters): "))
height = float(input("Height (meters): "))

# length = 5.6
# width  = 4.5
# height  = 2.7

#The circumference of the room (float) 

circumference = float(2*(length+width))
print( f"Circumference: {circumference:.2f} meters")

#The volume of the room (float)

volume =  float(length*width*height)
print( f"Volume: {volume:.2f} cubic meters")

#The wall area of the room (int) A window is required for every full 12 square meters of wall area.

wallarea = circumference * height
window = int(wallarea / 12)
print( f"Wall area: {wallarea:.2f} cubic meters")
print( f"Number of windows: {window}")

#The amount of paint that is needed to paint the walls (float). 
#For every square meter of wall, 0.75 liters of paint are required. 
#The area that must be painted is the wall area of the room
#but without the windows. A single window has an area of 2 square meters.

paint = (wallarea - (2*window)) * 0.75
print( f"Needed paint: {paint:.02f} liters")