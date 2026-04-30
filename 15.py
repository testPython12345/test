'''
import threading
import time

def print_numbers():
    for i in range(10):
        print(f'Chislo: {i}')
        time.sleep(0.5)

thread = threading.Thread(target=print_numbers)
thread.start()
print('Potok1 start!')
thread.join()
print('Potok1 end!')
'''
import threading
import queue
counter = 0
lock = threading.Lock()
def f(q):
    task = q.get()
    print(f'Task: {task}')
    global counter
    for _ in range(5000):
        with lock:
            counter += 1
    q.task_done()
q = queue.Queue()
for i in range(5):
    q.put(f'Task {i}')
threads = [threading.Thread(target=f, args=(q,)) for _ in range(5)]
for th in threads:
    th.start()
print(f'Counter value: {counter}')

