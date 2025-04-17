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
    disk_map = file.readline()

# disk_map = '2333133121414131402'

print(disk_map)

disk_map_full = []
file = True
file_id = 0
for size in disk_map:
    if file:
        for space in range(0,int(size)):
            disk_map_full.append(file_id)
        file_id += 1
        file = False
    else:
        for space in range(0,int(size)):
            disk_map_full.append('.')
        file = True

print(disk_map_full)

def is_fragmented_list(disk_map: list) -> bool:
    return not ''.join([str(x) for x in disk_map]).strip('.').__contains__('.')

disk_size = len(disk_map_full)
print(disk_size)

# fragmented_disk_map = disk_map_full
# for moving_id_idx, moving_id in enumerate(reversed(fragmented_disk_map)):
#     if moving_id_idx % 100 == 0:
#         print(f'{moving_id_idx}/{disk_size}')
#     if is_fragmented_list(fragmented_disk_map):
#         break
#     if moving_id == '.':
#         continue
#     for empty_space_idx, potential_empty_space in enumerate(fragmented_disk_map):
#         if potential_empty_space != '.':
#             continue
#         fragmented_disk_map[empty_space_idx] = moving_id
#         fragmented_disk_map[disk_size-moving_id_idx-1] = '.'
#         break
#
# print(fragmented_disk_map)
#
# checksum = 0
# for idx, file_id in enumerate(fragmented_disk_map):
#     if file_id == '.':
#         continue
#     checksum += idx*int(file_id)
# print(checksum)

# PART 2

fragmented_disk_map = disk_map_full
# For every last file block
previous_id = -1
file_ids_done = []
for moving_id_idx, moving_id in enumerate(reversed(fragmented_disk_map)):
    if moving_id_idx % 100 == 0:
        print(f'{moving_id_idx}/{disk_size}')
    if moving_id == 0:
        # (until back at first file block)
        break
    if moving_id == '.':
        continue
    if moving_id in file_ids_done:
        continue
    if moving_id == previous_id:
        continue
    previous_id = moving_id
    # max size is digit 9
    file_size = 1
    for i in range(1,9):
        if disk_size-moving_id_idx-1-i < 0:
            break
        potential_other_moving_id = fragmented_disk_map[disk_size-moving_id_idx-1-i]
        if potential_other_moving_id == moving_id:
            file_size += 1
        else:
            break
    # Find first empty space
    for empty_space_idx, potential_empty_space in enumerate(fragmented_disk_map):
        if potential_empty_space != '.':
            continue
        if empty_space_idx >= disk_size-moving_id_idx-1:
            # Only move forward
            break
        empty_space_size = 1
        # max size is digit 9
        # Check large enough for file block
        for i in range(1, 9):
            if empty_space_idx+i >= disk_size:
                break
            potential_other_empty_space = fragmented_disk_map[empty_space_idx+i]
            if potential_other_empty_space == '.':
                empty_space_size += 1
                if empty_space_size >= file_size:
                    break
            else:
                break
        if empty_space_size >= file_size:
            for i in range(0,file_size):
                fragmented_disk_map[empty_space_idx+i] = moving_id
                fragmented_disk_map[disk_size-moving_id_idx-1-i] = '.'
            file_ids_done.append(moving_id)
            break

print(fragmented_disk_map)

checksum = 0
for idx, file_id in enumerate(fragmented_disk_map):
    if file_id == '.':
        continue
    checksum += idx*int(file_id)
print(checksum)