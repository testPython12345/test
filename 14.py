'''
import random
import string

alphabet = string.ascii_lowercase+"     "
for i in range(1, 4):
    with open(f'file{i}.txt', 'w', encoding='utf-8') as f:
        text = ''.join(random.choice(alphabet) for _ in range(5_000_000))
        f.write(text)
        '''
import asyncio
import aiofiles
from collections import Counter

files = ['file1.txt', 'file2.txt', 'file3.txt']

def count(text):
    return Counter(text)

async def procces_file(filename):
    async with aiofiles.open(filename, 'r', encoding='utf-8') as f:
        text = await f.read()
    counts = await asyncio.to_thread(count, text)
    return filename, counts
async def main():
    results = await asyncio.gather(*(procces_file(f) for f in files))
    for filename, counts in results:
        print(f'\n{filename}')
        for ch, cnt in counts.most_common():
            print(f'{repr(ch)}: {cnt}')
asyncio.run(main())