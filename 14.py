# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 23:22:32 2021

@author: USER
"""
a=list(input("輸入一字串為:"))
b=""
for i in range(0,len(a)):
    if a[i]==" ":
        a[i]=""
    b+=a[i]
print("There are "+str(len(b))+" characters")