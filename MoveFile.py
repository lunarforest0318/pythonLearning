# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 15:28:05 2018

@author: rayyu
"""

import os
import shutil
import xlrd
import zipfile
import pandas


df = pandas.read_excel(r'C:\Users\rayyu\Desktop\Argus\Test.xlsx')

keys = df['Name'].values
values = df['Path'].values

d={}

p = zip(keys, values)

for key,value in p:
    d[key]=value    


for directory in values:
    if not os.path.exists(directory):
        os.makedirs(directory)


for filename,filepath in d.items():
    src = os.path.join(r'C:/Users/rayyu/Desktop/Argus/',filename)
    dst = os.path.join(filepath,filename)
    try:
        shutil.copy(src,dst)
    except:
        pass

