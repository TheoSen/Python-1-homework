# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 16:18:21 2023

@author: TheoS
"""

def gen_fibonacci(upper_bound):
    try :
        if upper_bound == 0:
            yield 0
        if upper_bound > 0 :
            yield 0
        # check error
        if upper_bound < 0:
            raise ValueError
        if not isinstance(upper_bound,int) :
            if not isinstance(upper_bound,float):
                raise TypeError
    # when ValueError            
    except ValueError :
        print('ValueError')
    # when TypeError
    except TypeError:
        print('TypeError')
    else:
        # sequence start actually at n>2
        # when f_1 = f_2
        result = 1
        # f_2 = 0
        prev_fvalue = 0
        # f_1 = 1
        prev_svalue = 1
        while result <= upper_bound:  
            yield result
            # generate fibonacci number
            # f = f_n-1 + f_n-2
            result = prev_fvalue+prev_svalue
            # f_n-2 = f_n-1
            prev_fvalue = prev_svalue
            # f_n-1 = f
            prev_svalue = result
            
            

# print(list(gen_fibonacci(4184)))