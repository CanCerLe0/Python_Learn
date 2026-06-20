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