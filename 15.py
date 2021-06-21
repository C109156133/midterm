# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 23:34:39 2021

@author: USER
"""
a=list(input("輸入一組四位數字為:"))
c=0
for i in range(0,4):
    a[i]=str((int(a[i])+7)%10)
c=a[0]
a[0]=a[2]
a[2]=c
c=a[1]
a[1]=a[3]
a[3]=c
print("輸出加密後的數字為:"+a[0]+a[1]+a[2]+a[3])

    