# -*- coding: utf-8 -*-
"""
Created on Fri Mar 14 11:03:36 2025

@author: USER
"""

import matplotlib.pyplot as plt 
import matplotlib.image as mping 

#path of images 
path1 = "C:/Users/USER/Pictures/Rainbow-Rocks.jpg"
path2 = "C:/Users/USER/Desktop/Things-to-Do-in-Nepal.webp"
path3 = "C:/Users/USER/Desktop/supraaaaa.jpg"
path4 = "C:/Users/USER/Desktop/supra.jpg"

#load images
image1 = mping.imread(path1)
image2 = mping.imread(path2)
image3 = mping.imread(path3)
image4 = mping.imread(path4)


#Create figure and axes for 2 rows and 1 column 
fig1, axes = plt.subplots(1, 2, figsize = (10, 5)) # 1 row, 2 columns 

#Display images 
axes[0].imshow(image1)
axes[0].set_title("first Image")
axes[0].axis("off")

axes[1].imshow(image2)
axes[1].set_title("second Image")
axes[1].axis("off")

#Adjust layout and show
plt.tight_layout()
plt.show()

#Create figure and axes for 2 rows and 1 column 
fig1, axes1 = plt.subplots(2, 1, figsize = (5, 10))

#Display images 
axes1[0].imshow(image1)
axes1[0].set_title("first Image")

axes1[1].imshow(image1)
axes1[1].set_title("second Image")