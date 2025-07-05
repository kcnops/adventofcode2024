import os
from pathlib import Path

from day15.models import Wall, Robot, Box
from day15.parse import parse

cwd = os.getcwd()

this_dir = Path(__file__).parent
input_file = this_dir / 'input.txt'

with input_file.open('r') as file:
    lines = file.readlines()

field, moves, robot = parse(lines)

print(field.__str__())

for move in moves:
    print(f'Move: {move}')
    objects_to_move = [robot]
    pos_x = robot.location[0]
    pos_y = robot.location[1]
    while True:
        pos_x += move[0]
        pos_y += move[1]
        obj = field.get_object_at_location(pos_x, pos_y)
        if isinstance(obj, Wall):
            print('Not moving')
            break
        elif obj is None:
            print(f'Lets move! {objects_to_move}')
            objects_to_move.reverse()
            for obj_to_move in objects_to_move:
                field.move_object(obj_to_move, move)
            break
        elif isinstance(obj, Robot):
            raise ValueError('Robot running into robot !?')
        elif isinstance(obj, Box):
            objects_to_move.append(obj)
    print(field.__str__())

print(field.get_coordinate_sum())