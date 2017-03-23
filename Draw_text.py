#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 20:30:43 2017

@author: wangtianpei
"""
dir_path = "/Users/wangtianpei/Desktop/Chicago_png/"
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
def image_add_text(file1,text1,text2,new_file):

    image = Image.open(file1)
    (width1, height1) = image.size
    fnt = ImageFont.truetype(dir_path+"timeburnernormal.ttf", 50)
    # Drawing the text on the picture
    draw = ImageDraw.Draw(image)
    draw.text((width1-200, 50),text1,font=fnt,fill=(0,0,0,255))
    draw.text((width1-200, 100),text2,font=fnt,fill=(0,0,0,255))
    draw = ImageDraw.Draw(image)

    # Save the image(overlay the original one) 
    image.save(new_file)
    
final_files=[]
text1 = '00:00'
text2 = '1/1/2013'
for i in range(0,671):
    time_minute = (i*15)%1440
    if int(time_minute/60) < 10: 
        if time_minute%60 == 0:
            text1='0'+"{}".format(int(time_minute/60))+':'+'0'+"{}".format(time_minute%60)
        else:
            text1='0'+"{}".format(int(time_minute/60))+':'+"{}".format(time_minute%60)
    else:
        if time_minute%60 == 0:
            text1="{}".format(int(time_minute/60))+':'+'0'+"{}".format(time_minute%60)
        else:
            text1="{}".format(int(time_minute/60))+':'+"{}".format(time_minute%60)
    text2='1/'+"{0:.1f}".format(int(i*15/1440)+1)[0:1]+'/2013'
    image_add_text(dir_path+'flow_test_{}.png'.format(i),text1,text2,dir_path+'flow_final_{}.png'.format(i))
    final_files.append(dir_path+'flow_final_{}.png'.format(i))