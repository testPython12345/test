'''
#через def
def summm(a, b):
    return a+b
#лямбда
summ = lambda a, b: f"сумма = {a+b}"
print(summ(5, 10))

arr = [1, 2, 3]
print(list(map(lambda x: x**2, arr)))


list1 = [i for i in range(1, 10)] #генератор списка
print(list1)
print(list(filter(lambda x: x%2==0, list1)))

from functools import reduce

arr = [i for i in range(1, 6)]
print(reduce(lambda a,b:a*b, arr))

a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c']
c = list(zip(a, b))
d = c[1][0]
print(d)
'''
from functools import reduce
def calc_total(cart):
    items_total = map(lambda x: x[0]*x[1], cart)
    return reduce(lambda a,b:a+b, items_total)
cart = [(100.99, 1),(1549.00, 2),(56.87, 3)]
print(calc_total(cart))
