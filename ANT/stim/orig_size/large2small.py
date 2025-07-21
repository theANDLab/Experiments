# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 15:52:58 2021
BMP to PNG converter
@author: Paul Knytl
"""

from PIL import Image
import os

redux = 2 #image reduction factor int

files = os.listdir()

for file in files:
    file_split = file.split('.')
    if file_split[1] == 'png':
        img = Image.open(file)
        
        # Provide the target width and height of the image
        (width, height) = (img.width // redux, img.height // redux)
        img = img.resize((width, height))
        img.save(file_split[0] + '.png')

