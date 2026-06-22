"""
输入两个正整数求它们的最大公约数
"""

x = int(input("请输入第一个正整数："))
y = int(input("请输入第二个正整数："))
while x % y != 0:
    x, y = x % y, x
print(f"最大公约数是{y}")