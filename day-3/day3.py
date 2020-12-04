
def run(file):
    rows = []
    with open(file) as file:
        for line in file:
            rows.append(line.split())

    print(mark_rows(rows.copy()))


def mark_rows(rows):
    index_pos = 3
    tree_count = 0
    first_row = True
    for row in rows:
        if first_row:
            first_row = False
            continue
        if (row[0][index_pos] == '#'):
            row[0] = row[0][:index_pos] + 'X' + row[0][index_pos + 1:]
            tree_count += 1
        index_pos += 3
        index_pos %= len(row[0])

    return tree_count


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        run(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
