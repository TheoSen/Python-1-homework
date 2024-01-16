# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 16:14:16 2023

@author: TheoS
"""
import os

def chunks(path: str, size: int, **kwargs):
    if not os.path.isfile(path):
        raise ValueError(f'path {path} is not a file')
    if size < 1:
        raise ValueError('size is incorrect')
        
    with open(path, **kwargs) as f:
        while chunk := f.read(size):
            yield chunk
        
path = 'F:/Uni/Python/6/Examples/ex2_example.txt'

for i,c in enumerate(chunks(path, 25, mode='rb')):
    print(f'Chunk {i} = {c}')     