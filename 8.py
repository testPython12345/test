from collections import deque, Counter, defaultdict

dd = defaultdict(list)
dd1 = defaultdict(int)

data = ['a', 'b', 'c', 'a', 'c']
for i in data:
    dd1[i] += 1
print(dd1)

sl = {'name':'', 'age':10, 'have_car':True}
print(sl)
dd['a'].append(1)
dd['a'].append(2)
dd['b'].append(4)
print(dd)




'''
a = [1, 2, 3]
print(a.pop())
print(a)
d = deque(maxlen=3)
d.append(2)
d.append(3)
d.appendleft(1)
print(d)
d.append(4)
print(d)
d.appendleft(1)
print(d)
d.rotate(1)
print(d)
d.rotate(-2)
print(d)
print(Counter([1,2,3,3,2,1,3]))
print(Counter('as fFf rew qvs wwd'))
'''