from validator import PassportValidator
import itertools
import pprint
pp = pprint.PrettyPrinter(indent=4)
keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']


def run(file):
    with open(file) as file:
        rows = []
        for line in file:
            rows.append(line.split())
        passport_data = []
        valid_passport_counter = 0
        for item in process_data(rows):
            # flatten the list
            passport_data.append(list(itertools.chain(*item)))
        # pp.pprint(passport_data)
    passports = []
    for passport in passport_data:
        passports.append(create_passport(passport))
    pp.pprint(len(passports))
    validate_passports(filter_invalid_passports(passports))


def filter_invalid_passports(passports):
    counter = 0
    valid_passports = []
    for passport in passports:
        if len(passport.keys()) == 8:
            counter += 1
            valid_passports.append(passport)
        if len(passport.keys()) == 7 and 'cid' not in passport.keys():
            counter += 1
            valid_passports.append(passport)
    print(counter)
    return valid_passports


def validate_passports(passports):
    validity_states = []
    for passport in passports:
        validity_states.append(PassportValidator.validate(passport))
    print(f"Array of all validity states: {validity_states}")
    print(f"Length all validity states: {len(validity_states)}")
    print(f"Count of all valid passports: {validity_states.count(True)}")


def create_passport(passport_data):
    passport = {}
    for string in passport_data:
        passport[string[:3]] = string[4:]
    return passport


def process_data(rows):
    data = []
    tmp = []
    for row in rows.copy():
        if row:
            # keep adding to that temp variable
            tmp.append(row)
        elif not row:
            # then we want to add the temp data var to a data list
            data.append(tmp)
            # and reset the temp var
            tmp = []
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
