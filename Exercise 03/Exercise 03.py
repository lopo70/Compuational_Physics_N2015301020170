# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 12:33:41 2017

@author: 王飞虎
"""
import os
import time
w1=["#   #   #   #   # #####   ##### ##### # #   # #   #"]
w2=["#   #  # #  #   # #   #   #     #     # #   # #   #"]
w3=["#   # #   # ##  # #       #     #     # #   # #   #"]
w4=["#   # ##### # # # #       ####  ####  # ##### #   #"]
w5=["#   # #   # #  ## # ###   #     #     # #   # #   #"]
w6=["# # # #   # #   # #   #   #     #     # #   # #   #"]
w7=[" # #  #   # #   # #####   #     ##### # #   # #####"]
 
t=0
while t<30:
    i = os.system('cls')
    for i1 in w1:
        print(i1,end='')
    print("\n")
    for i2 in w2:
        print(i2,end='')
    print("\n")
    for i3 in w3:
        print(i3,end='')
    print("\n")
    for i4 in w4:
        print(i4,end='')
    print("\n")
    for i5 in w5:
        print(i5,end='')
    print("\n")
    for i6 in w6:
        print(i6,end='')
    print("\n")
    for i7 in w7:
        print(i7,end='')
    print("\n")
    for j in (w1,w2,w3,w4,w5,w6,w7):
        j.insert(0," ")
        
    time.sleep(0.2)
    t+=1
    print(" ")