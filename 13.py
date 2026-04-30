'''
import asyncio

async def task1():
    print('Task1 Start')
    await asyncio.sleep(3)
    print('task1 end')

async def task2():
    print('Task2 Start')
    await asyncio.sleep(1)
    print('task2 end') 

async def main():
    t1 = asyncio.create_task(task1())
    t2 = asyncio.create_task(task2())
    await t2
    await t1
asyncio.run(main())
'''
import time 
import asyncio
import aiohttp

urls = [
    "https://www.google.com"
]

async def fetch(session, url):
    async with session.get(url) as response:
        text = await response.text()
        with open('test.html', 'w', encoding='utf-8') as f:
            f.write(text) 
        print(f'{url} -> {len(text)} символов')
        return len(text)
async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        print(f'Сумма символов: {sum(results)}')
start = time.time()
asyncio.run(main())
end = time.time()
print(f'Время выполнения: {round(end-start,2)}, сек')


