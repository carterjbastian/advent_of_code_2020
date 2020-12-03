from lib.helpers import log, get_strings_by_lines

def count_trees(rows, slope):
    dx, dy = slope
    x = 0
    tree_count = 0

    for y in range(0, len(rows), dy):
        log(f"coordinate: ({x}, {y}) Tree: {rows[y][x]}")
        tree_count += 1 if rows[y][x] == "#" else 0
        x = (x + dx) % len(rows[0])

    return tree_count

def part_1():
    rows = get_strings_by_lines('3.txt')
    x = 0
    tree_count = 0
    return count_trees(rows, (3, 1))

def part_2():
    rows = get_strings_by_lines('3.txt')
    x = 0

    tree_counts = [
        count_trees(rows, slope)
        for slope in [(1,1), (3,1), (5,1), (7,1), (1,2)]
    ]
    log(tree_counts)

    # return functools.reduce(lambda x, y: x*y, tree_counts)
    # Yeah, Robin, I know how to reduce stuff too

    product = 1
    for count in tree_counts:
        product *= count
    return product
