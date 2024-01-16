# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 13:49:41 2024

@author: TheoS
"""
# from a10_ex1 import extend 
# from a10_ex2 import elements_wise
# from a10_ex3 import one_hot_encoding\
from a10_ex4 import moving_average_2D
import numpy as np

# a10_ex1
# m1 = np.arange(2*3).reshape(2,-1)
# print(m1)
# print(extend(m1, 2, 3))
# print(extend(m1, 4, 5))

# try:
#     print(extend(m1, 2, 1))
# except ValueError as e:
#     print(f"ValueError: {e}")
# try:
#     print(extend(m1, 1, 2))
# except ValueError as e:
#     print(f"ValueError: {e}")
    
# m2 = np.arange(2*3,dtype=float).reshape(2,-1)
# print(m2)
# print(extend(m2, 4, 5))
# print(extend(m1, 4, 5, fill=10))

# try:
#     print(extend(m2, 4,4, fill="foo"))
# except ValueError as e:
#     print(f"ValueError: {e}")
    
# m3 = np.ones(1)
# print(m3)
# try:
#     print(extend(m3, 2, 3))
# except ValueError as e:
#     print(f"ValueError: {e}")

# a10_ex2
# def func(x):
#     return x*x + 3*x + 2

# a1 = np.array(range(2 * 2 * 3), dtype=float).reshape(2, 2, -1)
# b = a1

# a2 = np.array(range(2 * 3), dtype=float).reshape(2, -1)
# c = a2

# print(np.shares_memory(a1, b))
# elements_wise(a1, func)
# print(np.shares_memory(a1, b))
# print(f"a1:\n {a1}")

# print(np.shares_memory(a2, c))
# elements_wise(a2, func)
# print(np.shares_memory(a2, c))
# print(f"a2:\n {a2}")

# a10_ex3
# a = np.array(["a", "a", "b", "c"])
# print(f'original array : {a}')
# print(f'one-hot-encoding: \n {one_hot_encoding(a)}')

# a = np.array([10, 5, 15, 20])
# print(f'original array : {a}')
# print(f'one-hot-encoding: \n {one_hot_encoding(a)}')

# a = np.array([[1, 2], [3, 4]])

# try:
#     print(one_hot_encoding(a))
# except ValueError as e:
#     print(f"ValueError: {e}")


# a10_ex4
arr = np.arange(4*5).reshape(4,-1)
print(arr)

result = moving_average_2D(arr, 3)
print(result)

try:
    moving_average_2D(arr, 5)
except ValueError as e:
    print(f"ValueError: {e}")
    
try:
    moving_average_2D(np.array([["a","b"],["c","d"]]), 2)
except TypeError as e:
    print(f'TypeError: {e}')    