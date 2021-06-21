# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 00:01:34 2021

@author: USER
"""
a=int(input("要測試的資料量:"))
a1=[]
for i in range(0,a):
    a1.append(input().split(" "))
for i in range(0,a):
    if a1[i][0]==a1[i][2] or a1[i][1]==a1[i][2]:
        print("YES")
    elif a1[i][0]!="AB" and a1[i][1]!="AB" and a1[i][2]=="O":
        print("YES")
    elif a1[i][0]=="AB" or a1[i][1]=="AB":
        if a1[i][2]=="A" or a1[i][2]=="B" or a1[i][2]=="AB":
            print("YES")
    elif (a1[i][0]=="A" and a1[i][1]=="B") or (a1[i][0]=="B" and a1[i][1]=="A"):
        if a1[i][2]=="AB":
            print("YES")
    else:
        print("IMPOSSIBLE")
        