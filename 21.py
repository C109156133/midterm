# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 17:09:22 2021

@author: USER
"""
data=[["123","456","9000"],["456","789","5000"],["789","888","6000"],["336","558","10000"],["775","666","12000"],["566","221","7000"]]
n=int(input("輸入查詢組數N為:"))
f=[]
x=""
for i in range(0,n):
    f.append(input().split(" "))
for i in range(0,n):
    for j in range(0,len(data)):
        if f[i][0]==data[j][0] and f[i][1]==data[j][1]:
            print(data[j][2])
            break
        else:
            x+="x"
    if x>="x"*len(data):
        print("error")
    x=""
    
