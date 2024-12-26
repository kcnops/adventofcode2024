import os
from pathlib import Path
from typing import List

cwd = os.getcwd()

this_dir = Path(__file__).parent
input_file = this_dir / 'input.txt'

with input_file.open('r') as file:
    lines = file.readlines()


def is_same_side(a: int, b: int):
    return a*b>0


def is_safe_report(levels: List[str]) -> bool:
    first_diff = int(levels[1]) - int(levels[0])
    for x, y in zip(levels, levels[1:]):
        x = int(x)
        y = int(y)
        if abs(x-y) > 3:
            print(f'Found unsafe list: {levels} cause step too high')
            return False
        if abs(x-y) < 1:
            print(f'Found unsafe list: {levels} cause no step')
            return False
        diff = y-x
        if not is_same_side(diff, first_diff):
            print(f'Found unsafe list: {levels} cause not unidirectional')
            return False
    print(f'Found safe list: {levels}')
    return True


def is_safe_report_with_dampening(levels: List[str]) -> bool:
    if is_safe_report(levels):
        return True
    print(f'original list: {levels}')
    for i, level in enumerate(levels):
        partial_levels = levels.copy()
        del partial_levels[i]
        print(f'checking partial list: {partial_levels}')
        if is_safe_report(partial_levels):
            return True
    return False


n_safe_reports = 0
n_safe_reports_dampened = 0
for line in lines:
    splits = line.replace('\n', '').split(' ')
    if is_safe_report(splits):
        n_safe_reports += 1
    if is_safe_report_with_dampening(splits):
        n_safe_reports_dampened += 1

print(n_safe_reports)
print(n_safe_reports_dampened)


