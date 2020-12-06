
def run(file):
    with open(file) as file:
        seat_codes = file.readlines()
        seat_codes = [seat_code.strip() for seat_code in seat_codes]
        print(seat_codes)
        seats = []
        for seat_code in seat_codes:
            seats.append(decode(seat_code))
        print(f"The highest seat number is {max(seats)}")
        find_my_seat(seats)


def find_my_seat(seats):
    sorted_seats = sorted(seats)

    for num in range(sorted_seats[0], sorted_seats[-1]):
        if num not in sorted_seats:
            print(f"The missing seat number is {num}")


def decode(seat_code):
    row_code = seat_code[:-3]
    column_code = seat_code[-3:]
    row = parse_row(row_code)
    column = parse_column(column_code)
    seat_number = find_seat_number(row, column)
    return seat_number


def parse_row(row_code):
    start = 0
    stop = 127
    for char in row_code:
        diff = (stop + start) // 2
        if char == 'F' or char == 'R':
            stop = diff
            # print(f"F means take lower: keep rows {start} to {stop}")
        if char == 'B' or char == 'L':
            start = diff + 1
            # print(f"B means take upper: keep rows {start} to {stop}")
    # print(f"Parse row: {stop}")
    return stop


def parse_column(column_code):
    start = 0
    stop = 7
    for char in column_code:
        diff = (stop + start) // 2
        if char == 'F' or char == 'L':
            stop = diff
            # print(f"L means take lower: keep rows {start} to {stop}")
        if char == 'B' or char == 'R':
            start = diff + 1
            # print(f"R means take upper: keep rows {start} to {stop}")
    # print(f"Parse column: {stop}")
    return stop


def find_seat_number(row, column):
    seat_number = (int(row) * 8) + int(column)
    print(f"Seat number is {seat_number}")
    return seat_number


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Not very binary Binary Partioning for Advent of Code 2020 Day 4.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        run(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
