from parse import parse
from lib.helpers import log, get_input

REQUIRED_CREDENTIALS = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid"
]

EYE_COLORS = [
    "amb",
    "blu",
    "brn",
    "gry",
    "grn",
    "hzl",
    "oth"
]

def build_passport(passport_string):
    sub_strings = passport_string.split()
    values = [
        parse('{:w}:{:S}', str_pair)
        for str_pair in sub_strings if str_pair != '  '
    ]
    return {code: value for (code, value) in values}


def validate_passport(ppt):
    try:
        # Check Birth Year
        if not 1920 <= int(ppt['byr']) <= 2002:
            return False

        # Issue Year
        if not 2010 <= int(ppt['iyr']) <= 2020:
            return False

        # Eye Color
        if not 2020 <= int(ppt['eyr']) <= 2030:
            return False

        # Height
        if ppt['hgt'][-2:] == 'cm':
            if not 150 <= int(ppt['hgt'][:-2]) <= 193:
                return False
        elif ppt['hgt'][-2:] == 'in':
            if not 59 <= int(ppt['hgt'][:-2]) <= 76:
                return False
        else:
            return False

        # Hair Color
        if len(ppt['hcl']) == 7:
            if ppt['hcl'][0] != '#':
                return False
            for char in ppt['hcl'][1:]:
                if char not in 'abcdef0123456789':
                    return False
        else:
            return False

        # Eye Color
        if len(ppt['pid']) != 9:
            return False
        if not 0 <= int(ppt['pid']) <= 999999999:
            return False

        if ppt['ecl'] not in EYE_COLORS:
            return False

    except:  # One of the int conversions failed
        return False

    return True


def part_1():
    rows = get_input('4.txt')
    passport_strings = [
        passport.replace('\n', ' ') for passport in rows.split('\n\n')
    ]
    objects = [ build_passport(string) for string in passport_strings ]

    count = 0
    for obj in objects:
        complete = True
        for field in REQUIRED_CREDENTIALS:
            if field not in obj:
                complete = False

        if complete:
            count += 1

    return count

def part_2():
    rows = get_input('4.txt')

    passport_strings = [
        passport.replace('\n', ' ') for passport in rows.split('\n\n')
    ]
    objects = [ build_passport(string) for string in passport_strings ]

    count = 0
    for obj in objects:
        complete = True
        for field in REQUIRED_CREDENTIALS:
            if field not in obj:
                complete = False

        if complete:
            if validate_passport(obj):
                count += 1

    return count
