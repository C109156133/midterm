# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 19:57:47 2021

@author: USER
"""
i=list(input("輸入值為:").split(","))
an=int(i[0])
if int(i[0])==186:
    if an<(int(i[1])*0.09):
        an=int(i[1])*0.09
        if an<=int(i[0])*2:
            an*=0.9
        elif an>int(i[0])*2:
            an*=0.8
elif int(i[0])==386:
    if an<(int(i[1])*0.08):
        an=int(i[1])*0.08
        print(an)
        if an<=int(i[0])*2:
            an*=0.8
        elif an>(int(i[0])*2):
            an=int(an)*0.7
            print(an)
elif int(i[0])==586:
    if an<(int(i[1])*0.07):
        an=int(i[1])*0.07
        if an<=int(i[0])*2:
            an*=0.7
        elif an>int(i[0])*2:
            an*=0.6
elif int(i[0])==986:
    if an<(int(i[1])*0.06):
        an=int(i[1])*0.06
        if an<=int(i[0])*2:
            an*=0.6
        elif an>int(i[0])*2:
            an*=0.5
print(round(an))

