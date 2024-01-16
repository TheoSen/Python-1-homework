# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 19:12:43 2023

@author: TheoS
"""
from a7_ex1 import Radian
import math

class Rotate:
    
    def __init__(self, matrix: list, degree: float, inplace=False):
        self.matrix = matrix
        self.degree = degree
        self.inplace = inplace
        
    def rotation(self) -> list[list] | None:
        # rotatoin around x-axis
        # rotation matrix
        r_x = [[1,0,0],[0,matn.cos(self.degree),-math.sin(self.degree)],[0,math.sin(self.degree),math.cos(self.degree)]]
        return self.matrix * r_x