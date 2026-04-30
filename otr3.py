'''
int - целые числа
str - символьный тип данных
float - дроби
bool - True/False

print(a)
print('sdgasdg')
print(f'fghfgh {a}')
b = int(input('Введите число: '))
c = input('Введите число: ')
c = int(c)
print(b+c)
/ 
//
%
print(5/2)
print(5//2)
print(5%2)
print(7/5)
print(7//5)
print(7%3)

sec = input('Введите кол-во секунд: ')
sec = int(sec)
min = sec/60
print(f'Минут: {min}')
==
>
<
>=
<=
!=
'''
"""
0-6 ночь
6-12 утро
12-18 день
18-24 вечер
"""
chas = input('Введите который сейчас час: ')
chas = int(chas)
if 0<=chas<=6: #chas>=0 and chas <=6
    print('ночь')
elif 6<chas<=12:
    print('утро')
elif 12<chas<=18:
    print('утро')
elif 18<chas<=24:
    print('утро')
else:
    print('такого часа')

#Пользователь с клавиатуры вводит значения роста
#если рост больше 185, то не подходит, если меньше то подходит