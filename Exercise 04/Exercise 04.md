# Problem 1.3 The Terminal Velocity
## 1.题目分析
<div align=center><a href="https://www.codecogs.com/eqnedit.php?latex=\frac{\mathrm{d}&space;v}{\mathrm{d}&space;t}=a-bv" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{\mathrm{d}&space;v}{\mathrm{d}&space;t}=a-bv" title="\frac{\mathrm{d} v}{\mathrm{d} t}=a-bv" /></a>
<div align=left>取a，b值分别为10，1，则有
<div align=center><a href="https://www.codecogs.com/eqnedit.php?latex=\frac{\mathrm{d}&space;v}{\mathrm{d}&space;t}=10-bv" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{\mathrm{d}&space;v}{\mathrm{d}&space;t}=10-bv" title="\frac{\mathrm{d} v}{\mathrm{d} t}=10-bv" /></a>
<div align=left>用欧勒法绘制曲线，取步长h=0.1.有递推公式
<div align=center><a href="https://www.codecogs.com/eqnedit.php?latex=v_{n&plus;1}=v_{n}&plus;(10-v)\cdot&space;h" target="_blank"><img src="https://latex.codecogs.com/gif.latex?v_{n&plus;1}=v_{n}&plus;(10-v)\cdot&space;h" title="v_{n+1}=v_{n}+(10-v)\cdot h" /></a>

<div align=left>
 
 ## 2.代码思路
  递推公式的部分可以用while循环实现
```python
while v <= 10:
    b = v
    v = v + (10-v)*h
    t = t + h
```
而为了便于之后绘出速度-时间图像，将循环中的两组数据分别存储于两个list中
```python
f.append(t)
    z.append(v)
 ```
由于该题目速度具有一个有限范围，而另一个时间变量却没有范围。但是题目要求给出终止速度，就需要在while循环中加一个if判断语句，并且中止循环
```python 
 if v == b:
        print (d,b)
        break 
 ```
其中v变量在while语句开头处定义为前一次输出的v值，通过比较下一次输出v值与b的值，可以判断速度是否已经不变（即达到终止速度）。
最后用matplotlib画出曲线

![](https://github.com/lopo70/Computational_Physics_N2015301020170/blob/master/Exercise%2004/1.png)
 
 ## 3.思考总结
 微分方程精确解为
 <div align=center><a href="https://www.codecogs.com/eqnedit.php?latex=v=-10e^{-t}&plus;10" target="_blank"><img src="https://latex.codecogs.com/gif.latex?v=-10e^{-t}&plus;10" title="v=-10e^{-t}+10" /></a>

<div align=left>代码为

```python
    n = -10*py.exp(-t)+10
    m.append(n)
```
<div align=left>精确图像（橙色）与拟合图像（蓝色）为

![](https://github.com/lopo70/Computational_Physics_N2015301020170/blob/master/Exercise%2004/2.png)
 
 <div align=left>可见用欧勒法绘出的图像十分接近精确解的图像。
