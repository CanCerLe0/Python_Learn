"""用python设计一个游戏"""

temp = input("猜一个我心里想的数字：") #input函数的作用是获取用户输入的内容，返回一个字符串
guess = int(temp) #int函数的作用是将字符串转换为整数，如果输入的内容不能转换为整数，会抛出一个异常

if guess == 8: #判定符号（== !=等内容）同c语言，‘is’以及‘is not’先放一边
    print("你猜对了！")
elif guess < 8:
    print("你猜的数字小了！")
else:
    print("你猜的数字大了！")

print("游戏结束！")


temp = input("猜一个我心里想的数字：") #input函数的作用是获取用户输入的内容，返回一个字符串
guess = int(temp) #int函数的作用是将字符串转换为整数，如果输入的内容不能转换为整数，会抛出一个异常

while guess != 8: #while语句的使用同C语言，注意要有冒号
    if guess < 8:
        print("你猜的数字小了！")
    elif guess > 8:
        print("你猜的数字大了！")
    elif guess ==8:
        break #break作用同C语言，跳出循环
    temp = input("请重新输入：")
    guess = int(temp)

print("你猜对了！")


import random

temp = input("猜一个我心里想的数字：") #input函数的作用是获取用户输入的内容，返回一个字符串
guess = int(temp) #int函数的作用是将字符串转换为整数，如果输入的内容不能转换为整数，会抛出一个异常
secret = random.randint(1, 10) #random模块的randint函数可以生成一个指定范围内的随机整数

while guess != secret: #while语句的使用同C语言，注意要有冒号
    if guess < secret:
        print("你猜的数字小了！")
    elif guess > secret:
        print("你猜的数字大了！")
    temp = input("请重新输入：")
    guess = int(temp)
print("你猜对了！")