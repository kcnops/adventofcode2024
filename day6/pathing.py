import itertools
import math
import os
from pathlib import Path
from typing import List
from tqdm import tqdm
import copy

cwd = os.getcwd()

this_dir = Path(__file__).parent
input_file = this_dir / 'input.txt'

with input_file.open('r') as file:
    lines = file.readlines()

grid = []
for line in lines:
    line.replace('\n','')
    grid.append([char for char in line if char != '\n'])

for j, line in enumerate(lines):
    for i, char in enumerate(line):
        if char == '^':
            starting_x = i
            starting_y = j

len_x = len(grid[0])
len_y = len(grid)

print(f'starting at {starting_x},{starting_y}')

starting_dir_x = 0
starting_dir_y = -1

def get_next_dir(dirX, dirY) -> (int, int):
    if dirY == -1: return (1,0)
    if dirX == 1: return (0,1)
    if dirY == 1: return (-1,0)
    if dirX == -1: return (0,-1)

def count_x(grid) -> int:
    total = 0
    for line in grid:
        total += line.count('X')
    return total

def find_start_position(grid):
    for j, line in enumerate(grid):
        for i, char in enumerate(line):
            if char == '^':
                return i, j


def get_steps_to_exit(grid) -> int:
    # Find starting position
    starting_x, starting_y = find_start_position(grid)
    # Find
    len_x = len(grid[0])
    len_y = len(grid)
    # Starting setup
    curr_x = starting_x
    curr_y = starting_y
    dir_x = starting_dir_x
    dir_y = starting_dir_y
    # Loop with limit
    steps = 0
    while steps < 99999:
        # turn if need
        next_x = curr_x + dir_x
        next_y = curr_y + dir_y
        try:
            next = grid[next_y][next_x]
        except IndexError:
            return count_x(grid)
        if next == '#' or next == 'O':
            dir_x, dir_y = get_next_dir(dir_x, dir_y)
        # step
        curr_x += dir_x
        curr_y += dir_y
        grid[curr_y][curr_x] = 'X'
        # check end
        steps += 1
    # Couldn't find exit, so no result
    return None

p1_grid = copy.deepcopy(grid)
print(get_steps_to_exit(p1_grid))

n_options = len_x*len_y
print('to check: ' + str(n_options))

checked = 0
result = 0
for j, line in enumerate(grid):
    for i, char in enumerate(line):
        checked += 1
        if checked % 1000 == 0:
            print(f'Checked {checked}/{n_options}')
        if char == '.':
            p2_grid = copy.deepcopy(grid)
            p2_grid[j][i] = 'O'
            print(f'Checking {p2_grid}')
            if not get_steps_to_exit(p2_grid):
                # Couldnt exit so obstruction found
                result += 1
print(result)


