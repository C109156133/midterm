# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 00:28:20 2021

@author: USER
"""
a=list(input("輸入一字元為:"))
b=""
b1="1"*len(a)
for i in range(0,len(a)):
    if a[i]==a[len(a)-1-i]:
        b+="1"
    else:
        b+="0"
if b==b1:
    print("YES")
else:
    print("NO")
    
