# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 21:30:27 2021

@author: USER
"""
a=list(input("輸入一整數序列為:").split(" "))
h=len(a)/2
an=""
c=0
c1=0
for i in range(0,len(a)):
    for j in range(0,len(a)):
        if a[i]==a[j]:
            c+=1
        if c>h:
            an=a[i]
    c=0   
if an!="":
    print("過半元素為:"+an)
else:
    print("過半元素為:NO")


