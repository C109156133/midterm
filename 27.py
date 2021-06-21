# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 19:58:54 2021

@author: USER
"""

a=list(input("甲方的數字:"))
b=list(input("乙方的數字:"))
an=""
for i in range(len(a)):
    if a[i]==b[i]:
        an+="和"
    elif a[i]>b[i]:
        an+="贏"
    elif a[i]<b[i]:
        an+="輸"
print("洗刷刷結果:"+an)