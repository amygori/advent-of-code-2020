import itertools
import pprint

pp = pprint.PrettyPrinter(indent=4)


def run(file):
    with open(file) as file:
        lines = [line.strip() for line in file.readlines()]
        data = format_data(lines)
        count_answers(data)


def format_data(lines):
    data = []
    tmp = ''
    for idx, line in enumerate(lines):
        if line:
            # keep adding to that temp variable
            tmp += line
            if idx == len(lines) - 1:
                data.append(tmp)
        else:
            # then we want to add the temp data var to a data list
            data.append(tmp)
            # and reset the temp var
            tmp = ''
    return data


def count_answers(data):
    count = []
    for answer_set in data:
        unique_chars = list(set(answer_set))
        count.append(len(unique_chars))
    print(f"The sum of answers is {sum(count)}")


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Run Advent of Code Day 6')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        run(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
