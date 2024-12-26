import os
import re
from pathlib import Path

cwd = os.getcwd()

this_dir = Path(__file__).parent
input_file = this_dir / 'input.txt'

with input_file.open('r') as file:
    lines = file.readlines()


# We are looking for "mul(aaa,bbb)" where aaa & bbb are numbers with up to 3 digits

total = 0
for line in lines:
    # print(line)
    muls = re.findall(pattern=r'mul\((\d{1,3}),(\d{1,3})\)', string=line)
    # print(muls)
    for mul in muls:
        # print(f'processing {mul}')
        total += int(mul[0]) * int(mul[1])
print(total)

total = 0
for line in lines:
    # print(line)
    muls = re.findall(pattern=r'mul\((?:\d{1,3}),(?:\d{1,3})\)', string=line)
    # print(muls)
    for mul in muls:
        # print(f'processing {mul}')
        numbers = mul.replace('mul(','').replace(')','').split(',')
        total += int(numbers[0]) * int(numbers[1])
print(total)

total = 0
active = None
for line in lines:
    print(line)
    matches = re.findall(pattern=r'mul\((?:\d{1,3}),(?:\d{1,3})\)|do\(\)|don\'t\(\)', string=line)
    print(matches)
    for match in matches:
        print(f'processing {match}')
        if match == 'do()':
            active = True
            continue
        if match == 'don\'t()':
            active = False
            continue
        # match is mul
        if not active:
            continue
        print(f'actual processing {match}')
        numbers = match.replace('mul(','').replace(')','').split(',')
        total += int(numbers[0]) * int(numbers[1])
print(total)

