# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 10:36:03 2017

@author: 王飞虎
"""

import math
import matplotlib.pyplot as plt

F_D=1.35
q=1/2
l=9.8
g=9.8
Ω_D=2/3
dt=0.01
θ0=0.2
ω0=0
ω=ω0
θ=θ0
t=0
F_D_list=[]
θ_list=[]

while F_D<1.5:
    ω=ω0
    θ=θ0
    t=0
    while t<10000:
        ω=ω-((g/l)*math.sin(θ)+q*ω-F_D*math.sin(Ω_D*t))*dt
        θ=θ+ω*dt
    
        if θ>=math.pi:
            θ=θ-2*math.pi
        elif θ<-math.pi:
            θ=θ+2*math.pi
        t=t+dt
        for n in range(300,400):
            if abs(t-math.pi*n*2/(Ω_D))<0.005:
                F_D_list.append(F_D)
                θ_list.append(θ)
    F_D=F_D+0.001

print(θ_list)

plt.figure(figsize=(12,12))
plt.title('bifrcation diagram')
plt.xlabel('F_D')
plt.ylabel('θ(rad)')
plt.plot(F_D_list,θ_list,'.',color='black')
plt.show()
