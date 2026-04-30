import re
'''
#Сегодня 14 апреля 2026 года
text = 'Сегодня 14 апреля 2026 года'
lst_text = text.split(' ')
print(lst_text)
a = list(filter(lambda x: x.isdigit(), lst_text))
a1 = []
for i in lst_text:
    if i.isdigit():
        a1.append(i)
print(a1)

text = 'Сегодня 14 апреля 2026 года'
pattern = r'\d+'
matches = re.findall(pattern, text)
print(matches)
'''
import logging
logger1 = logging.getLogger('example1_logger')
logger1.setLevel(logging.DEBUG)
log_file2 = logging.FileHandler('app2.log')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
log_file2.setFormatter(formatter)
logger1.addHandler(log_file2)

a = input('Введите email: ')
pattern = r'[a-zA-Z0-9_+-=%]+@[a-zA-Z0-9_+-=%]+\.[a-z]{2,}'
if re.match(pattern, a):
    print('True')
    logger1.debug(f'Succes email: {a}')
else:
    logger1.error(f'Uncorect email: {a}')
'''
1) больше 8 символов
2) Наличие большой буквы
3) Использование спец символов
4) Использование цифр
5) Наличие строчной буквы
'''
pattern = r'^(!-_+=%$*[A-Z])(!-_+=%$*[a-z])(!-_+=%$*[0-9])(!-_+=%$*[a-zA-Z0-9]).{8,}$'



gos_nomer_pattern = r'^[A-Z]{1}[0-9]{3}[A-Z]{2}[0-9]{2,3}$'