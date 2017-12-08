# Exercise 11
# 问题

![](https://github.com/lopo70/Computational_Physics_N2015301020170/blob/master/Exercise%2011/%E6%8D%95%E8%8E%B7.PNG)
## 解题思路
在电荷不存在的空间中，电势分布满足拉普拉斯方程
<div align=center>
<a href="http://www.codecogs.com/eqnedit.php?latex=\frac{\partial&space;^{2}V}{\partial&space;x^{2}}&plus;\frac{\partial&space;^{2}V}{\partial&space;y^{2}}&plus;\frac{\partial&space;^{2}V}{\partial&space;z^{2}}=0" target="_blank"><img src="http://latex.codecogs.com/gif.latex?\frac{\partial&space;^{2}V}{\partial&space;x^{2}}&plus;\frac{\partial&space;^{2}V}{\partial&space;y^{2}}&plus;\frac{\partial&space;^{2}V}{\partial&space;z^{2}}=0" title="\frac{\partial ^{2}V}{\partial x^{2}}+\frac{\partial ^{2}V}{\partial y^{2}}+\frac{\partial ^{2}V}{\partial z^{2}}=0" /></a>

<div align=left>

如果加上边界条件，理论上我们就可以解出电势V。但是除了一些特殊的边界条件以外，对于这类问题我们难以得到解析解。所以我们必须使用数值计算的方法，得到电势的数值解。理论分析表明，对于本文中所讨论的情况，二维网格化离散的情况下，非边界上的点的电势相等于其周围最近的四个点的电势的平均值。

<div align=center>
<a href="http://www.codecogs.com/eqnedit.php?latex=V(i,j)=[V(i-1,j)&plus;V(i&plus;1,j)&plus;V(i,j-1)&plus;V(i,j&plus;1)]/4" target="_blank"><img src="http://latex.codecogs.com/gif.latex?V(i,j)=[V(i-1,j)&plus;V(i&plus;1,j)&plus;V(i,j-1)&plus;V(i,j&plus;1)]/4" title="V(i,j)=[V(i-1,j)+V(i+1,j)+V(i,j-1)+V(i,j+1)]/4" /></a>
  
<div align=left>
这一道题采用relaxation method，这种方法可以用来数值求解以拉普拉斯方程为代表的一类所谓的“椭圆偏微分方程”。电容器的边界条件如下图所示

<div align=center>

![](https://github.com/lopo70/Computational_Physics_N2015301020170/blob/master/Exercise%2011/%E6%8D%95%E8%8E%B71.PNG)

<div align=left>
图中两块有限导体平板横坐标为±0.3，纵坐标范围是-0.3~+0.3。边界条件为左侧平板上电势为+1，右侧平板上电势为-1，周围x=±1和y=±1的地方电势为0.
Jacobi方法的改进版是Gauss-Seidel方法。在计算中，我们总是算完一个点再算另一个点，也就是逐点更新计算结果。该方法主要的改进是在计算某一点的电势时，使用之前的点已经更新后的数据。

## 结果
电容器周围电势分布如图所示

<div align=center>

![](https://github.com/lopo70/Computational_Physics_N2015301020170/blob/master/Exercise%2011/1.PNG)

<div align=left>
三维势场示意图为

<div align=center>

![](https://github.com/lopo70/Computational_Physics_N2015301020170/blob/master/Exercise%2011/2.png)
<div align=left>
由电势分布推导出的电场分布
<div align=center>

![](https://github.com/lopo70/Computational_Physics_N2015301020170/blob/master/Exercise%2011/3.png)
