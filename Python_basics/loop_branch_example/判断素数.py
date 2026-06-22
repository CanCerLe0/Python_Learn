"""
输入一个大于1的正整数判断它是不是素数

素数指的是只能被 1 和自身整除的大于 1 的整数。
例如对于正整数n ，我们可以通过在 2 到 n - 1 之间寻找有没有 n 的因子，
来判断它到底是不是一个素数。当然，循环不用从 2 开始到 n - 1 结束，
因为对于大于 1 的正整数，因子应该都是成对出现的，所以循环到根号n就可以结束了。
"""

num = int(input('请输入一个正整数: '))
end = int(num ** 0.5)
is_prime = True
for i in range(2, end + 1):
    if num % i == 0:
        is_prime = False
        break
#如果is_prime的值为True，说明num是素数，否则不是素数
if is_prime:
    print(f'{num}是素数')
else:
    print(f'{num}不是素数')