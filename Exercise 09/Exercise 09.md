# Exercise 09
# 问题
![](https://github.com/lopo70/Computational_Physics_N2015301020170/blob/master/Exercise%2009/%E6%8D%95%E8%8E%B7.PNG)
## 解题思路
用Euler法计算绘制台球在不同平面下的轨迹并观察混沌现象
当碰撞发生时,<br>
![](http://latex.codecogs.com/gif.latex?%5C%5C%20%5Cvec%7Bv%7D_%7Bi%2C%5Cperp%20%7D%3D%28%5Cvec%7Bv%7D_%7Bi%7D%5Ccdot%20%5Chat%7Bn%7D%29%5Chat%7Bn%7D%20%5C%5C%20%5Cvec%7Bv%7D_%7Bi%2C%5Cparallel%20%7D%3D%5Cvec%7Bv%7D_%7Bi%7D-%5Cvec%7Bv%7D_%7Bi%2C%5Cperp%20%7D)<br>
所以碰撞后的速度为<br>
![](http://latex.codecogs.com/gif.latex?%5C%5C%20%5Cvec%7Bv%7D_%7Bf%2C%5Cperp%20%7D%3D-%5Cvec%7Bv%7D_%7Bi%2C%5Cperp%20%7D%20%5C%5C%20%5Cvec%7Bv%7D_%7Bf%2C%5Cparallel%20%7D%3D%5Cvec%7Bv%7D_%7Bi%2C%5Cparallel%20%7D)
