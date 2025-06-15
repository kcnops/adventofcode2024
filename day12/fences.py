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

grid = []
for line in lines:
    line.replace('\n','')
    # grid.append([int(char) for char in line if char != '\n'])
    grid_line = []
    for char in line:
        if char != '\n':
            grid_line.append(char)
    grid.append(grid_line)

n_rows = len(grid)
n_cols = len(grid[0])

dirs = [(-1,0),(1,0),(0,1),(0,-1)]

PROCESSED_FIELDS = []

def is_in_bounds(row, col) -> bool:
    return 0 <= row < n_rows and 0 <= col < n_cols


def is_already_processed(row, col) -> bool:
    return PROCESSED_FIELDS.__contains__((row,col))

def add_to_processed(row, col):
    PROCESSED_FIELDS.append((row,col))


# Loop over all fields
    # Check if we already processed field
    # add to processed fields, area +1
    # Check all directions
        # Check diff or OOB -> perimeter +1
        # Check if same -> repeat for this field, if not already processed, add to proc fields, area+1, check directions, ...

def process_field(row: int, col: int, field: str, area: int, perimeter: int) -> (int, int):
    if is_already_processed(row, col):
        return area, perimeter
    add_to_processed(row, col)
    area = area + 1
    print(f'processing {row} {col}')
    for row_dir, col_dir in dirs:
        new_row = row + row_dir
        new_col = col + col_dir
        if not is_in_bounds(new_row, new_col):
            perimeter += 1
            continue
        new_field = grid[new_row][new_col]
        if new_field != field:
            perimeter += 1
            continue
        new_area, new_perimeter = process_field(new_row, new_col, new_field, 0, 0)
        area += new_area
        perimeter += new_perimeter
    return area, perimeter

total_price = 0
for row, field_row in enumerate(grid):
    for col, field in enumerate(field_row):
        if is_already_processed(row, col):
            continue
        print(f'Start processing {row} {col}')
        area, perimeter = process_field(row, col, field, 0, 0)
        print(f'Found area {area} & perimeter {perimeter}')
        total_price += area * perimeter

print(total_price)
