from lib.config import DEBUG_MODE, TEST_MODE

def log(string):
    global DEBUG_MODE
    if DEBUG_MODE:
        print(string)

def get_input(number):
    in_str = ''
    dir = "test" if TEST_MODE else "inputs"
    fname = f"../{dir}/{number}.txt"
    with open(fname, 'r') as f:
        in_str = f.read()

    log(f"Read Input from {fname}:")
    log(in_str)
    return in_str.string('\n')

# TODO(carter): Fix this
def get_input_by_lines(number):
    in_str = get_input(number)
    return (
        [instr for instr in line.split(',')]
        for line in in_str.strip('\n').split('\n') if line
    )
