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

equations = []
for line in lines:
    line = line.replace('\n','')
    parts = line.split(': ')
    test_value = int(parts[0])
    numbers_str = parts[1].split(' ')
    numbers = [int(number) for number in numbers_str]
    equations.append((test_value,numbers))

def is_true_equation(test_value: int, evaluated_so_far: int, numbers: List[int]) -> int:
    if len(numbers) == 0:
        return test_value == evaluated_so_far
    new_eval_plus = evaluated_so_far + numbers[0]
    new_eval_mult = evaluated_so_far * numbers[0]
    return (
            is_true_equation(test_value, new_eval_plus, numbers[1:])
            or
            is_true_equation(test_value, new_eval_mult, numbers[1:])
    )

def is_true_equation_2(test_value: int, evaluated_so_far: int, numbers: List[int]) -> int:
    if len(numbers) == 0:
        return test_value == evaluated_so_far
    new_eval_plus = evaluated_so_far + numbers[0]
    new_eval_mult = evaluated_so_far * numbers[0]
    new_eval_conc = int(str(evaluated_so_far) + str(numbers[0]))
    return (
            is_true_equation_2(test_value, new_eval_plus, numbers[1:])
            or
            is_true_equation_2(test_value, new_eval_mult, numbers[1:])
            or
            is_true_equation_2(test_value, new_eval_conc, numbers[1:])
    )


total = 0
for (test_value, numbers) in equations:
    if is_true_equation(test_value, numbers[0], numbers[1:]):
        # print(f'{test_value}: {numbers}')
        total += test_value

print(total)

total = 0
for (test_value, numbers) in equations:
    if is_true_equation_2(test_value, numbers[0], numbers[1:]):
        # print(f'{test_value}: {numbers}')
        total += test_value

print(total)




