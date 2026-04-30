'''
price = input('Введите цену товара: ') #str
sayle = input('Введите скидку: ') #str
price = int(price) #int
sayle = int(sayle) #int
price_with_sayle = price * (1 - sayle/100)
print(f'Цена по скидке {price_with_sayle}')
'''
from random import randint as ri

print(ri(1, 10))


'''
if #основое условие
elif #доп условие
else #иначе (обратное от всех условий в конструкции)
> больше
< меньше
== равенство
!= неравно
<= меньше или равно
>= больше или равно
'''
num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
znak = input('Введите знак операции: *, +, -, /')
if znak == '+':
    print(f'Сумма: {num1+num2}')
elif znak == '*':
    print(f'Произведение: {num1*num2}')
elif znak == '-':
    print(f'Вычитание: {num1-num2}')
elif znak == '/':
    print(f'Частное: {num1/num2}')
else:
    print('такого знака не существует ')