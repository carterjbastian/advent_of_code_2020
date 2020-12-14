from parse import parse
from lib.helpers import log, get_strings_by_lines
from lib.config import TEST_MODE


def set_bitmask(new_mask_string):
    # Split mask into and-mask and or-mask
    # All the 0s go into the "And Mask" (because anding with 0 overwrites - 00 && 11 = 00)
    log(f'Setting bitmask: {new_mask_string}')
    and_mask = ''
    for char in new_mask_string:
        if char == '0':
            and_mask += '0'
        else:
            and_mask += '1'
    # All the 1s go into the "Or Mask" (because oring with 1 overwrites - 11 || 00 = 11)
    or_mask = ''
    for char in new_mask_string:
        if char == '1':
            or_mask += '1'
        else:
            or_mask += '0'

    log(f'\tAND MASK: {and_mask}')
    log(f'\tOR MASK: {or_mask}')
    return int(and_mask, 2), int(or_mask, 2)

def set_register(memory, address, value, and_mask, or_mask):
    log(f'value: {format(value, "036b")}')
    log(f'and_mask: {format(and_mask, "036b")}')
    log(f'or_mask: {format(or_mask, "036b")}')
    log(f'result: {format(((value & and_mask) | or_mask), "036b")}')
    memory[address] = (value & and_mask) | or_mask
    return memory

def write_value_to_decoded_registers(memory, address, mask_string, value):
    og_address = format(address, '036b')
    addresses = ['']
    for idx in range(1, len(mask_string) + 1):
        if mask_string[-1 * idx] == '1':
            addresses = [ '1' + address for address in addresses ]
        elif mask_string[-1 * idx] == '0':
            addresses = [ og_address[-1 * idx] + address for address in addresses ]
        elif mask_string[-1 * idx] == 'X':
            ones = [ '1' + address for address in addresses ]
            zeros = [ '0' + address for address in addresses ]
            addresses = ones + zeros
        else:
            log(f"PROBLEM")

    log(f"Writing to {len(addresses)} addresses")
    log(addresses)

    for address in addresses:
        memory[int(address, 2)] = value

    return memory

def part_1():
    instructions = get_strings_by_lines('14.txt')
    memory = {}
    and_mask, or_mask = 0, 0

    for inst in instructions:
        if inst[:4] == 'mask':
            (new_mask, ) = parse('mask = {}', inst)
            and_mask, or_mask = set_bitmask(new_mask)

        else:
            address, value = parse('mem[{:d}] = {:d}', inst)
            memory = set_register(memory, address, value, and_mask, or_mask)

    log(memory)
    return sum(memory.values())


def part_2():
    instructions = get_strings_by_lines('14.txt')
    memory = {}
    mask = ''

    for inst in instructions:
        if inst[:4] == 'mask':
            (mask, ) = parse('mask = {}', inst)
            log(f"set mask to {mask}")

        else:
            address, value = parse('mem[{:d}] = {:d}', inst)
            memory = write_value_to_decoded_registers(memory, address, mask, value)

    log(memory)
    return sum(memory.values())
    return None
