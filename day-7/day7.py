import pprint
import re

pp = pprint.PrettyPrinter(indent=4)

# {'bright white': {'shiny gold': '1'},
#     'dark olive': {'dotted black': '4', 'faded blue': '3'},
#     'dark orange': {'bright white': '3', 'muted yellow': '4'},
#     'dotted black': {},
#     'faded blue': {},
#     'light red': {'bright white': '1', 'muted yellow': '2'},
#     'muted yellow': {'faded blue': '9', 'shiny gold': '2'},
#     'shiny gold': {'dark olive': '1', 'vibrant plum': '2'},
#     'vibrant plum': {'dotted black': '6', 'faded blue': '5'}}
RULES = {}
target = 'shiny gold'


def run(file):
    with open(file) as file:
        lines = [line.strip() for line in file.readlines()]
    define_bag_rules(lines)
    find_bag(target)


def define_bag_rules(lines):
    """
    Assign a value to constant BAGS as dictionary in the following format:
    { 'bright white': {'shiny gold': '1'},  'dotted black': {}}
    """
    for line in lines:
        new_line = line.partition('contain')
        key = re.split(r'\sbags?', new_line[0])[0]
        RULES[key] = {}
        contained_bags = new_line[-1].strip().split(', ')

        for bag in contained_bags:
            if 'no other' in bag:
                continue
            nested_key = re.split(r'\sbags?', bag[2:])[0]
            value = bag[:1]
            RULES[key][nested_key] = value


def find_bag(bag):
    counter = 0
    for key in RULES:
        if find_bag_recursive(key, bag):
            counter += 1

    pp.pprint(f"Number of bags that contain the {target} bag is: {counter}")


def find_bag_recursive(key, inner_bag):
    if RULES[key]:
        for bag in RULES[key].keys():
            if bag == inner_bag:
                return True
            if find_bag_recursive(bag, inner_bag):
                return True
    return False


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Run Advent of Code Day 7, now with RECURSION')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        run(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
