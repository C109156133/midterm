# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 23:48:04 2021

@author: USER
"""
s=list(input("輸入N及M為:").split(" "))
a=[]
an=""
for i in range(0,int(s[0])):
    a.append(input("輸入矩陣數值第"+str(i+1)+"列數值為:").split(" "))
for i in range(0,int(s[1])):
    for j in range(0,int(s[0])):
        an=an+" "+str(a[j][i])
    print("輸出矩陣數值第"+str(i+1)+"列數值為:"+an)
    an=""
