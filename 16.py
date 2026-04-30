'''
from multiprocessing import Process, Queue
import time 

def producer(que):
    for i in range(5):
        print(f'отправитель отправляет: {i}')
        que.put(i)
        time.sleep(1)
def consumer(que):
    while True:
        item = que.get()
        if item == 'DONE':
            break
        print(f'Потребитель получил: {item}')

if __name__ == "__main__":
    que = Queue()
    producer_procces = Process(target=producer, args=(que,))
    consumer_procces = Process(target=consumer, args=(que,))
    producer_procces.start()
    consumer_procces.start()
    producer_procces.join()
    que.put('DONE')
    consumer_procces.join()
    print('Обмен данными завершен')
    '''


from multiprocessing import Pool
import time
import random
def sq(x):
    print(x**2)
    time.sleep(random.randint(1, 7))
    return x**2

if __name__ == '__main__':
    with Pool(processes=3) as pool:
        numbers = [1, 2, 3, 4, 5, 6, 7, 8]
        results = pool.map(sq, numbers)
    print(f'квадраты чисел: {results}')