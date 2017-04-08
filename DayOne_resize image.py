#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 12:07:23 2017

@author: wangtianpei
"""

dir_path = "/Users/wangtianpei/Desktop/DayOne2013/"
import PIL
from PIL import Image
for i in range(0,95):
    image = Image.open(dir_path+'flow_{}.png'.format(i))
    img = image.resize((2100,1304), PIL.Image.ANTIALIAS)
    img.save(dir_path+'flow_test_{}.png'.format(i))