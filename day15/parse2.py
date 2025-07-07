from day15.models2 import Wall, Robot, Box, Field


def parse(lines):
    width = 0
    parsing_moves = False
    objects = []
    moves = []

    for y, line in enumerate(lines):
        line = line.replace('\n', '')
        if line == '':
            height = y
            field = Field(width=width, height=height)
            for obj in objects:
                field.add_object(obj)
            parsing_moves = True
            continue

        if parsing_moves:
            # parse moves
            for ch in line:
                if ch == '<':
                    moves.append((-1,0))
                elif ch == '>':
                    moves.append((1, 0))
                elif ch == 'v':
                    moves.append((0, 1))
                elif ch == '^':
                    moves.append((0, -1))

        else:
            # Parse field
            if width == 0:
                width = 2*len(line)
            for x, ch in enumerate(line):
                if ch == '#':
                    objects.append(Wall(2*x, y))
                    objects.append(Wall(2*x+1, y))
                elif ch == 'O':
                    objects.append(Box(2*x, y))
                    # objects.append(Box(2*x+1, y))
                elif ch == '@':
                    robot = Robot(2*x,y)
                    objects.append(robot)

    if robot is None:
        raise ValueError('No robot found!')

    return field, moves, robot