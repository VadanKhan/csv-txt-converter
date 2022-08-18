# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

'Python file format converter'
#%%
import numpy as np
#%%
#IMPORT FILE NAME HERE
name = "16-12_39_54, VK second testsavg"
#IMPORT FILE INPUT FORMAT HERE
fmt = ".txt"
#IMPUT FILE OUTPUT FORMAT HERE
outfmt = ".csv"
#%%
raw = np.genfromtxt(name + fmt,dtype='float',delimiter=',',skip_header=0)
np.savetxt(name + outfmt, raw, delimiter = ',')