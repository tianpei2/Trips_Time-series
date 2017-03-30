#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 10:02:36 2017

@author: wangtianpei
"""
dir_path = "/Users/wangtianpei/Desktop/Chicago_png/"
import PIL
from PIL import Image
for i in range(126,127):
    image = Image.open(dir_path+'flow_{}.png'.format(i))
    img = image.resize((2100,1358), PIL.Image.ANTIALIAS)
    img.save(dir_path+'flow_test_{}.png'.format(i))
    