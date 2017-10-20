# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 14:05:04 2017

@author: 王飞虎
"""

import matplotlib.pyplot as plt
import numpy as py
import math

y=float(input("请输入初始高度："))
x=0
z=0
xlist=[x]
ylist=[y]
zlist=[z]
angel=float(input("请输入初射角度："))
w=float(input("请输入自旋角速度："))
v=float(input("请输入初始速度："))
d="轨迹横向偏转="
t=0.001
vx=v*math.cos(math.radians(angel))
vy=v*math.sin(math.radians(angel))
vz=0
S=4.1*10**-4
n=0
xend=18.288
while y>=0 and x<=xend:
    v=py.sqrt(vx**2+vy**2+vz**2)
    x=x+vx*t
    y=y+vy*t
    z=z+vz*t 
    vz=vz+S*vx*w*t
    vx=vx-(0.0039+0.0058/(1+py.exp(v-35/5)))*v*vx*t
    vy=vy-9.8*t
    xlist.append(x)
    ylist.append(y)
    zlist.append(z)
    n=n+1
if y<0:
    r=ylist[n-1]/(ylist[n-1]-ylist[n])
    xlist[n]=xlist[n-1]+(xlist[n]-xlist[n-1])*r
    ylist[n]=0
    zlist[n]=zlist[n-1]+(zlist[n]-zlist[n-1])*r
if x>=xend:
    r=(xend-xlist[n-1])/(xlist[n-1]-xlist[n])
    ylist[n]=ylist[n-1]-(ylist[n-1]-ylist[n])*r
    zlist[n]=zlist[n-1]+(zlist[n]-zlist[n-1])*r
    xlist[n]=xend
print(d,zlist[n])
    

plt.figure(figsize=(10,5))
plt.plot(xlist,ylist,label='x-y plain',color='red')
plt.xlabel("X/m")
plt.ylabel("Z,Y/m")
plt.plot(xlist,zlist,label='z deflection',color='blue')
plt.legend(loc='best')
plt.title("Curve Ball Trajectory")
plt.show()

ax=plt.subplot(111,projection='3d')
ax.scatter(xlist,zlist,ylist,c='b')
ax.set_zlabel('Y')
ax.set_ylabel('Z')
ax.set_xlabel('X')