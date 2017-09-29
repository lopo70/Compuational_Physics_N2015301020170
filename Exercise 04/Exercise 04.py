# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 18:27:17 2017

@author: 王飞虎
"""
import matplotlib.pyplot as plt
import numpy as py
v = 0 
t = 0 
h = 0.1
d = "Terminal Velocity ="
f = [0]
z = [0]
m = [0]
print (t,v)
while v <= 10:
    b = v
    v = v + (10-v)*h
    t = t + h
    n = -10*py.exp(-t)+10
    f.append(t)
    z.append(v)
    m.append(n)
    print (t, v)
    if v == b:
        print (d,b,m)
        break
print (f)
print (z)
plt.plot(f,z)
plt.plot(f,m)