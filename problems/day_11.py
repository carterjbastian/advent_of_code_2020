from parse import parse
from lib.helpers import log, get_strings_by_lines

def print_grid(grid):
    for row in grid:
        log(''.join(row))

def count_grid(grid):
    count = 0
    for row in grid:
        for char in row:
            count += 1 if char == '#' else 0
    return count

def occupied_in_direction(grid, x, y, dx, dy):
    x_max = len(grid[0]) - 1
    y_max = len(grid) - 1

    x += dx
    y += dy

    while 0 <= x <= x_max and 0 <= y <= y_max:
        if grid[y][x] == '#':
            return 1
        elif grid[y][x] == 'L':
            return 0
        else:
            x += dx
            y += dy

    return 0  # Hit an edge

def count_visibility(grid, row, col):
    visibility = [
        occupied_in_direction(grid, col, row, -1, -1),
        occupied_in_direction(grid, col, row, -1, 0),
        occupied_in_direction(grid, col, row, -1, 1),
        occupied_in_direction(grid, col, row, 0, -1),
        occupied_in_direction(grid, col, row, 0, 1),
        occupied_in_direction(grid, col, row, 1, -1),
        occupied_in_direction(grid, col, row, 1, 0),
        occupied_in_direction(grid, col, row, 1, 1),
    ]
    return sum(visibility)

def count_surrounding(grid, row, col):
    col_max = len(grid[0]) - 1
    row_max = len(grid) - 1
    count = 0

    # Check Previous Row
    if row >= 1:
        count += 1 if grid[row - 1][col] == '#' else 0
        if col >= 1:
            count += 1 if grid[row - 1][col - 1] == '#' else 0
        if col < col_max:
            count += 1 if grid[row - 1][col + 1] == '#' else 0

    # Check Next Row
    if row < row_max:
        count += 1 if grid[row + 1][col] == '#' else 0
        if col >= 1:
            count += 1 if grid[row + 1][col - 1] == '#' else 0
        if col < col_max:
            count += 1 if grid[row + 1][col + 1] == '#' else 0

    # Check current row
    if col >= 1:
        count += 1 if grid[row][col - 1] == '#' else 0
    if col < col_max:
        count += 1 if grid[row][col + 1] == '#' else 0

    return count

def iterate(grid, use_surroundings):
    threshold = 4 if use_surroundings else 5
    changed = False
    copy = [[None] * len(grid[0]) for _ in range(len(grid))]
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            # Use one of our two counting functions
            if use_surroundings:
                count = count_surrounding(grid, row, col)
            else:
                count = count_visibility(grid, row, col)

            if grid[row][col] == '.':
                copy[row][col] = '.'
            elif grid[row][col] == 'L':
                if count == 0:
                    copy[row][col] = '#'
                    changed = True
                else:
                    copy[row][col] = 'L'
            elif grid[row][col] == '#':
                if count >= threshold:
                    copy[row][col] = 'L'
                    changed = True
                else:
                    copy[row][col] = '#'
            else:
                log(f'PROBLEM CHARACTER: {grid[row][col]}')

    return copy, changed

def part_1():
    grid = [
        [char for char in line] for line in get_strings_by_lines('11.txt')
    ]
    changed = True
    iterations = 0

    while changed:
        grid, changed = iterate(grid, True)
        iterations += 1
        log(f"iterated {iterations} times")

    print_grid(grid)

    return count_grid(grid)

def part_2():
    grid = [
        [char for char in line] for line in get_strings_by_lines('11.txt')
    ]
    changed = True
    iterations = 0
    print_grid(grid)

    while changed:
        grid, changed = iterate(grid, False)
        iterations += 1
        log(f"iterated {iterations} times")

    print_grid(grid)
    return count_grid(grid)
