# Problem 1.3 The Terminal Velocity
## 1.题目分析
<div align=center><a href="https://www.codecogs.com/eqnedit.php?latex=\frac{\mathrm{d}&space;v}{\mathrm{d}&space;t}=a-bv" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{\mathrm{d}&space;v}{\mathrm{d}&space;t}=a-bv" title="\frac{\mathrm{d} v}{\mathrm{d} t}=a-bv" /></a>
<div align=left>取a，b值分别为10，1，则有
<div align=center><a href="https://www.codecogs.com/eqnedit.php?latex=\frac{\mathrm{d}&space;v}{\mathrm{d}&space;t}=10-bv" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\frac{\mathrm{d}&space;v}{\mathrm{d}&space;t}=10-bv" title="\frac{\mathrm{d} v}{\mathrm{d} t}=10-bv" /></a>
<div align=left>用欧勒法绘制曲线，取步长h=0.1.有递推公式
<div align=center><a href="https://www.codecogs.com/eqnedit.php?latex=v_{n&plus;1}=v_{n}&plus;(10-v)\cdot&space;h" target="_blank"><img src="https://latex.codecogs.com/gif.latex?v_{n&plus;1}=v_{n}&plus;(10-v)\cdot&space;h" title="v_{n+1}=v_{n}+(10-v)\cdot h" /></a>

## 2.代码思路
  递推公式的部分可以用while循环实现
```python
while v <= 10:
    b = v
    v = v + (10-v)*h
    t = t + h
```
