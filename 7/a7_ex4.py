# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 19:43:00 2023

@author: TheoS
"""
import math
from a7_ex3 import Distance

class Minkowski(Distance):
    
    def __init__(self, x:int, vect1: list, vect2: list):
        self.vect1 = vect1
        self.vect2 = vect2
        super().__init__(x)

        
    def to_string(self) -> str:
        return super().to_string() + f', vector1={self.vect1}, vector2= {self.vect2}'

    def dist(self) -> float:
        distance = 0
        for i in range(len(self.vect1)):
            distance += (self.vect1[i]-self.vect2[i])**2
        return f'{math.sqrt(distance):.04f}'
    
