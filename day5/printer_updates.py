import itertools
import math
import os
from pathlib import Path
from typing import List
from tqdm import tqdm

cwd = os.getcwd()

this_dir = Path(__file__).parent
input_file = this_dir / 'input.txt'

with input_file.open('r') as file:
    lines = file.readlines()

constraint_lines = []
update_lines = []
for line in lines:
    if line.__contains__('|'):
        constraint_lines.append(line.replace('\n',''))
    if line.__contains__(','):
        update_lines.append(line.replace('\n',''))
constraints = [line.split('|') for line in constraint_lines]
print(constraints)
print(update_lines)

print(f'{len(update_lines)} updates')

def is_correct_update(update: List[str]) -> bool:
    for i, a in enumerate(update):
        for b in update[i+1:]:
            for constraint in constraints:
                if constraint[0] == b and constraint[1] == a:
                    return False
    return True


correct_updates= []
incorrect_updates = []
for update_line in update_lines:
    update = update_line.split(',')
    # print(f'Checking update {update}')
    if is_correct_update(update):
        correct_updates.append(update)
    else:
        incorrect_updates.append(update)
print(f'{len(correct_updates)} correct updates')
print(f'{len(incorrect_updates)} incorrect updates')

total = 0
for update in correct_updates:
        length = len(update)
        middle_index = math.floor(length/2)
        total += int(update[middle_index])
print(total)


def fix_update(update: List[str]):
    if len(update) == 1:
        return update
    most_constrains = 0
    most_constrained = update[0]
    for first in update:
        n_constraints = 0
        for second in update:
            if constraints.__contains__([first, second]):
                n_constraints += 1
        if n_constraints > most_constrains:
            most_constrains = n_constraints
            most_constrained = first
    rest = update.copy()
    rest.remove(most_constrained)
    return [most_constrained] +  fix_update(rest)

fixed_updates = []
for incorrect_update in incorrect_updates:
    # print(f'Fixing {incorrect_update}')
    fixed_update = fix_update(incorrect_update)
    fixed_updates.append(fixed_update)

new_total = 0
for update in fixed_updates:
        length = len(update)
        middle_index = math.floor(length/2)
        new_total += int(update[middle_index])
print(new_total)
