# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 15:33:39 2024

@author: TheoS
"""
import math

class Angle:
    
    def __init__(self, degree: float = None, radian: float = None):
        
        #todo 
        #both arguments are specified
        
        if degree is not None and radian is not None:
            self.degree = degree
            self.radian = radian
            self.consistency()
                               
        #degree is specified 
        elif degree is not None and radian is None:
            self.degree = degree
            self.radian = self.deg_to_rad(degree)
            
        #radian is specified
        elif radian is not None and degree is None:
            self.degree = self.rad_to_deg(radian)
            self.radian = radian
            
        #neither are specified
        else:
            raise ValueError("Either degree or radian must be specified.")
        
    #check whether degree and radian correspond to the same angle   
    def consistency(self):
        if math.isclose(self.degree,self.rad_to_deg(self.radian)):
            return True
        else:
            raise ValueError("Degree and radian are not consistent.")
             
    def __eq__(self, other):
        #check other is an Angle instance
        if isinstance(other, Angle):
            return math.isclose(self.degree,other.degree) and math.isclose(self.radian,other.radian)
        else:
            return NotImplemented
        
    def __repr__(self):
        return f"Angle(degree={self.degree:.3f}, radian={self.radian:.3f})"
    
    def __str__(self):
        return f"{self.degree:.2f} deg = {self.radian:.2f} rad"
    
    def __add__(self,other):
        if isinstance(other,Angle):
            return Angle(degree = self.degree + other.degree, radian = self.radian + other.radian)
        else:
            return NotImplemented
        
    def __iadd__(self,other):
        if isinstance(other,Angle):
            self.degree = self.degree + other.degree
            self.radian = self.radian + other.radian
            self.consistency()
            return self
        else:
            return NotImplemented
        
    #method 
    @staticmethod
    # radian = degree * (pi/180)
    def deg_to_rad(degree):
        return degree * (math.pi/180)
    
    @staticmethod
    # degree = radian * (180/pi)
    def rad_to_deg(radian):
        return radian * (180/math.pi)
     
    @staticmethod
    def add_all(angle, *angles):
        
        sum_degree = angle.degree
        sum_radian = angle.radian
        
        for e in angles:
            sum_degree += e.degree
            sum_radian += e.radian
            
        return Angle(sum_degree,sum_radian)
    
    