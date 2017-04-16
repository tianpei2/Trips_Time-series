#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 22:01:58 2017

@author: wangtianpei
"""

dir_path = "/Users/wangtianpei/Desktop/Random_Week/"
import PIL
from PIL import Image
for i in range(671):
    image = Image.open(dir_path+'flow_{}.png'.format(i))
    img = image.resize((2100,1290), PIL.Image.ANTIALIAS)
    img.save(dir_path+'flow_test_{}.png'.format(i))