# -*- coding: utf-8 -*-
'''
JDoe_JSmith_1_4_2: Read and show an image.
'''
import matplotlib.pyplot as plt
import os.path
import numpy as np # “as” lets us use standard abbreviations
   
'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
filename2= os.path.join(directory, 'cat1-a.gif')
# Read the image data into an array
img = plt.imread(filename)
img2 = plt.imread(filename2)
  
# Create figure with 2 subplots
fig, ax = plt.subplots(1, 2)
# Show the image data in the first subplot
ax[0].imshow(img2)
ax[1].imshow(img, interpolation='none') # Override default
ax[0].set_xlim(0, 100)
ax[0].set_ylim(100, 0)
ax[1].set_xlim(135, 165)
ax[1].set_ylim(470, 420)
# Show the figure on the screen
fig.show()