"""
输出斐波那契数列的前二十项
"""

a, b = 1, 1
for i in range(1, 21):
    if i == 1 or i == 2:
        print(1)
    else:
        c =a + b
        print(c)
        a, b = b, c
        