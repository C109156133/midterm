# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 16:47:17 2021

@author: USER
"""

data=[["123","Tom","DTGD"],["456","Cat","CSIE"],["789","Nana","ASIE"],["321","Lim","DBA"],["654","Won","FDD"]]
id=input("輸入查詢學號為:")
n=""
for i in range(0,len(data)):    
    if data[i][0]==id:
        print("學生資料為:"+data[i][0]+" "+data[i][1]+" "+data[i][2])
    else:
        n+="x"
    if n=="x"*len(data):
        print("學生資料為:無")
        



