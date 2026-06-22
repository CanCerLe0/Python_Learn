"""
求100以内的素数
"""

for num in range(1, 100):
    end = int(num ** 0.5)
    is_prime = True
    for i in range(2, end+1):
        if num % i != 0:
            continue
        else:
            is_prime = False
            break
    if is_prime:
        print(f"{num}是素数")