# Exercise 10
## 问题
![](https://github.com/lopo70/Computational_Physics_N2015301020170/blob/master/Exercise%2010/e.png)
## 解题思路
相比较太阳与地球的两体运动，对于三体运动我们需要考虑木星对地球及太阳的影响。假设三者处在同一平面x-y平面，我们利用牛顿第二定律以及万有引力公式可以得到地球x方向上的运动方程
<div align=center>
![](<a href="http://www.codecogs.com/eqnedit.php?latex=\frac{dv_{x,e}}{t}=-\frac{GM_{s}x_{e}}{r^{3}}-\frac{GM_{J}(x_{e}-x_{J})}{r_{EJ}^{3}}" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{dv_{x,e}}{t}=-\frac{GM_{s}x_{e}}{r^{3}}-\frac{GM_{J}(x_{e}-x_{J})}{r_{EJ}^{3}}" title="\frac{dv_{x,e}}{t}=-\frac{GM_{s}x_{e}}{r^{3}}-\frac{GM_{J}(x_{e}-x_{J})}{r_{EJ}^{3}}" /></a>)

<div align=left>
同理可得到地球运动y方向的运动方程，以及木星x，y方向上的运动方程。 
本文计算使用欧拉-克拉默方法。 
