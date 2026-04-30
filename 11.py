'''
def is_balanced(string):
    if not string:
        return 'Сбалансированая'
    if len(string) == 1 or string[0] not in '({[':
        return 'не сбалансированая'
    for pair in ['()', '[]', '{}']:
        if pair in string:
            new_string = string.replace(pair, '')
            return is_balanced(new_string)
string = input('введите: ')
print(is_balanced(string))

num = 1
for _ in range(poww):
    num *= number

def num_pow(a, b):
    if b == 0:
        return 1
    return a*num_pow(a, b-1)

number = int(input()) #5
poww = int(input()) #3  
print(num_pow(number, poww))  
'''

s = input('введите: ')
c = 0
while s != '':
    c += 1
    print(s)
    s = s[1:]
print(c)
s = input('введите: ')
def myLen(s):
    if s == '':
        return 0
    return 1+myLen(s[1:])
print(myLen(s))