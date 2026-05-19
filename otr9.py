'''
true_pass = '1234'
password = input('Введите пароль ->')
while true_pass != password:
    print('Неверный пароль попробуйте еще раз!')
    password = input('Введите пароль ->')
print('Добро пожаловать!')

for i in range(10):
    print(i)
print('---------------------')
for i in range(2, 8):
    print(i)
print('---------------------')
for i in range(1, 10, 2):
    print(i*'*')
    '''
for i in range(10):
    print(i*'*')