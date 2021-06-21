# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 19:41:29 2021

@author: USER
"""

s=input("檢測的字串(end結束):")
f=input("檢測的單一字元:")
if s=="end":
    print("檢測結束")
else:
    ss=list(s)
    c=0
    for i in range(0,len(ss)):
        if ss[i]==f:
            c+=1
    print("字元"+f+"出現數為:"+str(c))
