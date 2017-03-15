#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 16:24:52 2017

@author: wangtianpei
"""
import xlrd
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
   
import os             
import folium
#from folium import plugins
from folium.plugins import PolyLineTextPath
from folium.features import (
    ClickForMarker, CustomIcon, DivIcon, GeoJson, LatLngPopup, CircleMarker,
    MarkerCluster, PolyLine, Vega, RegularPolygonMarker,
    TopoJson, WmsTileLayer
)
m = folium.Map(
 location=[41.900321,-87.633446],
    zoom_start=11,
    tiles='openstreetmap'
)
for i in range(sheet.nrows-1):
    list_node = [[0 for x in range(2)] for y in range(len(s[i].split(', ')))]
    for j in range(len(s[i].split(', '))):
        list_node[j][1] = float(k[i][j].split(' ')[0])
        list_node[j][0] = float(k[i][j].split(' ')[1]) 
    census_tract = folium.PolyLine(
            list_node,
            weight=3,
            color = 'green'
            )
    m.add_children(census_tract)
    
color_list = ['#ffffff','#ffe6e6','#ffcccc','#ffb3b3','#ff9999','#ff8080','	#ff6666'
              ,'#ff4d4d','#ff3333','#ff1a1a','#ff0000','#e60000','#cc0000','#b30000'
              ,'#990000','#800000','#660000','#4d0000','#330000','#1a0000','#000000'
              ,'#000000','#000000','#000000','#000000']

Area_8=folium.CircleMarker(
    location=[41.900321,-87.633446],
    radius=500,
    popup='Near North Side',
    color='red',
    fill_color = 'red'
)
m.add_children(Area_8)

Area_7=folium.CircleMarker(
    location=[41.921613,-87.651142],
    popup='Lincoln Park',
    radius=500,
    color='orange',
    fill_color = 'orange'
)
m.add_children(Area_7)
Area_32=folium.CircleMarker(
    location=[41.878865584,-87.625192142],
    popup='Loop',
     radius=500,
    color='green',
    fill_color = 'green'
)
m.add_children(Area_32)
Area_6=folium.CircleMarker(
    location=[41.943985, -87.658228],
    popup='Lake View',
    radius=500,
    color='black',
    fill_color = 'black'
)
m.add_children(Area_6)
Area_28=folium.CircleMarker(
    location=[41.881290, -87.663019],
    popup='Near West Side',
    radius=500,
    color='blue',
    fill_color = 'blue'
)
m.add_children(Area_28)


list_1 = [[41.900321,-87.633446],
    [41.900321,-87.633446]]
Trip_8_8 = folium.PolyLine(
    list_1,
    weight=20
)
m.add_children(Trip_8_8)

'''
list_2 = [[41.900321,-87.633446],
    [41.878865584,-87.625192142]]'''
list1=[]
list2=[] 
for i in range(26): 
    list1.append(i)
    list2.append(i)
for i in range(26): 
    list1[i]=41.878865584+i*0.000858216
    list2[i]=(-87.627192142)+i*0.000858216*(-0.384698)
for i in range(25):
    List_2 = [[list1[i],list2[i]],[list1[i+1],list2[i+1]]]
    Trip_8_32 = folium.PolyLine(
            List_2,
            weight=13.5,
            color = color_list[i]
            )
    m.add_children(Trip_8_32)



list_3 = [[41.878865584,-87.623192142],
    [41.900321,-87.631446]]
Trip_32_8 = folium.PolyLine(
    list_3,
    weight=13.5
)
m.add_children(Trip_32_8)

list_4 = [[41.878865584,-87.625192142],
    [41.878865584,-87.625192142]]
Trip_32_32 = folium.PolyLine(
    list_4,
    weight=8.6
)
m.add_children(Trip_32_32)

list_5 = [[41.898321,-87.633446],
    [41.879290, -87.663019]]
Trip_8_28 = folium.PolyLine(
    list_5,
    weight=5.8
)
m.add_children(Trip_8_28)

list_6 = [[41.876865584,-87.625192142],
    [41.879290, -87.663019]]
Trip_32_28 = folium.PolyLine(
    list_6,
    weight=5.4
)
m.add_children(Trip_32_28)

list_7 = [[41.881290, -87.663019],
    [41.900321,-87.633446]]
Trip_28_8 = folium.PolyLine(
    list_7,
    weight=4.9
)
m.add_children(Trip_28_8)

list_8 = [[41.901321,-87.632446],
    [41.922613,-87.650142]]
Trip_8_7 = folium.PolyLine(
    list_8,
    weight=4
)
m.add_children(Trip_8_7)

list_9 = [[41.881290, -87.663019],
    [41.878865584,-87.625192142]]
Trip_28_32 = folium.PolyLine(
    list_9,
    weight=4
)
m.add_children(Trip_28_32)

list_10 = [[41.943985, -87.658228],
    [41.943985, -87.658228]]
Trip_6_6 = folium.PolyLine(
    list_10,
    weight=3
)
m.add_children(Trip_6_6)

list_11 = [[41.921613,-87.651142],
    [41.900321,-87.633446]]
Trip_7_8 = folium.PolyLine(
    list_11,
    weight=2.7
)
m.add_children(Trip_7_8)

list_12 = [[41.900321,-87.630446],
    [41.943985, -87.658228]]
Trip_8_6 = folium.PolyLine(
    list_12,
    weight=2.7
)
m.add_children(Trip_8_6)

list_13 = [[41.900321,-87.633446],
    [41.912431869,-87.670189148]]
Trip_8_24 = folium.PolyLine(
    list_13,
    weight=2.7
)
m.add_children(Trip_8_24)

list_14 = [[41.881290, -87.663019],
    [41.881290, -87.663019]]
Trip_28_28 = folium.PolyLine(
    list_14,
    weight=2.2
)
m.add_children(Trip_28_28)

list_15 = [[41.921613,-87.651142],
    [41.921613,-87.651142]]
Trip_7_7 = folium.PolyLine(
    list_15,
    weight=1.8
)
m.add_children(Trip_7_7)

m.save('Chicago.html') 
