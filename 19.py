# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 16:33:51 2021

@author: USER
"""

a=int(input("組數為:"))
b=[]
an=0
for i in range(0,a):
    b.append(input("第"+str(i+1)+"組:").split(" "))
for i in range(0,a):
    an=int(b[i][0])*250+int(b[i][1])*175
    print("第"+str(i+1)+"組應付費用為:"+str(an))