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
import re

cwd = os.getcwd()

this_dir = Path(__file__).parent
input_file = this_dir / 'input.txt'

with input_file.open('r') as file:
    lines = file.readlines()

# WIDTH = 11
WIDTH = 101
# HEIGHT = 7
HEIGHT = 103

MOVES = 100

x_split = math.floor(WIDTH/2)  # 5 - 50
y_split = math.floor(HEIGHT/2)  # 3 - 51

class Guard:
    pos_x: int
    pos_y : int
    v_x: int
    v_y: int

    def __init__(self, pos_x: int, pos_y: int, v_x: int, v_y: int):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.v_x = v_x
        self.v_y = v_y

    def move(self):
        self.pos_x = (self.pos_x + self.v_x) % WIDTH
        self.pos_y = (self.pos_y + self.v_y) % HEIGHT

    # quadrants are 1 to 4, 0 if on the middle lines
    def get_q(self) -> int:
        if self.pos_x == x_split or self.pos_y == y_split:
            return 0
        q = 1
        if self.pos_x > x_split:
            q += 1
        if self.pos_y > y_split:
            q += 2
        return q

    def __str__(self):
        return f'{self.pos_x},{self.pos_y}'

# Regex pattern to capture the values
pattern = re.compile(r"p=(-?\d+),(-?\d+)\s+v=(-?\d+),(-?\d+)")

guards = []
for line in lines:
    match = pattern.match(line)
    if match:
        px, py, vx, vy = map(int, match.groups())
        guards.append(Guard(pos_x=px, pos_y=py, v_x=vx, v_y=vy))
        # print(f"Parsed: p=({px},{py}) v=({vx},{vy})")
    else:
        print(f"!! No match for line: {line}")

for i in range(0, MOVES):
    for guard in guards:
        guard.move()

quadrants = []
for guard in guards:
    quadrants.append(guard.get_q())

print(quadrants)

q1 = quadrants.count(1)
q2 = quadrants.count(2)
q3 = quadrants.count(3)
q4 = quadrants.count(4)

print(f'{q1} - {q2} - {q3} - {q4}')

output = q1*q2*q3*q4
print(output)

