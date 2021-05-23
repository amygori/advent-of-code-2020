from functools import partial

accumulator = 0
lines_index = []
lines = []
done = False


def tick_accumulator(num, index):
    print(f"hello from the accumulator, adding {num}")
    global accumulator
    accumulator += eval(num)
    print(f"Now accumulator is: ", accumulator)
    parse_code(index+1)


def skip_to_line(jump, index):
    print(f"SKIP_TO_LINE, index is: ", index)
    print(f"And jump is: ", jump)
    parse_code(index+eval(jump))


def do_nothing(_, index):
    print(f"DO_NOTHING. index is:", index)
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
    print("Lines:", lines)
    parse_code(0)


def parse_code(index=0):
    print("PARSE_CODE, index: ", index)
    global lines
    check_lines(index)
    if done:
        print(f"Here is the value in the accumulator: {accumulator}")
    else:
        execute_instructions(index)


def execute_instructions(index):
    operation = lines[index][:3]
    value = lines[index][4:]
    OPERATIONS[operation](value, index)


def check_lines(index):
    print("CHECK_LINES, index: ", index)
    global lines
    global lines_index
    global done
    if not lines:
        return False
    index_of_instruction = index
    if index_of_instruction in lines_index:
        done = True
    else:
        lines_index.append(index_of_instruction)
    print(f"Lines index: ", lines_index)


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
