# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 16:19:31 2020

@author: cojs2018
"""

import pandas as pd
import numpy as np
from datetime import date

def write2form(df, dt, setID, date_format="%Y-%m-%d"):
    """
    Function writes to fills out a html form using data from a given dataframe.
    
    Input: df, dataframe
           dt, date
           setID, string
           date_format, user selected date format string (optional)
    
    Returns: none
    """
    try:
        
        html = open(setID + dt.strftime(date_format.replace("-", "").replace("/", "").replace(".", "")) + ".html", "w")
        
        html.write('<html>\n<head>\n</head>\n<body>')
        html.write('\n\t<table id="setData" style="width:100%">\n\t\t<tr>')
        html.write('\n\t\t\t<th> Set </th>')
        html.write('\n\t\t\t<th> Class </th>')
        html.write('\n\t\t\t<th> Date </th>')
        html.write('\n\t\t\t<th> Number of Participants </th>')
        html.write('\n\t\t</tr>\n\t\t<tr>')
        html.write('\n\t\t\t<td> ' + setID + ' </td>')
        html.write('\n\t\t\t<td> ' + df.Gender[df.index[0]] + ' </td>')
        html.write('\n\t\t\t<td> ' + dt.strftime(date_format) + ' </td>')
        html.write('\n\t\t\t<td> ' + str(df.shape[0]) + ' </td>')
        html.write('\n\t\t</tr>\n\t</table>\n')
        html.write('\n\t<svg width="1124" height="1124">')
        
        #In this SVG write in the matches
        y = 0
        for i in range(df.shape[0]):
            html.write('\n\t\t\t<g>')
            html.write('\n\t\t\t\t<rect x="0" y="' + str(y) + '" width="300" height="100" style="fill:rgb(255,255,255);stroke-width:3;stroke:rgb(0,0,0)" />')
            html.write('\n\t\t\t\t"<text id="txt0" x="150" y="' + str(50+y) + '" dominant-baseline="middle" text-anchor = "middle" fill="black">' + str(df.Participant_Number[df.index[i]]))
            html.write('\n\t\t\t\t\t<tspan>' + df.Belt[df.index[i]] + '</tspan>\n\t\t\t\t</text>')
            html.write('\n\t\t\t</g>')
            html.write('\n\t\t<path d="M 300 ' + str(50+y) + ' l 50 0 l 0 ' + str(60 * pow(-1,i)) + ' l 50 ' + str(90 * pow(-1,np.floor(i/2))) +' " stroke="rgb(0,0,0)" stroke-width="3" fill="none" />')
            if i % 2 == 0:
                y += 120
            else:
                y += 180
            
        
        #write in paths and remaining matches
        y = 150
        for i in range(int(np.ceil(df.shape[0] / 2))):
            html.write('\n\t\t\t<rect x="400" y="' + str(y) + '" width="300" height="100" style="fill:rgb(255,255,255);stroke-width:3;stroke:rgb(0,0,0)" />')
            html.write('\n\t\t\t<path d="M 700 ' + str(50+y) + ' l 50 0 l 0 ' + str(60 * pow(-1,i)) + ' l 50 ' + str(240 * pow(-1,np.floor(i/2))) + ' " stroke="rgb(0,0,0)" stroke-width="3" fill="none" />')
            if i % 2 == 0:
                y += 120
            else:
                y += 480
                
        html.write('\n\t\t\t<rect x="800" y="450" width="300" height="100" style="fill:rgb(255,255,255);stroke-width:3;stroke:rgb(0,0,0)" />')
        html.write('\n\t\t\t<rect x="800" y="570" width="300" height="100" style="fill:rgb(255,255,255);stroke-width:3;stroke:rgb(0,0,0)" />')
        
        html.write('\n\t</svg>')
        
        html.write('\n\t<table id="podium" style="width:100%">')
        html.write('\n\t\t<th> Rank </th>\n\t\t<th> ID </th>\n\t\t<th> Points Total </th>\n\t</tr>')
        html.write('\n\t<tr>\n\t\t<td> 1st </td>\n\t</tr>')
        html.write('\n\t<tr>\n\t\t<td> 2nd </td>\n\t</tr>')
        html.write('\n\t<tr>\n\t\t<td> 3rd </td>\n\t</tr>')
        
        html.write('\n\t</table>\n</body>\n</html>')
        html.close()
    except Exception as exe:
        print("ERROR[" + setID  + "]: Unable to write to file! Please check input parameters")
        print(type(exe))
        print(exe.args)
        print(exe)
        
        
participants = pd.read_csv('result.csv', sep=',')
sets = participants.Set.unique()

for s in sets:
    dt = date.today()
    df = participants[participants.Set == s]
    write2form(df, dt, s)