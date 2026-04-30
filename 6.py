'''
def factorial(n):
    if n <= 1:
        return 1
    return n*factorial(n-1)
print(factorial(-1))

# 1 1 2 3 5 8 13 21
def fibanachi(n):
    if n <= 1:
        return 1
    return fibanachi(n-2) + fibanachi(n-1)

for i in range(10): # 0 1 2 3 4 5 6 7 8 9
    print(fibanachi(i), end=" ")'''
import sys
sys.setrecursionlimit(5000)

def calc_sum(n):
    if n <= 0:
        print(f'calc_sum({n}) = 0')
        return 0
    print(f'ДЛЯ ЧИСЛА {n}')
    print(f'{n} + {calc_sum(n-1)}')
    return n + calc_sum(n-1)
calc_sum(5)

def step(n, s):
    if s == 0:
        return 1
    elif s == 1:
        return n**s
    elif s%2==0:
        return step(n, s//2) * step(n, s//2)
    elif s%2!=0:
        return step(n,s-1)*n
print(step(2, 10))