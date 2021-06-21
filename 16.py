# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 00:38:52 2021

@author: USER
"""
#16
a=list(input().split(" "))
a1=[]
for i in range(0,int(a[0])):
    a1.append(input().split(" "))
b=list(input().split(" "))
b1=[]
for i in range(0,int(b[0])):
    b1.append(input().split(" "))
an=[list(range(int(a[1]))) for _ in range(int(a[0]))] 
ans=""
if a!=b:
    print("兩個矩陣無法相加")
else:
    for i in range(0,int(a[0])):
        for j in range(0,int(a[1])):
            an[i][j]=str(int(a1[i][j])+int(b1[i][j]))
            ans=ans+str(an[i][j])+" "
        print(ans)
        ans=""
