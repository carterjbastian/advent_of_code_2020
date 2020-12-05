import math
from lib.helpers import log, get_strings_by_lines

FIRST_HALF_INSTR = ['F', 'L']
SECOND_HALF_INSTR = ['B', 'R']

def bin_search(value, string):
    if string[0] in FIRST_HALF_INSTR:
        # Base Case
        if len(string) == 1:
            return 0
        # Recurse on first half of the values
        return 0 + bin_search(math.ceil(value / 2), string[1:])
    elif string[0] in SECOND_HALF_INSTR:
        # Base Case
        if len(string) == 1:
            return 1
        # Recurse on the second half of the values
        return math.ceil(value/2) + bin_search(math.ceil(value/2) - 1, string[1:])

def part_1():
    boarding_passes = get_strings_by_lines('5.txt')
    max = 0
    for bp in boarding_passes:
        row = bin_search(127, bp[:7])
        col = bin_search(8, bp[7:])
        id = (row * 8) + col
        if id > max:
            max = id

    return max

def part_2():
    boarding_passes = get_strings_by_lines('5.txt')
    ids = []
    for bp in boarding_passes:
        row = bin_search(127, bp[:7])
        col = bin_search(8, bp[7:])
        ids += [(row * 8) + col]

    ids.sort()
    log(ids)

    for idx in range(1, len(ids)):
        # Did we skip a number?
        if ids[idx] - ids[idx-1] != 1:
            return ids[idx] - 1  # Return the skipped number

    return None
