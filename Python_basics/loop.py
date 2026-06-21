"""
    Python循环结构
"""

"""
Python 内置`time`模块的`sleep`函数可以实现程序的休眠，参数`1`表示休眠的秒数
可以使用`int`或`float`类型，例如`0.05`表示`50`毫秒。
"""
import time

print('hello, world')
time.sleep(1) # 休眠1秒

#for-in循环结构
#每隔一秒输出一个数字 总共输出十个数字
"""
range(101)：可以用来产生`0`到`100`范围的整数，需要注意的是取不到`101`。
range(1, 101)：可以用来产生`1`到`100`范围的整数，相当于是左闭右开的设定，即`[1, 101)`。
range(1, 101, 2)：可以用来产生`1`到`100`的奇数，其中`2`是步长（跨度），即每次递增的值，`101`取不到。
range(100, 0, -2)：可以用来产生`100`到`1`的偶数，其中`-2`是步长（跨度），即每次递减的值，`0`取不到。
"""
for i in range(10):
    print(i)
    time.sleep(1)

for _ in range(10): #当循环变量不需要使用时 可以使用_代替
    print('hello, world')
    time.sleep(1)

#1到100的整数求和
total = 0
for i in range(1, 101):
    total += i
print(total)

#使用Python内置的`sum`函数和`range`函数来计算1到100的整数求和
print(sum(range(1, 101)))

"""
while循环结构，同C语言中的while循环结构，满足条件就执行循环体，否则就跳出循环
"""
total = 0
i = 1
while i <= 100:
    total += i #total = total + i
    i += 1     #i = i + 1
print(total)

"""
break和continue语句同C语言中的break和continue语句
break语句用于跳出当前循环体
continue语句用于跳过当前循环体的剩余部分，直接进入下一次循环
"""
#1到100的偶数求和（break实现）
total = 0
i = 2
while True:
    total += i
    i += 2
    if i > 100:
        break
print(total) 

#1到100的偶数求和（continue实现）
total = 0
for i in range(1, 101):
    if i % 2 != 0:
        continue
    total += i
print(total)

""""
循环嵌套同C语言中的循环嵌套结构，外层循环控制行数，内层循环控制列数
"""