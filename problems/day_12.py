from parse import parse
from lib.helpers import log, get_strings_by_lines

directions = [
    'E',
    'S',
    'W',
    'N'
]

def rotate(current, degrees):
    rotations = degrees / 90
    idx = directions.index(current)
    return directions[int((idx + rotations) % 4)]

def rotate_waypoint(wx, wy, degrees):
    rotations = int((degrees / 90) % 4)
    for _ in range(rotations):
        wx, wy = wy, -1 * wx
    return wx, wy

def handle_instruction(x, y, dir, instr_str):
    instr, amount = instr_str[0], int(instr_str[1:])
    log(instr)
    log(amount)

    if instr == 'E':
        x += amount
    elif instr == 'N':
        y += amount
    elif instr == 'W':
        x -= amount
    elif instr == 'S':
        y -= amount
    elif instr == 'R':
        dir = rotate(dir, amount)
    elif instr == 'L':
        dir = rotate(dir, -1 * amount)
    elif instr == 'F':
        x, y, dir = handle_instruction(x, y, dir, dir + str(amount))

    return x, y, dir

def handle_instruction_with_waypoint(x, y, wx, wy, instr_str):
    instr, amount = instr_str[0], int(instr_str[1:])

    if instr == 'E':
        wx += amount
    elif instr == 'N':
        wy += amount
    elif instr == 'W':
        wx -= amount
    elif instr == 'S':
        wy -= amount
    elif instr == 'R':
        wx, wy = rotate_waypoint(wx, wy, amount)
    elif instr == 'L':
        wx, wy = rotate_waypoint(wx, wy, -1 * amount)
    elif instr == 'F':
        x += (wx * amount)
        y += (wy * amount)

    return x, y, wx, wy

def part_1():
    x, y, dir = 0, 0, 'E'
    log(f"({x}, {y}, {dir})")
    for instr_str in get_strings_by_lines('12.txt'):
        x, y, dir = handle_instruction(x, y, dir, instr_str)
        log(f"({x}, {y}, {dir})")

    return abs(x) + abs(y)

def part_2():
    x, y, wx, wy = 0, 0, 10, 1
    log(f"({x}, {y}), ({wx}, {wy})")
    for instr_str in get_strings_by_lines('12.txt'):
        x, y, wx, wy = handle_instruction_with_waypoint(x, y, wx, wy, instr_str)
        log(f"({x}, {y}), ({wx}, {wy})")

    return abs(x) + abs(y)
