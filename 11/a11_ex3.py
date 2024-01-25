# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 11:53:42 2024

@author: TheoS
"""

import matplotlib.pyplot as plt
import numpy as np

# todo
# data in the following format:
## The key is the name of the powerlifting weight

## The value is another dictionary
## The inner dictionary has two entries

### <weights> refers to a list of n NumPy arrays containing integer numbers in the range [50, 250]
### <ages> refers to a list of n strings that indicate the age groups/IDs of these arrays
### (i.e., arrays and IDs match, there is exactly one array per ID). 


def plot_lifts(data: dict, save_path: str = None):
    
    plt.ioff()  # Show figures when explicitly stated ("plt.show")
    
    # unpack data from dictionary
    
    # get name
    feature_name = np.array(list(data.keys()))
    
    number_plots = len(feature_name)
    
    fig ,ax = plt.subplots(ncols = number_plots, sharey = True,figsize= (11,7), dpi = 300)
    
    
    # get values, <values> is another dictionary 
    for i in range(number_plots):
        
        values = data.get(feature_name[i])
        
        # weight_name = np.array(list(values.keys()))
        weight_value = list(values.values())
        
        # set label
        label = weight_value[1]
        
        # boxplot
        bplot = ax[i].boxplot(weight_value[0], patch_artist=True, medianprops = dict(color = "black", linewidth = 1),vert = 'True')
        
        # set the medianprops
        
        # fill boxes with colors
        cmap = plt.get_cmap('Set1')
        # cmap.colors otherwise Errormessage: 'ListedColormap' object is not subscriptable 
        for patch, color in zip(bplot['boxes'], cmap.colors):
            patch.set_facecolor(color)
            
        # set the x label
        ax[i].set_xticklabels(label, rotation = -90)
        ax[i].set_xlabel('man age range')
        ax[i].set_title(f'{feature_name[i]}')
        
        # set the grid for y axis
        ax[i].yaxis.grid(color='b', linestyle='-.', linewidth=1)
        
    # set common y label   
    fig.supylabel('Best (kg)') 
    # avoiding overlap
    fig.tight_layout(rect=(0.025,0,0.05,1))  
    
    # save
    if save_path is not None :  
        plt.savefig(f'{save_path}')
        
    plt.show()
    
    
    