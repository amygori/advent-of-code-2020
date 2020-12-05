from functools import reduce


def run(file):
    rows = []
    with open(file) as file:
        for line in file:
            rows.append(line.split())

    count_trees(rows)


def count_trees(rows):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    tree_counts = []
    for slope in slopes:
        tree_counts.append(mark_rows(rows.copy(), slope))

    print(tree_counts)
    print(reduce((lambda x, y: x*y), tree_counts))


def mark_rows(rows, slope):
    index_pos = slope[0]
    tree_count = 0
    first_row = True
    for row in rows:
        if first_row:
            first_row = False
            continue
        if slope[1] == 2 and rows.index(row) % 2 != 0:
            continue
        if (row[0][index_pos] == '#'):
            tree_count += 1
        index_pos += slope[0]
        index_pos %= len(row[0])
    return tree_count


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
    parser.add_argument('file', help='file to read')
    args=parser.parse_args()

    file=Path(args.file)
    if file.is_file():
        run(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
