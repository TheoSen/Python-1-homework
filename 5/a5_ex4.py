# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 17:20:37 2023

@author: TheoS
"""

def f(x: int): 
    try:
        g(x) 
        print("f1" )
    except TypeError:
            print("f2" )
    finally: 
        print("f3" )
                
def g(x: int): 
    try:
        h(x) 
        print("g1" )
    except TypeError: 
            print("g2" )
    except ValueError: 
        print("g3" ) 
        if x < -10: 
            raise IndexError 
            print("g4" )
        else: 
            print("g5" ) 
        print("g6")
        
def h(x: int):
    try:
        if x > 10: 
            raise TypeError
        if x < 0: 
            raise ValueError
    finally: 
        print("h1" )
    print("h2" )
    
f(-11)