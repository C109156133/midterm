# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 20:24:58 2021

@author: USER
"""
a=list(input("輸月及日為:").split(" "))
b=["Aquarius","Pisces","Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio","Sagittarius","Capricorn"]
if int(a[0])==1:
    if int(a[1])>=21 and int(a[1])<=31:
        print(b[0])
    elif int(a[1])>0 and int(a[1])<21:
        print(b[11])
    else:
        print("None")
elif int(a[0])==2:
    if int(a[1])>=19 and int(a[1])<=28:
        print(b[1])
    elif int(a[1])>0 and int(a[1])<19:
        print(b[0])
    else:
        print("None")
elif int(a[0])==3:
    if int(a[1])>=21 and int(a[1])<=31:
        print(b[2])
    elif int(a[1])>0 and int(a[1])<21:
        print(b[1])
    else:
        print("None")
elif int(a[0])==4:
    if int(a[1])>=21 and int(a[1])<=30:
        print(b[3])
    elif int(a[1])>0 and int(a[1])<21:
        print(b[2])
    else:
        print("None")
elif int(a[0])==5:
    if int(a[1])>=22 and int(a[1])<=31:
        print(b[4])
    elif int(a[1])>0 and int(a[1])<22:
        print(b[3])
    else:
        print("None")
elif int(a[0])==6:
    if int(a[1])>=22 and int(a[1])<=30:
        print(b[5])
    elif int(a[1])>0 and int(a[1])<22:
        print(b[4])
    else:
        print("None")
elif int(a[0])==7:
    if int(a[1])>=23 and int(a[1])<=31:
        print(b[6])
    elif int(a[1])>0 and int(a[1])<23:
        print(b[5])
    else:
        print("None")
elif int(a[0])==8:
    if int(a[1])>=24 and int(a[1])<=31:
        print(b[7])
    elif int(a[1])>0 and int(a[1])<24:
        print(b[6])
    else:
        print("None")
elif int(a[0])==9:
    if int(a[1])>=24 and int(a[1])<=30:
        print(b[8])
    elif int(a[1])>0 and int(a[1])<24:
        print(b[7])
    else:
        print("None")
elif int(a[0])==10:
    if int(a[1])>=24 and int(a[1])<=31:
        print(b[9])
    elif int(a[1])>0 and int(a[1])<24:
        print(b[8])
    else:
        print("None")
elif int(a[0])==11:
    if int(a[1])>=23 and int(a[1])<=30:
        print(b[10])
    elif int(a[1])>0 and int(a[1])<23:
        print(b[9])
    else:
        print("None")
elif int(a[0])==12:
    if int(a[1])>=22 and int(a[1])<=31:
        print(b[11])
    elif int(a[1])>0 and int(a[1])<22:
        print(b[10])
    else:
        print("None")
