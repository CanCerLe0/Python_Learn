"""
计算圆的周长与面积
"""
r = float(input('请输入圆的半径:'))
C = 2 * 3.1415926 * r
S = 3.1415926 * r ** 2
print(f'圆的周长为：{C:.2f}')
print(f'圆的面积为：{S:.2f}')

#使用math模块中的pi常量来计算圆的周长和面积
import math
r1 = float(input('请输入圆的半径:'))
C1 = 2 * math.pi * r1
S1 = math.pi * r1 ** 2
#第二种输出方式 f-string的表达式中可以使用=号来显示变量名和变量值
print(f'{C1 = :.2f}')
print(f'{S1 = :.2f}')