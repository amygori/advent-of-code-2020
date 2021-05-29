from itertools import combinations

START_NUM = 25


def check_numbers(input):
    for enum in enumerate(input[START_NUM:], start=START_NUM):
        num = int(enum[1])
        idx = enum[0]
        pairs = list(combinations(input[idx - START_NUM: idx], 2))
        valid = False
        for pair in pairs:
            if int(pair[0]) + int(pair[1]) == int(num):
                valid = True
        if not valid:
            return num


def run(file):
    with open(file) as file:
        input = [line.strip() for line in file.readlines()]
        result = check_numbers(input)
        print(result)


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Run Advent of Code Day 9')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        run(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
