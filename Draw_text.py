#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 20:30:43 2017

@author: wangtianpei
"""
import xlrd

'''Area information'''
file_location1 = '/Users/wangtianpei/Desktop/python/Area.xls'
workbook1 = xlrd.open_workbook(file_location1)
sheet1 = workbook1.sheet_by_index(0)
for i in range(sheet1.nrows-1):
    Area = [[0 for x in range(2)] for y in range(77)]
for i in range(sheet1.nrows-1):
    j = int(sheet1.cell_value((i+1),0))
    Area[j][0] = sheet1.cell_value((i+1),1)
    Area[j][1] = sheet1.cell_value((i+1),2)
'''Area information'''

file_location2 = "/Users/wangtianpei/Desktop/python/Sorted_Pace.xlsx"
workbook2 = xlrd.open_workbook(file_location2)
sheet2 = workbook2.sheet_by_index(0)
time_stamp=[]
start_com=[]
end_com=[]
pace=[]
for row in range(sheet2.nrows-1):
    time_stamp.append(sheet2.cell_value((row+1),0))
    start_com.append(sheet2.cell_value((row+1),5))
    end_com.append(sheet2.cell_value((row+1),2))
    pace.append(sheet2.cell_value((row+1),4))
def count_number(A1, A2, start_row, end_row):
    n = 0
    for i in range(start_row, end_row):
        if start_com[i] == A1 and end_com[i] == A2 or start_com[i] == A2 and end_com[i] == A1:
            n = n+1
    return n
def aver_pace(A1, A2, start_row, end_row):
    pac = 0
    for i in range(start_row, end_row):
        if start_com[i] == A1 and end_com[i] == A2 or start_com[i] == A2 and end_com[i] == A1:
            pac = pace[i] + pac
    if count_number(A1, A2, start_row, end_row) == 0:
        pac = 0
    else:        
        pac = pac/count_number(A1, A2, start_row, end_row)
    return pac

dir_path = "/Users/wangtianpei/Desktop/Chicago_png/"
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

def image_add_text(file1,text1,text2,new_file):

    image = Image.open(file1)
    (width1, height1) = image.size
    fnt = ImageFont.truetype(dir_path+"timeburnernormal.ttf", 50)
    fnt1 = ImageFont.truetype(dir_path+"Times New Romance.ttf", 40)
    fnt2 = ImageFont.truetype(dir_path+"Times New Romance.ttf", 40)
    #Area coordinates - picture position
    intial_po = [42.001745,-87.954131] #by observation
    center = [41.923776,-87.77571]
    draw = ImageDraw.Draw(image)
    for j in range(1,77):
        hei = (Area[j][0]-intial_po[0])*(height1/2)/(center[0]-intial_po[0])
        wid = (Area[j][1]-intial_po[1])*(width1/2)/(center[1]-intial_po[1])
        draw.text((wid, hei),"{}".format(j),font=fnt2,fill=(0,0,0,255))
    # Drawing the text on the picture
    draw.text((width1-200, 50),text1,font=fnt,fill=(0,0,0,255))
    draw.text((width1-200, 100),text2,font=fnt,fill=(0,0,0,255))
    draw.text((20,height1/2-140),'Pace (in minutes/mile) between corresponding areas:',font=fnt1,fill=(0,0,0,255))
    draw = ImageDraw.Draw(image)
    # Save the image(overlay the original one) 
    image.save(new_file)
    
def image_add_pace(file1, start_row, end_row, new_file):
    image = Image.open(file1)
    (width1, height1) = image.size
    fnt = ImageFont.truetype(dir_path+"Times New Romance.ttf", 30)
    draw = ImageDraw.Draw(image)
    n = 0
    for j in range(1,77):
        for q in range(j,77):
            if count_number(j, q, start_row, end_row)!=0:
                draw.text((50+250*int((n*30)/(height1/2)), height1/2-70+(n*30)%int(height1/2)),"{}".format(j)+' to '+"{}".format(q)+':',font=fnt,fill=(0,0,0,255))
                draw.text((170+250*int((n*30)/(height1/2)), height1/2-70+(n*30)%int(height1/2)),"{0:.4f}".format(aver_pace(j, q, start_row, end_row)),font=fnt,fill=(0,0,0,255))
                n = n+1
    # Save the image(overlay the original one) 
    image.save(new_file)
    
final_files=[]
text1 = '00:00'
text2 = '1/1/2013'
Tim = 0
previous_row = 0  
for i in range(sheet2.nrows-2):
    if time_stamp[i+1] != time_stamp[i]:
        Tim = Tim+1
    '''
    if time_stamp[i+1] != time_stamp[i] and Tim-1==125:  
        previous_row = i+1    
    if time_stamp[i+1] != time_stamp[i] and Tim-1>125 and Tim-1<=126:
    '''
    if time_stamp[i+1] != time_stamp[i]:
        time_minute = ((Tim-1)*15)%1440
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
        text2='1/'+"{0:.1f}".format(int((Tim-1)*15/1440)+1)[0:1]+'/2013'
        image_add_text(dir_path+'flow_test_{}.png'.format(Tim-1),text1,text2,dir_path+'flow_final_{}.png'.format(Tim-1))       
        image_add_pace(dir_path+'flow_final_{}.png'.format(Tim-1), previous_row, i+1, dir_path+'flow_final_{}.png'.format(Tim-1)) 
        final_files.append(dir_path+'flow_final_{}.png'.format(Tim-1))
        previous_row = i+1 

