# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 19:56:42 2021

@author: USER
"""
i=list(input("輸入值為:").split(","))
ch=0
mx=""
mn=""
for n in range(0,len(i)):
    for j in range(0,len(i)-n-1):
        if i[j]>i[j+1]:
            ch=i[j]
            i[j]=i[j+1]
            i[j+1]=ch
for n in range(len(i)-1,-1,-1):
    mx=mx+i[n]
    mn=mn+i[len(i)-n-1]
print("最大值數列與最小值數列差值為:"+str(int(mx)-int(mn)))
