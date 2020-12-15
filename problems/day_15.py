from parse import parse
from lib.helpers import log, get_strings_by_lines
from lib.config import TEST_MODE

list = [0,3,6] if TEST_MODE else [0,14,6,20,1,4]
contained = {}

def compute_list(limit):
    global contained

    # Build the contained dict so far
    idx = 0
    while idx < len(list) - 1:
        contained[list[idx]] = idx
        idx += 1
    curr = list[-1]

    # Iterate upwards until we hit our limit
    while idx < limit - 1:
        if curr in contained:
            next = idx - contained[curr]
        else:
            next = 0
        contained[curr] = idx

        curr = next
        idx += 1

    return curr

def part_1():
    return compute_list(2020)

def part_2():
    return compute_list(30000000)
