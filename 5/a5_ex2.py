# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 19:07:23 2023

@author: TheoS
"""
import os
# Write a function print_directory(dir_path: str) that enumerates and prints 
# recursively all les and sub directories in an input directory specied 
# by its path dir_path.

def print_directory(dir_path: str):
    
    if os.path.isfile(dir_path):
        print(f'{dir_path} is a file not a directory.')
        
    elif os.path.isdir(dir_path):
        print(f'path_to_the_directory_{os.path.basename(dir_path)}')
        print_directory_recursively(dir_path, 1)
    else:
        print(f'{dir_path} invalid')
        
def print_directory_recursively(dir_path: str, level: int = 0):
    
    for elem in os.listdir(dir_path):
        # recreat the path with os.path.join
        current_path = os.path.join(dir_path,elem)
        # if elem is point to file
        if os.path.isfile(current_path):
            print('\t'*level+os.path.basename(current_path))
        # if elem is point to directory    
        elif os.path.isdir(current_path): 
            print('\t'*level+os.path.basename(current_path))
            print_directory_recursively(current_path,level+1)
            
# dir_path = 'F:/Uni/Python/5/d0'
# print_directory(dir_path)
        