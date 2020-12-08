from parse import parse
from lib.helpers import log, get_strings_by_lines

def run_instr(instr, acc, pointer):
    command, sign, val = parse("{} {}{:d}", instr)
    if command == 'nop':
        return acc, pointer + 1
    elif command == 'acc':
        if sign == '+':
            return acc + val, pointer + 1
        elif sign == '-':
            return acc - val, pointer + 1
        else:
            log('PROBLEM VALUE')
    elif command == 'jmp':
        if sign == '+':
            return acc, pointer + val
        elif sign == '-':
            return acc, pointer - val
        else:
            log('PROBLEM JMP')
    else:
        log('PROBLEM INSTR')

    return acc, pointer

def part_1():
    instructions = get_strings_by_lines('8.txt')
    acc, pointer = 0, 0
    already_run = set()

    while pointer not in already_run:
        instr = instructions[pointer]
        already_run.add(pointer)
        acc, pointer = run_instr(instr, acc, pointer)

    return acc

def part_2():
    instructions = get_strings_by_lines('8.txt')
    for idx in range(len(instructions)):
        # Copy the instructions
        copy = [] + instructions
        log(f'trying flipping instruction {idx}')
        if instructions[idx][:3] == 'jmp':
            copy[idx] = 'nop' + instructions[idx][3:]
        elif instructions[idx][:3] == 'nop':
            copy[idx] = 'jmp' + instructions[idx][3:]
        else:
            log('skipping instr: ' + instructions[idx])

        acc, pointer = 0, 0
        already_run = set()

        while pointer not in already_run:
            instr = copy[pointer]
            already_run.add(pointer)
            acc, pointer = run_instr(instr, acc, pointer)

            if pointer == len(instructions):
                log(f'found it flipping idx {idx}')
                return acc

        log('Failed idx {idx}')

    return None
