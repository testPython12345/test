'''
a = [10, 20.5, 'HEllo', True]
print(a)
print(a[-2])
a.append(20)
print(a)
a.pop(2)
print(a)
a.remove(20.5)
print(a)

for i in a:
    print(i)
print(len(a))
5 - количество чисел
10
26
7
18
24
'''
n = int(input('->'))
list1 = []
for i in range(n):
    a = int(input())
    list1.append(a)
print(f'ср: {sum(list1)/len(list1)}')
print(min(list1))
print(max(list1))

list2 = [12, 64, 52, 84, 9, 34]
m = list2[0]
for i in list2:
    if i > m:
        m = i
print(m)

def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -=1 
        arr[j+1] = key
    return arr
print(insert_sort(list2))