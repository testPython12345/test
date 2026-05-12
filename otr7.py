"""
1 задача: написать функцию hello() которая выводит на экран фразу "hello world!"

2 задача: написать функцию sum_two(a, b) которая считает сумму a и b

3 задача: написать функцию max_two(a, b) которая находит максимальное из a и b



def hello():
    print('hello world!')
hello()
import random
def multiply(a, b):
    c = a*b
    print(f'Произвдение: {c}')
    return c

num_1 = int(input('->')) #4
num_2 = int(input('->')) #7
mult = multiply(num_1, num_2)
print(f'mult = {mult}')

#from random import randint as ri
import random as rnd

def buy_ticket():
    #ticket = ri(1, 10)
    ticket = rnd.randint(1, 10)
    if ticket == 7:
        return 'ВЫ ПОБЕДИЛИ!'
    return 'Вы проиграли, попробуйте еще раз :('
for i in range(3):
    print(buy_ticket())
    """


def max_two(a, b):
    if a>b:
        return a
    elif b>a:
        return b
    return None
print(max_two(2, 5))