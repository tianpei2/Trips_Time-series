#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 20:36:43 2017

@author: wangtianpei
"""

import xlrd
import os
import time
from selenium import webdriver             
import folium
#from folium import plugins
from folium.plugins import PolyLineTextPath
from folium.features import (
    ClickForMarker, CustomIcon, DivIcon, GeoJson, LatLngPopup, CircleMarker,
    MarkerCluster, PolyLine, Vega, RegularPolygonMarker,
    TopoJson, WmsTileLayer
)
'''census tract'''
file_location= "/Users/wangtianpei/Desktop/python/CensusTracts.xls"
workbook = xlrd.open_workbook(file_location)
sheet = workbook.sheet_by_index(0)
s=[]
for i in range(sheet.nrows-1):
    s.append(i)
    
k =[]
for i in range(sheet.nrows-1):
    s[i] = sheet.cell_value((i+1),0).split('(')[3]
    s[i] = s[i].split(')')[0]
    k.append([])
    for j in range(len(s[i].split(', '))):
        k[i].append(s[i].split(', ')[j])
'''census tract'''

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

files=[]
browser = webdriver.Chrome('/Users/wangtianpei/Desktop/python/chromedriver')
'''Trip_data'''
dir_path="/Users/wangtianpei/Desktop/Chicago_png/"
def save_map(m,filename,pngname):
    delay=2
    fn=filename
    tmpurl='file://{path}/{mapfile}'.format(path=os.getcwd(),mapfile=fn)
    m.save(fn)
    #use chrome driver, if you have not used it before, download it at https://sites.google.com/a/chromium.org/chromedriver/downloads
    #browser = webdriver.Chrome('C://Users//Price//chromedriver.exe')
    browser.get(tmpurl)
    #Give the map tiles some time to load
    time.sleep(delay)
    #take screenshot
    browser.save_screenshot(dir_path+pngname)
    #browser.quit()
    

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
        
Tim = 0
previous_row = 0  
for i in range(sheet2.nrows-2):
    if time_stamp[i+1] != time_stamp[i]:
        Tim = Tim+1
    if time_stamp[i+1] != time_stamp[i] and Tim-1==125:  
        previous_row = i+1
    
    if time_stamp[i+1] != time_stamp[i] and Tim-1>125 and Tim-1<=126:
        m = folium.Map(
                location=[41.923776,-87.775710],
                zoom_start=12,
                tiles='openstreetmap'
                )
        for w in range(sheet.nrows-1):
            list_node = [[0 for x in range(2)] for y in range(len(s[w].split(', ')))]
            for r in range(len(s[w].split(', '))):
                list_node[r][1] = float(k[w][r].split(' ')[0])
                list_node[r][0] = float(k[w][r].split(' ')[1]) 
            census_tract = folium.PolyLine(
                    list_node,
                    weight=1,
                    color = 'blue'
                    )
            m.add_children(census_tract)     
        for j in range(1,77):
            for q in range(j,77):
                if aver_pace(j, q, previous_row, i+1) <= 0.2262:
                    Trip = folium.PolyLine(
                            [Area[j], Area[q]],
                            weight= count_number(j, q, previous_row, i+1)/2,
                            color = 'red'                                                       
                        )
                else:
                     Trip = folium.PolyLine(
                            [Area[j], Area[q]],
                            weight= count_number(j, q, previous_row, i+1)/2,
                            color = 'green'                                                       
                        )                    
                m.add_children(Trip)
        file_temp=dir_path+'flow_{}.png'.format(Tim-1)
        filename='flow_{}.html'.format(Tim-1)
        pngname='flow_{}.png'.format(Tim-1)
        save_map(m,filename,pngname)    
        files.append(file_temp)
        previous_row = i+1               
'''Trip_data'''       
