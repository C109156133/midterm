# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 19:56:19 2021

@author: USER
"""
m=int(input("輸入階乘值M:"))
a=1
n=1
while (a<m):    
    a*=n        
    n+=1
print("超過M為"+str(m)+"的最小階層N值為:"+str(n-1))
