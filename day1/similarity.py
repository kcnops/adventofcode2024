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

similarity = 0
for loc in list1:
    simcount = list2.count(loc)
    similarity += loc * simcount

print(similarity)
