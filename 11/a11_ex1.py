# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 23:18:41 2024

@author: TheoS
"""
import matplotlib.pyplot as plt
import numpy as np



def plot_breastcancer(data: dict, save_path: str = None):
    # Choose interactive mode off or on
    plt.ioff()  # Show figures when explicitly stated ("plt.show")
    # plt.ion()  # Show figures immediately (no "plt.show" needed)
    fig, ax = plt.subplots(len(data),figsize=(8, 8), dpi=100)
    fig.tight_layout(h_pad = 2.4)
    
    
    for i in range(len(data)):
        
        # unpack data from dictionary
        feature_name = np.array(list(data.keys()))
        values = np.array(list(data.values()))
        
           
        # the y-ticks must range fronm 1 to the number of datapoints with a step size of 1
        y_pos = np.arange(1,len(values[i])+1, step = 1)
        # verifiying y-axis
        # print(f'y_pos: {y_pos}')
        
        # draw Horizontal bar chart with the color of bar being green
        ax[i].barh(y_pos,values[i],color = 'g')
        ax[i].set_yticks(y_pos)
        
        # x-axis label must be set to <feature_name> (mm)
        ax[i].set_xlabel(f"{feature_name[i]} (mm)")  # Set labels for x-axis and y-axis (don't confuse with the plot axis "ax")
        
        # plots must show a grid on the x-axis with red dashed lines
        ax[i].grid(color='r', linestyle='--', axis = 'x')
        
    # todo 
    # save the plot
    ## after plt.show() is called, a new figure is created
    ## save before plt.show()
    if save_path is not None :  
        plt.savefig(f'{save_path}')
        
    plt.show()
    
    