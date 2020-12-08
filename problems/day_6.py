import math
from lib.helpers import log, get_input


def part_1():
    groups = get_input('6.txt').split('\n\n')
    grouped_people = [
        group.split('\n') for group in groups
    ]

    count = 0
    for group in grouped_people:
        pset = ''.join(set(''.join(group)))
        log(pset)
        count += len(pset)

    return count

def part_2():
    groups = get_input('6.txt').split('\n\n')
    grouped_people = [
        group.split('\n') for group in groups
    ]

    # Loop through each group, intersecting the sets
    count = 0
    for group in grouped_people:
        shared = set('abcdefghijklmnopqrstuvwxyz')
        psets = [ set(person) for person in group ]
        intersection = ''.join(shared.intersection(*psets))
        count += len(intersection)

    return count
