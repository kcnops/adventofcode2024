import os
import re
from pathlib import Path

cwd = os.getcwd()

this_dir = Path(__file__).parent
input_file = this_dir / 'input.txt'

with input_file.open('r') as file:
    lines = file.readlines()

grid = []
for line in lines:
    fixed_line = line.replace('\n','')
    line_list = [char for char in fixed_line]
    grid.append(line_list)
print(grid)

rows = len(grid)
cols = len(grid[0])

word_to_find = 'XMAS'

directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

total = 0
for row in range(0, rows):
    for col in range(0, cols):
        if grid[row][col] != word_to_find[0]:
            continue

        # print(f'x at {row}-{col}')
        for dirX,dirY in directions:
            for k in range(1,len(word_to_find)):
                curr_x = col + dirX*k
                curr_y = row + dirY*k

                # check bounds
                if curr_x < 0 or curr_x > cols-1 or curr_y < 0 or curr_y > rows-1:
                    break

                if grid[curr_y][curr_x] != word_to_find[k]:
                    break

                # print(f'found {word_to_find[0:k+1]}')

                if k == len(word_to_find)-1:
                    total += 1

print(total)


orth_directions = [(-1,0),(0,-1),(0,1),(1,0)]
bin_directions = [-1,1]

# x_total = 0
# for row in range(0, rows):
#     for col in range(0, cols):
#         index_char = grid[row][col]
#         if index_char != 'M':
#             continue
#
#         for dirX,dirY in orth_directions:
#             curr_x = col + dirX*2
#             curr_y = row + dirY*2
#
#             # check bounds
#             if curr_x < 0 or curr_x > cols-1 or curr_y < 0 or curr_y > rows-1:
#                 continue
#
#             if grid[curr_y][curr_x] != 'M':
#                 continue
#
#             if dirX == 0:
#                 for second_dir in bin_directions:
#                     a_x = col + second_dir
#                     a_y = row + dirY
#
#                     # check bounds
#                     if a_x < 0 or a_x > cols - 1 or a_y < 0 or a_y > rows - 1:
#                         continue
#
#                     if grid[a_y][a_x] != 'A':
#                         continue
#                     s_x = col + 2*second_dir
#
#                     # check bounds
#                     if s_x < 0 or s_x > cols - 1 or curr_y < 0 or curr_y > rows - 1:
#                         continue
#
#                     if grid[row][s_x] != 'S':
#                         continue
#                     if grid[curr_y][s_x] != 'S':
#                         continue
#                     # print(f'Found x-mas at {row}-{col} dir {dirY}-{dirX} then {second_dir}')
#                     x_total += 1
#
#
# print(x_total/2)

x_total = 0
for row in range(0, rows):
    for col in range(0, cols):
        index_char = grid[row][col]
        if index_char != 'A':
            continue

        # print(f'A found at {row}-{col}')

        for dirX,dirY in orth_directions:
            # print(f'dirs: {dirY}-{dirX}')
            m_line_x = col - dirX
            m_line_y = row - dirY
            m1_x = m_line_x + dirY
            m2_x = m_line_x - dirY
            m1_y = m_line_y + dirX
            m2_y = m_line_y - dirX
            if (m1_x < 0 or m1_x > cols - 1 or m2_x < 0 or m2_x > cols - 1
                    or m1_y < 0 or m1_y > rows - 1 or m2_y < 0 or m2_y > rows - 1):
                continue
            if grid[m1_y][m1_x] != 'M' or grid[m2_y][m2_x] != 'M':
                continue
            # print(f'search first m at {m1_y}-{m1_x}')
            # print(f'search second m at {m2_y}-{m2_x}')

            s_line_x = col + dirX
            s_line_y = row + dirY
            s1_x = s_line_x + dirY
            s2_x = s_line_x - dirY
            s1_y = s_line_y + dirX
            s2_y = s_line_y - dirX
            if (s1_x < 0 or s1_x > cols - 1 or s2_x < 0 or s2_x > cols - 1
                    or s1_y < 0 or s1_y > rows - 1 or s2_y < 0 or s2_y > rows - 1):
                continue
            if grid[s1_y][s1_x] != 'S' or grid[s2_y][s2_x] != 'S':
                continue
            # print(f'search first s at {s1_y}-{s1_x}')
            # print(f'search second s at {s2_y}-{s2_x}')

            print(f'Found x-mas at {row}-{col} dir {dirY}-{dirX}')

            x_total += 1

print(x_total)


