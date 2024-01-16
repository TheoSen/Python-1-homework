# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 17:58:17 2024

@author: TheoS
"""
import math
from a8_ex1 import Angle
from a8_ex2 import Square,Power
from a8_ex3 import StandardScaler

# a8_ex1
# a1 = Angle(degree=45)
# a2 = Angle(radian=math.pi/4)
# a3 = Angle(30, math.pi/6)

# print(a1)
# print(a2.__repr__())
# print(repr(a3))
# print(a1 == a2)
# print(a1 + a2)

# a1 += a3
# print(a1)

# sum_angle = Angle.add_all(a1, a2, a3)
# print(sum_angle)

# try:
#     a4 = Angle()
# except ValueError as e:
#     print(e)
# try:
#     a5 = Angle(degree=45, radian=1)
# except ValueError as e:
#     print(e)

# a8_ex2
# x = 3
# square = Square()
# cube = Power(3)
# print(square.exponent, square(x))
# print(cube.exponent, cube(x))
# m1 = square * 2
# print(m1.exponent, m1.__call__(x))
# m2 = square * cube
# print(m2.exponent, m2.__call__(x))
# try :
#     square("foo")
# except TypeError as e:
#     print(e)
# try :
#     Power("foo")
# except TypeError as e:
#     print(e)    

# a8_ex3
feats1 = [0,2,4,6,8,10]
feats2 = [1,3,5,7,9]
s = StandardScaler()
print(s.mu, s.sig)
s.fit(feats1)
print(s[0], s[1])
feats1_scaled = s.transform(feats1)
print(feats1_scaled)
feats2_scaled = s.transform(feats2)
print(feats2_scaled)
s = StandardScaler()
feats2_scaled = s.fit_transform(feats2)
print(feats2_scaled)
print(s[0], s[1])
s = StandardScaler()

try:
    s.transform(feats2)
except ValueError as e:
    print(f"{type(e).__name__}: {e}")
try:
    print(s["foo"])
except TypeError as e:
    print(f"{type(e).__name__}: {e}")
try:
    print(s[2])
except IndexError as e:
    print(f"{type(e).__name__}: {e}")