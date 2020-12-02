#!/bin/bash python
import argparse
import lib.config
import problems
import importlib

parser = argparse.ArgumentParser(prog="advent_of_code_2020")

# Positional Arguments (Day and Part)
parser.add_argument("day", type=int, help="Which advent day?")
parser.add_argument("part", type=int, help="Which part of this day to run?")

# Optional Arguments (Test mode and Debug mode)
parser.add_argument("-t", "--test", help="Run with test inputs", action="store_true")
parser.add_argument("-d", "--debug", help="Run with logging", action="store_true")

# Parse arguments
args = parser.parse_args()

# Set global state
lib.config.DEBUG_MODE = args.debug
lib.config.TEST_MODE = args.test

# Import helper functions
from lib.helpers import log

if __name__ == "__main__":
    # import the library dynamically
    lib_name = f"problems.day_{args.day}"
    solver = importlib.import_module(lib_name)

    # Choose day 1 or day 2
    if args.part == 1:
        print(solver.part_1())
    elif args.part == 2:
        print(solver.part_2())
    else:
        print(solver.part_1())
        print(solver.part_2())

    log("hello world")
