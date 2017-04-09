#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 14:01:54 2017

@author: wangtianpei
"""

dir_path = "/Users/wangtianpei/Desktop/Snow_Storm/"
final_files=[]
for i in range(287):
    final_files.append(dir_path+'flow_final_{}.png'.format(i))
import imageio
images = []
for file in final_files:
    images.append(imageio.imread(file))
imageio.mimsave(dir_path+'Trips_Time series.mp4', images,fps=6)