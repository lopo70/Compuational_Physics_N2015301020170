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
