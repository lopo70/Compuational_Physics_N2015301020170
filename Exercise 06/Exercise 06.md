# Exercise 06 Problem 2.21
## 问题
![](https://github.com/lopo70/Computational_Physics_N2015301020170/blob/master/Exercise%2006/%E6%8D%95%E8%8E%B7.PNG)
## 解题思路
题目要求计算一个击打出的产生绕竖直轴自旋的棒球的轨迹，以及在自旋角速度为2000rpm的情况下，棒球轨迹曲线水平偏转的距离。首先在空间建立三维直角坐标系，在地面选取一个原点，棒球高度为y轴，击打方向为x轴。设棒球绕y轴逆时针旋转，可知，会产生一个-z方向的力。
<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=F_{M}=S_{0}\omega&space;v_{x}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?F_{M}=S_{0}\omega&space;v_{x}" title="F_{M}=S_{0}\omega v_{x}" /></a>
<div align=left>
由于空气阻力对棒球y及z方向上的作用较小，故忽略不计。对这个问题再次使用欧勒法，则棒球实时坐标与速度为
<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=x_{i&plus;1}=x_{i}&plus;v_{x,i}\Delta&space;t" target="_blank"><img src="http://latex.codecogs.com/gif.latex?x_{i&plus;1}=x_{i}&plus;v_{x,i}\Delta&space;t" title="x_{i+1}=x_{i}+v_{x,i}\Delta t" /></a>

<a href="http://www.codecogs.com/eqnedit.php?latex=y_{i&plus;1}=y_{i}&plus;v_{y,i}\Delta&space;t" target="_blank"><img src="http://latex.codecogs.com/gif.latex?y_{i&plus;1}=y_{i}&plus;v_{y,i}\Delta&space;t" title="y_{i+1}=y_{i}+v_{y,i}\Delta t" /></a>

<a href="http://www.codecogs.com/eqnedit.php?latex=z_{i&plus;1}=z_{i}&plus;v_{z,i}\Delta&space;t" target="_blank"><img src="http://latex.codecogs.com/gif.latex?z_{i&plus;1}=z_{i}&plus;v_{z,i}\Delta&space;t" title="z_{i+1}=z_{i}+v_{z,i}\Delta t" /></a>

<a href="http://www.codecogs.com/eqnedit.php?latex=v_{x,i&plus;1}=v_{x,i}-\frac{B_{2}vv_{x,i}}{m}\Delta&space;t" target="_blank"><img src="http://latex.codecogs.com/gif.latex?v_{x,i&plus;1}=v_{x,i}-\frac{B_{2}vv_{x,i}}{m}\Delta&space;t" title="v_{x,i+1}=v_{x,i}-\frac{B_{2}vv_{x,i}}{m}\Delta t" /></a>

<a href="http://www.codecogs.com/eqnedit.php?latex=v_{y,i&plus;1}=v_{y,i}-g\Delta&space;t" target="_blank"><img src="http://latex.codecogs.com/gif.latex?v_{y,i&plus;1}=v_{y,i}-g\Delta&space;t" title="v_{y,i+1}=v_{y,i}-g\Delta t" /></a>

<a href="http://www.codecogs.com/eqnedit.php?latex=v_{z,i&plus;1}=v_{z,i}-\frac{S_{0}v_{x}\omega&space;}{m}\Delta&space;t" target="_blank"><img src="http://latex.codecogs.com/gif.latex?v_{z,i&plus;1}=v_{z,i}-\frac{S_{0}v_{x}\omega&space;}{m}\Delta&space;t" title="v_{z,i+1}=v_{z,i}-\frac{S_{0}v_{x}\omega }{m}\Delta t" /></a>

<div align=left>其中
<div align=center><a href="http://www.codecogs.com/eqnedit.php?latex=v=\sqrt{v_{x,i}^{2}&plus;v_{y,i}^{2}&plus;v_{z,i}^{2}}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?v=\sqrt{v_{x,i}^{2}&plus;v_{y,i}^{2}&plus;v_{z,i}^{2}}" title="v=\sqrt{v_{x,i}^{2}+v_{y,i}^{2}+v_{z,i}^{2}}" /></a>
<div align=center>一般情况下，设<a href="http://www.codecogs.com/eqnedit.php?latex=\frac{S_{0}}{m}=4.1\times&space;10^{-4}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{S_{0}}{m}=4.1\times&space;10^{-4}" title="\frac{S_{0}}{m}=4.1\times 10^{-4}" /></a>，棒球出射角度以及速度，自旋角速度为方便起见在程序中设定。
