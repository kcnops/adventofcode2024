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

n_rows = len(grid)
n_cols = len(grid[0])

# for line in grid:
#     print(line)

total = 0
for location_row, row in enumerate(grid):
    for location_col, location in enumerate(row):
        found = False
        for possible_antenna_row, row2 in enumerate(grid):
            if found:
                break
            for possible_antenna_col, possible_antenna_freq in enumerate(row2):
                if found:
                    break
                # possible_antenna_freq = grid[possible_antenna_row][possible_antenna_col]
                if location_row == possible_antenna_row and location_col == possible_antenna_col:
                    # Skip same location
                    continue
                if possible_antenna_freq == '.':
                    continue
                # found antenna
                row_diff = possible_antenna_row - location_row
                col_diff = possible_antenna_col - location_col
                location_on_double_diff_row = location_row + 2*row_diff
                location_on_double_diff_col = location_col + 2*col_diff
                if location_on_double_diff_row < 0 or location_on_double_diff_row >= n_rows or location_on_double_diff_col < 0 or location_on_double_diff_col >= n_cols:
                    # double diff is out of bounds
                    continue
                possible_double_diff_antenna_freq = grid[location_on_double_diff_row][location_on_double_diff_col]
                if possible_double_diff_antenna_freq == possible_antenna_freq:
                    total += 1
                    found = True
                    continue

print(total)


total = 0
# For each location
for location_row, row in enumerate(grid):
    for location_col, location in enumerate(row):
        print(f'{location_row}-{location_col}')
        found = False
        # For each direction
        for dir_row in range(-math.ceil(n_rows/2)-1,math.ceil(n_rows/2)-1):
            if found:
                break
            for dir_col in range(-math.ceil(n_cols/2)-1,math.ceil(n_cols/2)-1):
                if found:
                    break
                if dir_row == 0 and dir_col == 0:
                    break
                # print(f'{dir_row}-{dir_col}')
                found_antennas = []
                out_of_bounds = False
                i = 1
                # Loop until end
                while not out_of_bounds:
                    next_location_row = location_row + i*dir_row
                    next_location_col = location_col + i*dir_col
                    if next_location_row < 0 or next_location_col < 0 or next_location_row >= n_rows or next_location_col >= n_cols:
                        out_of_bounds = True
                        break
                    antenna_freq = grid[next_location_row][next_location_col]
                    if antenna_freq != '.':
                        if antenna_freq in found_antennas:
                            # If twice same frequency spotted -> antinode
                            total += 1
                            found = True
                            break
                        else:
                            found_antennas.append(antenna_freq)
                        found_antennas.append(antenna_freq)
                    i += 1

print(total)

# Too low
# Probably because of locations in between antennas on the line
