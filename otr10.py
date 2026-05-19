'''

def sum_two_nums(a, b):
    c = a + b
    print(f'Сумма -> {c}')
    return c

num1 = int(input('->')) #10
num2 = int(input('->')) #5
b = 0
g = sum_two_nums(num1, num2)
print(g)



def conversion_to_hours(seconds):
    return seconds / 3600
sec = int(input('---->'))
print(conversion_to_hours(sec))


a = 10
def f(x):
    st = 2
    def f1(x, st):
        global x_2
        x_2 = x**st
        print(a)
        print(st)
        return x_2
    return f1(x, st)
print(x_2)
c = 5
print(f(c))

'''

from random import randint
a = 10
def f():
    b = randint(0, 10) 
    print(f'b -> {b}')
    def f1(a, b):
        a = a+b
        print(f'a in f1 -> {a}')
        return a
    return f1(a, b)
f()
print(f'global a -> {a}')