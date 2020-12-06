
def run(file):
    with open(file) as file:
        seat_codes = file.readlines()
        seat_codes = [seat_code.strip() for seat_code in seat_codes]
        seats = []
        for seat_code in seat_codes:
            seats.append(decode(seat_code))
        print(f"The highest seat number is {max(seats)}")
        find_my_seat(seats)


def decode(seat_code):
    row = parse_chars(seat_code[:-3])
    column = parse_chars(seat_code[-3:])
    seat_number = find_seat_number(row, column)
    return seat_number


def parse_chars(code):
    start = 0
    stop = 127 if 'F' in code or 'B' in code else 7
    for char in code:
        take_lower = char == 'F' or char == 'L'
        take_upper = char == 'B' or char == 'R'
        midpoint = (stop + start) // 2
        if take_lower:
            stop = midpoint
        if take_upper:
            start = midpoint
    return stop


def find_my_seat(seats):
    sorted_seats = sorted(seats)

    for num in range(sorted_seats[0], sorted_seats[-1]):
        if num not in sorted_seats:
            print(f"The missing seat number is {num}")


def find_seat_number(row, column):
    seat_number = (int(row) * 8) + int(column)
    return seat_number


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Not very binary Binary Partioning for Advent of Code 2020 Day 5.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        run(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
