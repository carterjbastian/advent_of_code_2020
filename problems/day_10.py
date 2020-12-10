from lib.helpers import log, get_ints_by_lines

def part_1():
    jolts = [0] + sorted(get_ints_by_lines('10.txt'))
    jolts += [jolts[-1] + 3]

    log(jolts)

    diffs = [0, 0, 0, 0]
    for idx in range(1, len(jolts)):
        d = jolts[idx] - jolts[idx - 1]
        diffs[d] += 1

    log(diffs)

    return diffs[1] * diffs[3]

cache = {} # Cache lists we've seen before
def recursive_get_lists(remaining_jolts):
    # Base Case: Only one item means only one arrangement
    if (len(remaining_jolts) <= 1):
        return 1

    # Try getting the answer from cache
    if str(remaining_jolts) in cache:
        return cache[str(remaining_jolts)]

    # Recursive case: recurse on possible next steps and sum their results
    arrangements = 0
    curr = remaining_jolts[0]
    for idx in range(1, len(remaining_jolts)):
        if remaining_jolts[idx] - curr <= 3:
            new_options = recursive_get_lists(remaining_jolts[idx:])
            arrangements += new_options
        else:
            break # Quit the whole loop early (it's sorted)

    cache[str(remaining_jolts)] = arrangements  # Cache the answer for this list
    return arrangements


def part_2():
    jolts = [0] + sorted(get_ints_by_lines('10.txt'))
    jolts += [jolts[-1] + 3]

    arrangements = recursive_get_lists(jolts)
    return arrangements
