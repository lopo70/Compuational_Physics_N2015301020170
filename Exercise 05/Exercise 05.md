# Exercise 05 Problem 2.11
## 解题思路
 题目要求计算改变初始速度以及考虑加入风速影响后炮弹落点的改变量。首先计算考虑空气阻力,不考虑空气密度变化的炮弹运动情况。使用欧勒法处理该问题，则炮弹的坐标以及速度的平行与垂直分量可以表示为

<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=x_{i&plus;1}=x_{i}&plus;v_{x,i}\Delta&space;t" target="_blank"><img src="http://latex.codecogs.com/gif.latex?x_{i&plus;1}=x_{i}&plus;v_{x,i}\Delta&space;t" title="x_{i+1}=x_{i}+v_{x,i}\Delta t" /></a>
 
<a href="http://www.codecogs.com/eqnedit.php?latex=y_{i&plus;1}=y_{i}&plus;v_{y,i}\Delta&space;t" target="_blank"><img src="http://latex.codecogs.com/gif.latex?y_{i&plus;1}=y_{i}&plus;v_{y,i}\Delta&space;t" title="y_{i+1}=y_{i}+v_{y,i}\Delta t" /></a>

<a href="http://www.codecogs.com/eqnedit.php?latex=v_{x,i&plus;1}=v_{x,i}-\frac{B_{2}vv_{x,i}}{m}\Delta&space;t" target="_blank"><img src="http://latex.codecogs.com/gif.latex?v_{x,i&plus;1}=v_{x,i}-\frac{B_{2}vv_{x,i}}{m}\Delta&space;t" title="v_{x,i+1}=v_{x,i}-\frac{B_{2}vv_{x,i}}{m}\Delta t" /></a>

<a href="http://www.codecogs.com/eqnedit.php?latex=v_{y,i&plus;1}=v_{y,i}-g\Delta&space;t-\frac{B_{2}vv_{y,i}}{m}\Delta&space;t" target="_blank"><img src="http://latex.codecogs.com/gif.latex?v_{y,i&plus;1}=v_{y,i}-g\Delta&space;t-\frac{B_{2}vv_{y,i}}{m}\Delta&space;t" title="v_{y,i+1}=v_{y,i}-g\Delta t-\frac{B_{2}vv_{y,i}}{m}\Delta t" /></a>

<a href="http://www.codecogs.com/eqnedit.php?latex=v=\sqrt{v_{x,i}^{2}&plus;v_{y,i}^{2}}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?v=\sqrt{v_{x,i}^{2}&plus;v_{y,i}^{2}}" title="v=\sqrt{v_{x,i}^{2}+v_{y,i}^{2}}" /></a>
<div align=left>
 
 设炮弹初速为700m/s，发射角度为45°，<a href="http://www.codecogs.com/eqnedit.php?latex=\inline&space;\frac{B_{2}}{m}=4\times&space;10^{-5}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\inline&space;\frac{B_{2}}{m}=4\times&space;10^{-5}" title="\frac{B_{2}}{m}=4\times 10^{-5}" /></a>，绘制炮弹轨迹曲线，记录y=0时的炮弹x坐标。然后按题目要求改变初速大小为707m/s，再次绘制轨迹曲线，得到炮弹落地时x坐标。
 y=0时的x坐标可用下式估算，其中<a href="http://www.codecogs.com/eqnedit.php?latex=\inline&space;r=-\frac{y_{n}}{y_{n&plus;1}}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\inline&space;r=-\frac{y_{n}}{y_{n&plus;1}}" title="r=-\frac{y_{n}}{y_{n+1}}" /></a>,<a href="http://www.codecogs.com/eqnedit.php?latex=\inline&space;y_{n}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\inline&space;y_{n}" title="y_{n}" /></a>大于0，<a href="http://www.codecogs.com/eqnedit.php?latex=\inline&space;y_{n&plus;1}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\inline&space;y_{n&plus;1}" title="y_{n+1}" /></a>小于0.
 
<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=x_{l}=\frac{x_{n}&plus;rx_{n&plus;1}}{r&plus;1}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?x_{l}=\frac{x_{n}&plus;rx_{n&plus;1}}{r&plus;1}" title="x_{l}=\frac{x_{n}+rx_{n+1}}{r+1}" /></a>
 <div align=left>
若考虑10km/s的水平风速，分成以下两种情况：1.风速与炮弹方向相同（tail wind）；2.风速与炮弹方向相反（head wind）。这时空气阻力可用下式表示
  
<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=F_{drag,x}=-B_{2}\left&space;|&space;\vec{v}-\vec_{v_{wind}}&space;\right&space;|\left&space;(&space;v_{x}-v_{wind}&space;\right&space;)" target="_blank"><img src="http://latex.codecogs.com/gif.latex?F_{drag,x}=-B_{2}\left&space;|&space;\vec{v}-\vec_{v_{wind}}&space;\right&space;|\left&space;(&space;v_{x}-v_{wind}&space;\right&space;)" title="F_{drag,x}=-B_{2}\left | \vec{v}-\vec_{v_{wind}} \right |\left ( v_{x}-v_{wind} \right )" /></a>
 
<a href="http://www.codecogs.com/eqnedit.php?latex=F_{drag,y}=-B_{2}\left&space;|&space;\vec{v}-\vec_{v_{wind}}&space;\right&space;|\left&space;v_{y}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?F_{drag,y}=-B_{2}\left&space;|&space;\vec{v}-\vec_{v_{wind}}&space;\right&space;|\left&space;v_{y}" title="F_{drag,y}=-B_{2}\left | \vec{v}-\vec_{v_{wind}} \right |\left v_{y}" /></a>
 <div align=left>
其中，

<a href="http://www.codecogs.com/eqnedit.php?latex=\inline&space;\left&space;|&space;\vec{v}-\vec_{v_{wind}}&space;\right&space;|\left=\sqrt{v^{2}&plus;v_{wind}^{2}-2vv_{wind}cos\theta&space;}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\inline&space;\left&space;|&space;\vec{v}-\vec_{v_{wind}}&space;\right&space;|\left=\sqrt{v^{2}&plus;v_{wind}^{2}-2vv_{wind}cos\theta&space;}" title="\left | \vec{v}-\vec_{v_{wind}} \right |\left=\sqrt{v^{2}+v_{wind}^{2}-2vv_{wind}cos\theta }" /></a>,cos\theta =\frac{v_{y,i}}{v}
 
## 代码思路
 ### 不考虑风速影响
 为了方便得出不同角度与初始风速对炮弹轨迹的影响，可用下列语句任意输入角度与初始速度
 ```python
    v=float(input("请输入初始速度："))
    angel=float(input("请输入初射角度："))
```
 递推公式的部分可以用while循环实现
```python
while y>=0:
    vx=vx-a*v*vx*t
    vy=vy-9.8*t-a*v*vy*t
    x=x+vx*t
    y=y+vy*t
```
为了计算炮弹落地距离，由公式<a href="http://www.codecogs.com/eqnedit.php?latex=x_{l}=\frac{x_{n}&plus;rx_{n&plus;1}}{r&plus;1}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?x_{l}=\frac{x_{n}&plus;rx_{n&plus;1}}{r&plus;1}" title="x_{l}=\frac{x_{n}+rx_{n+1}}{r+1}" /></a>可知，需要存储y小于0之前的y与x数据，代码如下
```python
    x1=x
    y1=y
    b=-y1/y
    l=(x+b*x1)/(b+1)
    print(l)
```
### 考虑风速的影响（vwind=10km/h）
考虑风速的作用，只需要在炮弹速度表达式中修改阻尼项即可
<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=v_{x,i&plus;1}=v_{x,i}-\frac{B_{2}\left&space;|&space;\vec{v}-\vec{v_{wind}}&space;\right&space;|\left&space;(&space;v_{x}-v_{wind}&space;\right&space;)}{m}\Delta&space;t" target="_blank"><img src="http://latex.codecogs.com/gif.latex?v_{x,i&plus;1}=v_{x,i}-\frac{B_{2}\left&space;|&space;\vec{v}-\vec{v_{wind}}&space;\right&space;|\left&space;(&space;v_{x}-v_{wind}&space;\right&space;)}{m}\Delta&space;t" title="v_{x,i+1}=v_{x,i}-\frac{B_{2}\left | \vec{v}-\vec{v_{wind}} \right |\left ( v_{x}-v_{wind} \right )}{m}\Delta t" /></a>

<a href="http://www.codecogs.com/eqnedit.php?latex=v_{y,i&plus;1}=v_{y,i}-\frac{B_{2}\left&space;|&space;\vec{v}-\vec{v_{wind}}&space;\right&space;|v_{y}}{m}\Delta&space;t" target="_blank"><img src="http://latex.codecogs.com/gif.latex?v_{y,i&plus;1}=v_{y,i}-\frac{B_{2}\left&space;|&space;\vec{v}-\vec{v_{wind}}&space;\right&space;|v_{y}}{m}\Delta&space;t" title="v_{y,i+1}=v_{y,i}-\frac{B_{2}\left | \vec{v}-\vec{v_{wind}} \right |v_{y}}{m}\Delta t" /></a>

<a href="http://www.codecogs.com/eqnedit.php?latex=\left&space;|&space;\vec{v}-\vec{v_{wind}}&space;\right&space;|=\sqrt{v^{2}&plus;v_{wind}^{2}-2vv_{wind}cos\alpha&space;}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\left&space;|&space;\vec{v}-\vec{v_{wind}}&space;\right&space;|=\sqrt{v^{2}&plus;v_{wind}^{2}-2vv_{wind}cos\alpha&space;}" title="\left | \vec{v}-\vec{v_{wind}} \right |=\sqrt{v^{2}+v_{wind}^{2}-2vv_{wind}cos\alpha }" /></a>
<div align=left>
这一部分代码只需修改相应的速度分量表达式即可。
 
## 结果分析
### 改变初始速度的影响
设定发射角度为45°，初速为700m，炮弹落点为L1=21691.737413m，轨迹如下所示

![](https://github.com/lopo70/Computational_Physics_N2015301020170/blob/master/Exercise%2005/1.png)

保持发射角度不变，初速为707m/s，炮弹落点为L2=21900.1204403m，轨迹如下所示

![](https://github.com/lopo70/Computational_Physics_N2015301020170/blob/master/Exercise%2005/2.png)

可见，改变初速百分之一后，炮弹落点距离
<a href="http://www.codecogs.com/eqnedit.php?latex=\Delta&space;L=208.4m" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\Delta&space;L=208.4m" title="\Delta L=208.4m" /></a>
### 加入风速的影响
设发射角度45°，炮弹初速为700m/s，水平风速为10km/h（tail wind），炮弹落点为L3=21782.3007858，轨迹如下所示

![](https://github.com/lopo70/Computational_Physics_N2015301020170/blob/master/Exercise%2005/3.png)

设发射角度45°，炮弹初速为700m/s，水平风速为10km/h（head wind），炮弹落点为L3=21588.0674307，轨迹如下所示

![](https://github.com/lopo70/Computational_Physics_N2015301020170/blob/master/Exercise%2005/4.png)

可见，加入10km/s的风速影响后，炮弹落点距离

<a href="http://www.codecogs.com/eqnedit.php?latex=\Delta&space;L(tail&space;wind)=90.6m" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\Delta&space;L(tail&space;wind)=90.6m" title="\Delta L(tail wind)=90.6m" /></a>

<a href="http://www.codecogs.com/eqnedit.php?latex=\Delta&space;L(hwad&space;wind)=-103.7m" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\Delta&space;L(hwad&space;wind)=-103.7m" title="\Delta L(hwad wind)=-103.7m" /></a>

从以上计算结果可以看出，即使稍微改变初始条件，也会对炮弹的轨迹以及落点产生可观的影响。

![源代码1](https://raw.githubusercontent.com/lopo70/Computational_Physics_N2015301020170/master/Exercise%2005/Exercise%20501.py)
![源代码2](https://raw.githubusercontent.com/lopo70/Computational_Physics_N2015301020170/master/Exercise%2005/Exercise%20502.py)

# 补充：用pygame做一个大炮小游戏
