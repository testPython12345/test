import csv

with open('text.csv', 'r', encoding='utf-8') as file:
    text = csv.reader(file)
    for row in text:
        print(row)

data = [
    ['Name', 'Salary', 'Gender'],
    ['Bob', 2000, 'Male'],
    ['Gleb', 200, 'Male'],
    ['Alice', 5000, 'Female']
]
with open('people.csv', 'w', encoding='utf-8', newline='') as f:
    text = csv.writer(f)
    text.writerows(data)
print('--------------------')
with open('people.csv', 'r', encoding='utf-8', newline='') as f:
    txt = csv.reader(f)
    print(list(txt))