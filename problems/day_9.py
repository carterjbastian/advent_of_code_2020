from parse import parse
from lib.helpers import log, get_ints_by_lines
from lib.config import TEST_MODE

PREAMBLE_LEN = 5 if TEST_MODE else 25

def in_preamble(search_arr, value):
    log(search_arr)
    log(value)
    for i in range(len(search_arr) - 1):
        for j in range(i + 1, len(search_arr)):
            if search_arr[i] + search_arr[j] == value:
                log(f'found: {search_arr[i]}, {search_arr[j]}')
                return True
    return False

def part_1():
    code = get_ints_by_lines('9.txt')
    log(code)

    for idx in range(PREAMBLE_LEN, len(code)):
        log(f"checking {idx}")
        if not in_preamble(code[idx - PREAMBLE_LEN:idx], code[idx]):
            log(f"Found {code[idx]} at idx {idx}")
            return code[idx]
    return None

def part_2():
    code = get_ints_by_lines('9.txt')
    goal = part_1()

    for idx in range(len(code)):
        list = []
        sub_idx = idx
        total = 0
        while total < goal and sub_idx < len(code):
            total += code[sub_idx]
            list += [code[sub_idx]]
            sub_idx += 1

        if total == goal:
            log('FOUND IT')
            log(list)
            return min(list) + max(list)

    return None
