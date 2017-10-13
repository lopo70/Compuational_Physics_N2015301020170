# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 11:23:21 2017

@author: 王飞虎
"""

import matplotlib.pyplot as plt
import numpy as py
import math

x=0
y=0
f=[0]
z=[0]
v=float(input("请输入初始速度："))
t=0.00001 
angel=float(input("请输入初射角度："))
vx=v*math.cos(math.radians(angel))
vy=v*math.sin(math.radians(angel))
a=4*10**-5
vw=-2.78
d="炮弹落点距离="
while y>=0:
    v=py.sqrt(vx**2+vy**2)
    vx=vx-a*(vx-vw)*py.sqrt(v**2+vw**2-2*v*vw*vy/v)*t
    vy=vy-9.8*t-a*vy*py.sqrt(v**2+vw**2-2*v*vw*vy/v)*t
    x1=x
    y1=y
    x=x+vx*t
    y=y+vy*t
    b=-y1/y
    t=t+0.00001
    f.append(x)
    z.append(y)
    l=(x+b*x1)/(b+1)
    print(x,y)
print(d,l)

plt.figure(figsize=(10,5))
plt.plot(f,z,label="$Canon Shell Trajectory$",marker='.',color='red')
plt.xlabel("X/m")
plt.ylabel("Y/m")
plt.title("Canon Shell Trajectory")
plt.ylim(0,10000)
plt.legend()
plt.show()