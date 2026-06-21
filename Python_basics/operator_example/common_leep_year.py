"""
输入年份，闰年输出True，平年输出False
"""
year = int(input('请输入年份: '))
#公元年份为 4 的倍数但非 100 的倍数是闰年; 公元年份为 400 的倍数是闰年
is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0 #Bool值
print(f'{is_leap = }')