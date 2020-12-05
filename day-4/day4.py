import itertools
import pprint
pp = pprint.PrettyPrinter(indent=4)
keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']


def run(file):
    with open(file) as file:
        rows = []
        for line in file:
            rows.append(line.split())
        # passport_data = [line.strip() for line in file if line.strip()]
        # data.append(passport_data)
        passport_data = []
        valid_passport_counter = 0
        for item in process_data(rows):
            passport_data.append(list(itertools.chain(*item)))
        pp.pprint(passport_data)
    passports = []
    for passport in passport_data:
        passports.append(create_passport(passport))
    pp.pprint(passports)


def create_passport(passport_data):
    passport = {}
    for string in passport_data:
        passport[string[:3]] = string[4:]
    return passport


def process_data(rows):
    data = []
    tmp = []
    for i, row in enumerate(rows.copy()):
        print(f"the i is {i} and the row is {row}")
        # on the first line, start a temporary data variable
        if row:
            # keep adding to that temp variable
            tmp.append(row)
        elif not row:
            # then we want to add the temp data var to a data list
            data.append(tmp)
        # and reset the temp var to ''
            tmp = []
    # print(data)
    return data


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Validate passports for Advent of Code 2020 Day 4.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        run(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
