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
    # grid.append([int(char) for char in line if char != '\n'])
    grid_line = []
    for char in line:
        if char != '\n':
            if char == '.':
                grid_line.append(0)
            else:
                grid_line.append(int(char))
    grid.append(grid_line)

n_rows = len(grid)
n_cols = len(grid[0])

bottom_height = 0
top_height = 9

dirs = [(-1,0),(1,0),(0,1),(0,-1)]

# PART 1

def climb(current_height: int, current_location: (int,int)) -> list[(int,int)]:
    if current_height == top_height:
        # print(f'found peak {current_location}')
        return [current_location]
    # Keep climbing in all directions
    peaks = []
    for dir in dirs:
        next_location_row = current_location[0] + dir[0]
        next_location_col = current_location[1] + dir[1]
        if next_location_row < 0 or next_location_col < 0 or next_location_row >= n_rows or next_location_col >= n_cols:
            # out of bounds, ignore
            continue
        next_height = grid[next_location_row][next_location_col]
        if next_height != current_height + 1:
            # not +1 step, ignore
            continue
        # print(f'continue at {next_location_row},{next_location_col}')
        new_peaks = climb(next_height, (next_location_row, next_location_col))
        peaks += new_peaks
    return peaks


n_trailheads = 0
scores = []
ratings = []
for i_row, row in enumerate(grid):
    for j_col, height in enumerate(row):
        if height != bottom_height:
            continue
        # start climbing & finding score
        # print(f'starting at {i_row},{j_col}')
        peaks = climb(height, (i_row, j_col))
        # score = len(set(peaks))
        # PART 1
        score = len(set(peaks))
        # PART 2
        rating = len(peaks)
        scores.append(score)
        ratings.append(rating)

print(scores)
total_score = sum(scores)
print(total_score)
print(ratings)
total_rating = sum(ratings)
print(total_rating)
