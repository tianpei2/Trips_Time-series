#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 12:09:00 2017

@author: wangtianpei
"""

dir_path = "/Users/wangtianpei/Desktop/Snow_Storm/"
import PIL
from PIL import Image
for i in range(287):
    image = Image.open(dir_path+'flow_{}.png'.format(i))
    img = image.resize((2100,1298), PIL.Image.ANTIALIAS)
    img.save(dir_path+'flow_test_{}.png'.format(i))