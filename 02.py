# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 19:53:05 2021

@author: USER
"""
n=int(input("請輸入一個度數(正整數):"))
a=0
b=0
if n<=120:
    a=n*2.1
    b=a
elif n<=330:
    a=120*2.1+(n-120)*3.02
    b=120*2.1+(n-120)*2.68
elif n<=500:
    a=120*2.1+(330-120)*3.02+(n-330)*4.39
    b=120*2.1+(330-120)*2.68+(n-330)*3.61
elif n<=700:
    a=120*2.1+(330-120)*3.02+(500-330)*4.39+(n-500)*4.97
    b=120*2.1+(330-120)*2.68+(500-330)*3.61+(n-500)*4.01
elif n>700:
    a=120*2.1+(330-120)*3.02+(500-330)*4.39+(700-500)*4.97+(n-700)*5.63
    b=120*2.1+(330-120)*2.68+(500-330)*3.61+(700-500)*4.01+(n-700)*4.5
print("Summer months:"+str(a))
print("Non-Summer months:"+str(b))
