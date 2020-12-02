from lib.helpers import log, get_ints_by_lines

def part_1():
    input_arr = get_ints_by_lines('1.txt')
    # Loop through every pair in the array
    for x in range(0, len(input_arr)):
        for y in range(x + 1, len(input_arr)):
            val1, val2 = input_arr[x], input_arr[y]
            if val1 + val2 == 2020:
                log(f"{val1} + {val2} = {val1 + val2} (returning {val1 * val2})")
                return val1 * val2

    log('No solution')

def part_2():
    input_arr = get_ints_by_lines('1.txt')
    for x in range(0, len(input_arr)): 
        for y in range(x + 1, len(input_arr)):
            for z in range(y + 1, len(input_arr)):
                val1, val2, val3 = input_arr[x], input_arr[y], input_arr[z]
                if val1 + val2 + val3 == 2020:
                    log(f"{val1} + {val2} + {val3} = {val1 + val2 + val3}")
                    return val1 * val2 * val3

    log('No solution')
