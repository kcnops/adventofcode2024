import itertools
import math
import os
from dataclasses import dataclass
from multiprocessing import Process, Pool
from pathlib import Path
from typing import List, Optional
from tqdm import tqdm
import copy
import time

cwd = os.getcwd()

this_dir = Path(__file__).parent
input_file = this_dir / 'input.txt'

with input_file.open('r') as file:
    lines = file.readlines()


@dataclass
class Slot:
    a_x: int
    a_y: int
    b_x: int
    b_y: int
    x_goal: int
    y_goal: int


a_price = 3
b_price = 1


slots = []
for line in lines:
    line = line.replace('\n','')
    if line.startswith('Button A'):
        splits = line.split('+')
        a_x = int(splits[1].split(',')[0])
        a_y = int(splits[2])
    elif line.startswith('Button B'):
        splits = line.split('+')
        b_x = int(splits[1].split(',')[0])
        b_y = int(splits[2])
    elif line.startswith('Prize'):
        splits = line.split('=')
        x_goal = int(splits[1].split(',')[0])
        y_goal = int(splits[2])
    elif len(line) == 0:
        slots.append(Slot(a_x=a_x, a_y=a_y, b_x=b_x, b_y=b_y, x_goal=x_goal, y_goal=y_goal))
        a_x, a_y, b_x, b_y, x_goal, y_goal = None, None, None, None, None, None
    else:
        raise ValueError(f'Problem parsing line: {line}')
if a_x is not None:
    slots.append(Slot(a_x=a_x, a_y=a_y, b_x=b_x, b_y=b_y, x_goal=x_goal, y_goal=y_goal))
    a_x, a_y, b_x, b_y, x_goal, y_goal = None, None, None, None, None, None


def solve_slot(slot: Slot):
    winning_combos = []
    for a in range(101):
        for b in range(101):
            x = a*slot.a_x + b*slot.b_x
            y = a*slot.a_y + b*slot.b_y
            if x == slot.x_goal and y == slot.y_goal:
                # print(f'jej at a {a} & b {b}')
                winning_combos.append((a,b))
                return a*a_price + b*b_price
                break
            if x > slot.x_goal or y > slot.y_goal:
                break
    return 0
    # return winning_combos

total_price = 0
for slot in tqdm(slots):
    total_price += solve_slot(slot)
print(total_price)