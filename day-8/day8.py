from functools import partial
import sys
sys.setrecursionlimit(10000)

accumulator = 0
lines_index = []
lines = []
start_loop = False
swap_history = []
already_swapped = False


def tick_accumulator(num, index):
    global accumulator
    accumulator += eval(num)
    parse_code(index+1)


def skip_to_line(jump, index):
    parse_code(index+eval(jump))


def do_nothing(_, index):
    parse_code(index+1)


OPERATIONS = {
    'acc': partial(tick_accumulator),
    'jmp': partial(skip_to_line),
    'nop': partial(do_nothing)
}


def run(file):
    global lines
    with open(file) as file:
        lines = [line.strip() for line in file.readlines()]
    parse_code()


def swap_instructions(operation):
    swap = {
        'jmp': 'nop',
        'nop': 'jmp'
    }
    global already_swapped
    already_swapped = True
    return swap[operation]


def log_swap(idx):
    global swap_history
    swap_history.append(idx)


def parse_code(index=0):
    global accumulator
    global start_loop
    check_if_seen(index)
    if index == len(lines):
        print(
            f"Value in the accumulator at the end: {accumulator}")
        return
    if start_loop:
        restart()
    else:
        execute_instructions(index)


def restart():
    reset_global_values()
    parse_code()


def reset_global_values():
    global accumulator
    accumulator = 0
    global lines_index
    lines_index = []
    global start_loop
    start_loop = False
    global already_swapped
    already_swapped = False


def execute_instructions(index):
    global already_swapped
    global lines
    global swap_history
    global lines_index
    operation = lines[index][:3]
    if not already_swapped:
        if (operation != 'acc') and (index not in swap_history):
            operation = swap_instructions(operation)
            log_swap(index)
    value = lines[index][4:]
    OPERATIONS[operation](value, index)


def check_if_seen(index):
    global lines_index
    global start_loop
    current_index = index
    if current_index in lines_index:
        start_loop = True
    else:
        lines_index.append(current_index)


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Run Advent of Code Day 8')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        run(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
