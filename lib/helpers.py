from lib.config import DEBUG_MODE, TEST_MODE

def log(string):
    global DEBUG_MODE
    if DEBUG_MODE:
        print(string)
    else:
        print("no global debug var")
