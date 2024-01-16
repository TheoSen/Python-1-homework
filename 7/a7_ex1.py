# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 18:52:45 2023

@author: TheoS
"""

class Radian:
    
    def __init__(self, degree: float):
        self.degree = degree
        
    def rad(self):
        result = self.degree * (3.14/180)
        return float('{:.2f}'.format(result))
    
    def print(self):
        print (f'Degree is {self.degree:.02f} and radian is {self.rad():.02f}')
        
c = Radian(90) 
print(c.rad())
c.print()