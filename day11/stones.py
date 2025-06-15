import itertools
import math
import os
from multiprocessing import Process, Pool
from pathlib import Path
from typing import List
from tqdm import tqdm
import copy
import time

cwd = os.getcwd()

this_dir = Path(__file__).parent
input_file = this_dir / 'input.txt'

with input_file.open('r') as file:
    lines = file.readlines()
line = lines[0]

line.replace('\n','')
# grid.append([int(char) for char in line if char != '\n'])
stones = [int(i) for i in line.split()]


def blink(stones: List[int]) -> List[int]:
    # if len(stones) > 1 and len(stones)%4 == 0:
    #     part_size = int(len(stones)/4)
    #     pool = Pool()
    #     future1 = pool.apply_async(blink, [stones[0*part_size:1*part_size-1]])
    #     future2 = pool.apply_async(blink, [stones[1*part_size:2*part_size-1]])
    #     future3 = pool.apply_async(blink, [stones[2*part_size:3*part_size-1]])
    #     future4 = pool.apply_async(blink, [stones[3*part_size:4*part_size-1]])
    #     result1 = future1.get()
    #     result2 = future2.get()
    #     result3 = future3.get()
    #     result4 = future4.get()
    #     return result1 + result2 + result3 + result4
    new_stones = []
    for i in range(len(stones)):
        old_stone = stones[i]
        if old_stone == 0:
            new_stone = [1]
        elif len(str(stones[i]))%2 == 0:
            size = len(str(stones[i]))
            half_size = int(size / 2)
            new_stone = [int(str(stones[i])[:half_size]), int(str(stones[i])[half_size:])]
        else:
            new_stone = [old_stone * 2024]
        new_stones = new_stones + new_stone
    return new_stones

print(stones)

n_blinks = 25
for i in tqdm(range(n_blinks), miniters=1):
    start = time.time()
    stones = blink(stones)
    end = time.time()
    print(end - start)
    # print(stones)

result = len(stones)
print(result)