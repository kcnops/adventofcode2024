import os
from pathlib import Path

cwd = os.getcwd()

this_dir = Path(__file__).parent
input_file = this_dir / 'input.txt'

with input_file.open('r') as file:
    lines = file.readlines()

list1 = []
list2 = []
for line in lines:
    splits = line.replace('\n','').split('   ')
    list1.append(int(splits[0]))
    list2.append(int(splits[1]))

list1.sort()
list2.sort()

total_distance = 0
for loc1, loc2 in zip(list1, list2):
    total_distance += abs(loc1 - loc2)

print(total_distance)