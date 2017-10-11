# Exercise 05 Problem 2.11
## 解题思路
 题目要求计算改变初始速度以及考虑加入风速影响后炮弹落点的改变量。首先计算考虑空气阻力,不考虑空气密度的炮弹运动情况。使用欧勒法处理该问题，则炮弹的坐标以及速度的平行与垂直分量可以表示为

<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=x_{i&plus;1}=x_{i}&plus;v_{x,i}\Delta&space;t" target="_blank"><img src="http://latex.codecogs.com/gif.latex?x_{i&plus;1}=x_{i}&plus;v_{x,i}\Delta&space;t" title="x_{i+1}=x_{i}+v_{x,i}\Delta t" /></a>
 
<a href="http://www.codecogs.com/eqnedit.php?latex=y_{i&plus;1}=y_{i}&plus;v_{y,i}\Delta&space;t" target="_blank"><img src="http://latex.codecogs.com/gif.latex?y_{i&plus;1}=y_{i}&plus;v_{y,i}\Delta&space;t" title="y_{i+1}=y_{i}+v_{y,i}\Delta t" /></a>
 
<a href="http://www.codecogs.com/eqnedit.php?latex=v_{x,i&plus;1}=v_{x,i}-\frac{B_{2}vv_{x,i}}{m}\Delta&space;t" target="_blank"><img src="http://latex.codecogs.com/gif.latex?v_{x,i&plus;1}=v_{x,i}-\frac{B_{2}vv_{x,i}}{m}\Delta&space;t" title="v_{x,i+1}=v_{x,i}-\frac{B_{2}vv_{x,i}}{m}\Delta t" /></a>
 
<a href="http://www.codecogs.com/eqnedit.php?latex=v_{y,i&plus;1}=v_{y,i}-g\Delta&space;t-\frac{B_{2}vv_{y,i}}{m}\Delta&space;t" target="_blank"><img src="http://latex.codecogs.com/gif.latex?v_{y,i&plus;1}=v_{y,i}-g\Delta&space;t-\frac{B_{2}vv_{y,i}}{m}\Delta&space;t" title="v_{y,i+1}=v_{y,i}-g\Delta t-\frac{B_{2}vv_{y,i}}{m}\Delta t" /></a>

<a href="http://www.codecogs.com/eqnedit.php?latex=v=\sqrt{v_{x}^{2}&plus;v_{y}^{2}}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?v=\sqrt{v_{x}^{2}&plus;v_{y}^{2}}" title="v=\sqrt{v_{x}^{2}+v_{y}^{2}}" /></a>
