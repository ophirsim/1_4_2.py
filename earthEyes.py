'''earthEyes demonstrates PIL.Image.paste()
Unpublished work (c)2013 Project Lead The Way
CSE Activity 1.3.7 PIL API
Version 9/10/2013 '''

import PIL
import matplotlib.pyplot as plt
import os.path              

# Open the files in the same directory as the Python script
directory = os.path.dirname(os.path.abspath(__file__))  
student_file = os.path.join(directory, 'pepe the meme.png')

# Open and show the student image in a new Figure window
pepe_img = PIL.Image.open(student_file)
fig, axes = plt.subplots(1, 2)
axes[0].imshow(pepe_img, interpolation='none')

# Display student in second axes and set window to the right eye
axes[1].imshow(pepe_img, interpolation='none')
axes[1].set_ylim(400, 200)
fig.show()

# Open, resize, and display earth
ree_file = os.path.join(directory, 'ree.png')
ree_img = PIL.Image.open(ree_file)
ree_small = ree_img.resize((200, 100)) #eye width and height measured in plt
fig2, axes2 = plt.subplots(1, 2)
axes2[0].imshow(ree_img)
axes2[1].imshow(ree_small)
fig2.show()

# Paste earth into right eye and display
# Uses alpha from mask
pepe_img.paste(ree_small, (300, 300), mask=ree_small) 
# Display
fig3, axes3 = plt.subplots(1, 2)
axes3[0].imshow(pepe_img, interpolation='none')
axes3[1].set_ylim(400, 200)
axes3[1].imshow(pepe_img, interpolation='none')
fig3.show()