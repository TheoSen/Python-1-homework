# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 12:49:44 2024

@author: TheoS
"""



import matplotlib.pyplot as plt
import numpy as np

# function <plot_classes> plots 2D data points
# which are part of classes. data contains these data points in the following format: The key (string)
# is the name of the class, and the value is a NumPy array of shape (n, 2), where n is the number of
# samples of this class.


def plot_classes(data: dict, save_path: str = None):
    
    plt.ioff()  # Show figures when explicitly stated ("plt.show")
    
    # unpack data from dictionary
    
    ## The key (string) is the name of the class
    feature_name = np.array(list(data.keys()))
    
    ## the value is a NumPy array of shape (n, 2), where n is the number of samples of this class.
    values = np.array(list(data.values()))
    
    #The figure should have a square aspect (i.e. the length of the x- and y-axis should be the same).
    fig, ax = plt.subplots(figsize=(8, 8), dpi=100)
    
    # todo
    for i in range(len(data)):

        #A scatter plot showing all samples, colored according to their classes.
        ax.scatter(values[i][:,0],values[i][:,1], label = feature_name[i])
    
    #The plot must contain a legend that lists all classes.
    ax.legend(loc = 'upper right')
    
    #The axis title must be set to "2D data showing c classes", where c is the number of classes.
    ax.set_title(f"2D data showing {feature_name.size} classes")
    
    # save the plot

    if save_path is not None :  
        plt.savefig(f'{save_path}')
        
    plt.show()
    