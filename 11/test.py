# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 23:21:33 2024

@author: TheoS
"""

# from a11_ex1 import plot_breastcancer
# from a11_ex2 import plot_classes
from a11_ex3 import plot_lifts

# a11_ex1
# parameters = dict()

# with open("a11_ex1_data.csv") as f:
#     for line in f.readlines():
#         parameter_name, value = line.split(",", maxsplit=1)
#         parameters[parameter_name] = [float(w) for w in value.split(",")]
        
# plot_breastcancer(parameters, 'Breastcancer')

# a11_ex2
# import dill as pkl

# with open("a11_ex2_data.pkl", "rb") as f:
#     ex2_data = pkl.load(f)
    
# plot_classes(ex2_data)

# a11_ex3
import dill as pkl

with open("a11_ex3_data.pkl", "rb") as f:
    ex3_data = pkl.load(f)
    
plot_lifts(ex3_data, 'lift')