# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 14:41:20 2023

@author: TheoS
"""
import os

# there must be an another way to solve with without looping the file twice

def file_statistics(path: str):
    if not os.path.exists(path):
        raise OSError(f"Path {path} does not exist")
    elif not os.path.splitext(path)[1] == '.txt' :
        raise ValueError(f"Path {path} is not a text file")
    else:
        with open(path, "r", encoding = 'utf-8') as f:
            sum_line, sum_word, sum_char, sum_digits = 0, 0, 0, 0
            
            # loop through line
            for line in f:
                sum_line += 1
                # split the line and calculate word
                for word in line.split():
                    sum_word += 1
                    
            # goes back to the beginning of the file
            f.seek(0)           
            while chars := f.read(10240):
                for char in chars:
                    # sum_line start with 1 
                    # if char == '\n' or char == '\r':
                    #     sum_line += 1
                    # not working excatly since not only word can be separated by space
                    # if char == ' ':
                    #     sum_word += 1
                    if char.isdigit():
                        sum_digits += 1
                    sum_char += 1
            
            #display
            print('--------------------')
            print(f'Statistics of file {os.path.split(path)[1]}:')
            print(f'Number of lines: {sum_line}')
            print(f'Number of words: {sum_word}')
            print(f'Number of characters: {sum_char}')
            print(f'Number of characters: {sum_digits}')
            
# path  = ['F:/Uni/Python/6/Examples/ex1_1.txt',
#           'F:/Uni/Python/6/Examples/ex1_2.txt',
#           'F:/Uni/Python/6/Examples/ex1_3.txt',
#           'F:/Uni/Python/6/Examples/ex1_4.py',
#           'F:/Uni/Python/6/Examples/ex1_5.txt'
#           ]
# for elem in path:
#     file_statistics(elem)