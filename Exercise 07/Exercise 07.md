# Exercise 07 Problem 3.12
## 问题
![](https://github.com/lopo70/Computational_Physics_N2015301020170/blob/master/Exercise%2007/e.png)
## 解题思路
这道题首先要求做出非线性摆在驱动力FD=1.2时的ω-θ图，然后在相位图中取出那些与驱动力同相位的时间点，即庞加莱截面图。
根据Euler-cromer方法，用ωi+1的值来计算θi+1的值，计算公式如下所示
<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=\omega&space;_{i&plus;1}=\omega&space;_{i}-\left&space;[&space;\frac{g}{l}sin(\theta&space;)&plus;q\cdot&space;\omega&space;_{i}-F_{D}sin(\Omega_{D}t_{i}&space;)\right&space;]\Delta&space;t" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\omega&space;_{i&plus;1}=\omega&space;_{i}-\left&space;[&space;\frac{g}{l}sin(\theta&space;)&plus;q\cdot&space;\omega&space;_{i}-F_{D}sin(\Omega_{D}t_{i}&space;)\right&space;]\Delta&space;t" title="\omega _{i+1}=\omega _{i}-\left [ \frac{g}{l}sin(\theta )+q\cdot \omega _{i}-F_{D}sin(\Omega_{D}t_{i} )\right ]\Delta t" /></a>

<a href="http://www.codecogs.com/eqnedit.php?latex=\theta&space;_{i&plus;1}=\theta&space;_{i}&plus;\omega&space;_{i&plus;1}\Delta&space;t" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\theta&space;_{i&plus;1}=\theta&space;_{i}&plus;\omega&space;_{i&plus;1}\Delta&space;t" title="\theta _{i+1}=\theta _{i}+\omega _{i+1}\Delta t" /></a>

<a href="http://www.codecogs.com/eqnedit.php?latex=t&space;_{i&plus;1}=t&space;_{i}&plus;\Delta&space;t" target="_blank"><img src="http://latex.codecogs.com/gif.latex?t&space;_{i&plus;1}=t&space;_{i}&plus;\Delta&space;t" title="t _{i+1}=t _{i}+\Delta t" /></a>

<div align=left>其中取值为：g=l=9.8，FD=1.2，q=0.5，ΩD=2/3，取步长Δt=0.01，θ设定为取任意输入值，ω初值为0
由于题目要求建立庞加莱截面图，时间的取值要满足<a href="http://www.codecogs.com/eqnedit.php?latex=t\approx&space;\frac{2\pi&space;n}{\Omega&space;_{D}}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?t\approx&space;\frac{2\pi&space;n}{\Omega&space;_{D}}" title="t\approx \frac{2\pi n}{\Omega _{D}}" /></a>，这个取值可以由以下取值范围决定
<div align=center>

<a href="http://www.codecogs.com/eqnedit.php?latex=\left&space;|&space;t-\frac{2n\pi&space;}{\Omega&space;_{D}}&space;\right&space;|<&space;\frac{\Delta&space;t}{2}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\left&space;|&space;t-\frac{2n\pi&space;}{\Omega&space;_{D}}&space;\right&space;|<&space;\frac{\Delta&space;t}{2}" title="\left | t-\frac{2n\pi }{\Omega _{D}} \right |< \frac{\Delta t}{2}" /></a>
<div align=left>

## 代码实现
代码主循环用时间取值小于1000来实现
```python
while t<10000:
    ω=ω-(math.sin(math.radians(θ))+q*ω-FD*math.sin(ΩD*t))*Δt
    θ=θ+ω*Δt
``` 
为了使θ的值总是处于（-3.14，3.14）之间，需要角度超过范围后加减360°
```python
if -math.pi>math.radians(θ):
        θ=θ+360
    if math.pi<math.radians(θ):
        θ=θ-360
``` 
而判断时间与驱动力同向的代码可以用一个正整数循环来实现
```python
while n in range(0,65535):
        if -0.005<(t-2*math.pi*n/ΩD) and (t-2*math.pi*n/ΩD)<0.005:
            xlist1.append(math.radians(θ1))
            ylist1.append(ω1)
        n=n+1
``` 
可见只有满足时间条件的ω值会被加入y轴序列之中
最后，绘制出相应的ω-θ图以及庞加莱截面图即可。

## 结果分析
将摆从0，2rad的位置释放

### FD=0.5时的ω-θ图像
<div align=center>

![](https://github.com/lopo70/Computational_Physics_N2015301020170/blob/master/Exercise%2007/3.png)
<div align=left>

### FD=1.2时的ω-θ图像
<div align=center>

![](https://github.com/lopo70/Computational_Physics_N2015301020170/blob/master/Exercise%2007/4.png)
<div align=left>
上面的相图任然较复杂，为进一步看到混沌运动的内禀特征，我们只取驱动力周期的整数倍时刻去观察摆的运动，把这些时刻的相画在相图上，得到所谓的庞加莱截面。

### FD=1.2时的庞加莱截面图
<div align=center>

![](https://github.com/lopo70/Computational_Physics_N2015301020170/blob/master/Exercise%2007/2.png)
