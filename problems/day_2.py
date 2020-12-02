from parse import parse
from lib.helpers import log, get_strings_by_lines

def part_1():
    input_arr = get_strings_by_lines('2.txt')
    valid_count = 0

    # Loop through every pair in the array
    for input in input_arr:
        min, max, char, password = parse('{:d}-{:d} {:l}: {:w}', input)
        count = password.count(char)
        log(f"Testing {password} for {min} to {max} {char}'s")

        if min <= count <= max:
            log(f"\tYES")
            valid_count += 1
        else:
            log(f"\tNO")

    return valid_count

def part_2():
    input_arr = get_strings_by_lines('2.txt')
    valid_count = 0

    # Loop through every pair in the array
    for input in input_arr:
        idx_a, idx_b, char, password = parse('{:d}-{:d} {:l}: {:w}', input)
        count = password.count(char)
        log(f"Testing {password} for {char} at indexes {idx_a} and {idx_b}")

        # convert from indexing at 0 to indexing at 1
        # And cast to bools to use the exclusive or operator
        if bool(password[idx_a - 1] == char) ^ bool(password[idx_b - 1] == char):
            log(f"\tYES")
            valid_count += 1
        else:
            log(f"\tNO")

    return valid_count
