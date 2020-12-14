from parse import parse
from lib.helpers import log, get_strings_by_lines
from lib.config import TEST_MODE

def part_1():
    earliest, bus_list = get_strings_by_lines('13.txt')
    current_time = int(earliest)
    busses = [ int(bus) for bus in bus_list.split(',') if bus and bus != 'x']
    while True:
        log(f'Testing: {current_time}')
        for bus in busses:
            if current_time % bus == 0:
                log('FOUND IT')
                return (current_time - int(earliest)) * bus
        current_time += 1

def part_2():
    earliest, bus_list = get_strings_by_lines('13.txt')
    busses = [ bus for bus in bus_list.split(',') if bus ]

    # Fulfill the constraints one at a time - Once you find a number satisfying
    # Two divisors, future values must be a multiple of that value.
    # AKA for divisors w,x,y,z the minimum value satisfying y must be
    #   <the minimum value satisfying w,x> + (w * x)
    # And then the minimum value satisfying z must be
    #   <the minimum value satisfying w,x,y> + (w * x * y)
    # ETC.
    current_time = 0
    inc = 1
    for idx in range(len(busses)):
        if busses[idx] == 'x':
            log(f'Skipping idx {idx}')
            continue
        curr_bus = int(busses[idx])

        while (current_time + idx) % curr_bus != 0:
            current_time += inc

        log(f'constraint fulfilled! {curr_bus}')
        inc *= curr_bus
        log(f'New Inc: {inc}')

    return current_time
