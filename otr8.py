'''
file = open("file1.txt", "r", encoding="utf-8")
print(file)
text0 = file.read()
#text = file.readline()
#print(text)
print('-------------------------')
text1 = file.readlines()
print(text1)
file.close()
'''
with open("file1.txt", "r", encoding="utf-8") as file:
    for i in file:
        print(i)

with open("file_test.txt", 'w', encoding="utf-8") as f:
    f.write("Привет всем!\n")
    f.write('бла бла бла\n')

with open("file_test.txt", 'a', encoding="utf-8") as f:
    f.write("А вот 'a' добавляет в конец файла, а не перезаписывает\n")

import random
s = 'abcdef1234  '
print(random.choice(s))