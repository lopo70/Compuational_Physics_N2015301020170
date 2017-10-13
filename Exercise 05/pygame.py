# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 13:16:40 2017

@author: 王飞虎
"""
background_image_filename = 'bg.jpg'

import numpy as py
import math
import pygame
import matplotlib.pyplot as plt
from pygame.locals import *
from sys import exit
x=0
y=0
f=[0]
z=[0]
v=float(input("请输入初始速度："))
t=0.00001 
angel=45
vx=v*math.cos(math.radians(angel))
vy=v*math.sin(math.radians(angel))
a=4*10**-5
vw=-2.78


pygame.init()
 
screen = pygame.display.set_mode((500, 313), 0, 32)
pygame.display.set_caption("Canon Shell ATTACK")
background = pygame.image.load(background_image_filename).convert()
cannon = pygame.draw.polygon(pygame.surface, (255,0,0), [(310,10),(305, 10),(305,20),(310,20),(307.5, 25)])
while True:
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
   
    if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    angel=angel+1
                elif event.key == pygame.K_DOWN:
                    angel=angel-1
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


plt.figure(figsize=(10,5))
plt.plot(f,z,label="$Canon Shell Trajectory$",marker='.',color='red')
plt.xlabel("X/m")
plt.ylabel("Y/m")
plt.title("Canon Shell Trajectory")
plt.ylim(0,10000)
plt.legend()
plt.show()
