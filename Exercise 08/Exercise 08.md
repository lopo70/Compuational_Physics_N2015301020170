# Exercise 08 Problem 3.20
## 问题
![](https://github.com/lopo70/Computational_Physics_N2015301020170/blob/master/Exercise%2008/%E6%8D%95%E8%8E%B7.PNG)
## 解题思路
题目要求绘出F_D在(1.35,1.5)之间的bifurcation diagram，所谓的分叉图。摆运动的计算与上一节相同，用Euler-Cromer方法，用ωi+1的值来计算θi+1的值，计算公式如下
<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=\omega&space;_{i&plus;1}=\omega&space;_{i}-\left&space;[&space;\frac{g}{l}sin(\theta&space;)&plus;q\cdot&space;\omega&space;_{i}-F_{D}sin(\Omega_{D}t_{i}&space;)\right&space;]\Delta&space;t" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\omega&space;_{i&plus;1}=\omega&space;_{i}-\left&space;[&space;\frac{g}{l}sin(\theta&space;)&plus;q\cdot&space;\omega&space;_{i}-F_{D}sin(\Omega_{D}t_{i}&space;)\right&space;]\Delta&space;t" title="\omega _{i+1}=\omega _{i}-\left [ \frac{g}{l}sin(\theta )+q\cdot \omega _{i}-F_{D}sin(\Omega_{D}t_{i} )\right ]\Delta t" /></a>

<a href="http://www.codecogs.com/eqnedit.php?latex=\theta&space;_{i&plus;1}=\theta&space;_{i}&plus;\omega&space;_{i&plus;1}\Delta&space;t" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\theta&space;_{i&plus;1}=\theta&space;_{i}&plus;\omega&space;_{i&plus;1}\Delta&space;t" title="\theta _{i+1}=\theta _{i}+\omega _{i+1}\Delta t" /></a>

<a href="http://www.codecogs.com/eqnedit.php?latex=t&space;_{i&plus;1}=t&space;_{i}&plus;\Delta&space;t" target="_blank"><img src="http://latex.codecogs.com/gif.latex?t&space;_{i&plus;1}=t&space;_{i}&plus;\Delta&space;t" title="t _{i+1}=t _{i}+\Delta t" /></a>

<div align=left>其中取值为：g=l=9.8，q=0.5，ΩD=2/3，θ=0.2，取步长Δt=0.01，ω初值为0。
题目要求绘制分叉图，即θ-F_D图，与正常不同的是选取的点都是时间与驱动力同相的点，即时间取值要满足<a href="http://www.codecogs.com/eqnedit.php?latex=t\approx&space;\frac{2\pi&space;n}{\Omega&space;_{D}}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?t\approx&space;\frac{2\pi&space;n}{\Omega&space;_{D}}" title="t\approx \frac{2\pi n}{\Omega _{D}}" /></a>，这个取值可以由以下取值范围决定
<div align=center>

<a href="http://www.codecogs.com/eqnedit.php?latex=\left&space;|&space;t-\frac{2n\pi&space;}{\Omega&space;_{D}}&space;\right&space;|<&space;\frac{\Delta&space;t}{2}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\left&space;|&space;t-\frac{2n\pi&space;}{\Omega&space;_{D}}&space;\right&space;|<&space;\frac{\Delta&space;t}{2}" title="\left | t-\frac{2n\pi }{\Omega _{D}} \right |< \frac{\Delta t}{2}" /></a>
<div align=left>
注意到为了先使摆的运动趋于稳定，从第300个驱动力周期开始计数。

## 代码实现
程序主循环用F_D取值小于1.5来实现
```python
while F_D<1.52:
    ω=ω0
    θ=θ0
    t=0
    F_D=F_D+0.001
``` 
次循环用时间取值小于10000来实现
```python
while t<10000:
        ω=ω-((g/l)*math.sin(θ)+q*ω-F_D*math.sin(Ω_D*t))*dt
        θ=θ+ω*dt
        t=t+dt
``` 
为了使θ的值总是处于（-3.14，3.14）之间，需要角度超过范围后加减2π
```python
if θ>=math.pi:
    θ=θ-2*math.pi
elif θ<-math.pi:
    θ=θ+2*math.pi
``` 
而判断时间与驱动力同向的代码可以用一个正整数循环（且只计算时间在300到400个驱动力周期的点）来实现
```python
for n in range(300，400):
       if abs(t-math.pi*n*2/(Ω_D))<0.005:
               F_D_list.append(F_D)
               θ_list.append(θ)
``` 
可见只有满足时间条件的θ值会被加入y轴序列之中
最后，绘制出相应的θ-F_D图即bifurcation diagram即可。
## 结果分析
驱动力大小F_D在1.35至1.5之间的bifurcation diagram如下所示
<div align=center>

![](https://github.com/lopo70/Computational_Physics_N2015301020170/blob/master/Exercise%2008/result.png)
<div align=left>
从上图可以看出，F_D在1.5左右，θ的值出现了大幅度波动，归于“混沌”状态。
由于F_D在1.48左右数据点较密，无法分辨，所以在此处放大的bifurcation diagram如下
<div align=center>

![](https://github.com/lopo70/Computational_Physics_N2015301020170/blob/master/Exercise%2008/result2.png)
<div align=left>
    
![源代码](https://raw.githubusercontent.com/lopo70/Computational_Physics_N2015301020170/master/Exercise%2008/2.py)
   


