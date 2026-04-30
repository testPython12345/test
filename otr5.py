'''
num = int(input('Введите число: '))
for i in range(1, 11):
    print(f'{num} * {i} = {num*i}')
print('---------------------')
j = 1
while j<11:
    print(f'{num} * {j} = {num*j}')
    j+=1
for i in range(1, 11):
    for j in range(1, 11):
        print(f'{i} * {j} = {i*j}')
        break
    print('---------------------')

list1 = [10, 20, 'привет']
list1.append(40)
print(list1)
list1.remove('привет') #удаляет по значению
list1.pop() #удаляет по индексу и возвращает
print(list1)
'''
students = []
while True:
    print('0 - выход из программы')
    print('1 - добавить студента')
    print('2 - вывести список студентов')
    print('3 - удалить студента по имени')
    a = int(input('->'))
    if a == 0:
        break
    elif a == 1:
        student = input('Введите ФИО студента: ')
        students.append(student)
    elif a == 2:
        print(students)
    elif  a == 3:
        student = input('Введите ФИО студента: ')
        students.remove(student)