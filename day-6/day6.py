def run(file):
    with open(file) as file:
        lines = [line.strip() for line in file.readlines()]
        calculate_all_yes_answers(process_data(lines))


def process_data(lines):
    data = []
    answer_group = []
    answer_set = set()
    for line in lines:
        if line:
            # keep adding to the answer group
            answer_group.append(set(line))
            if line == lines[-1]:
                data.append(answer_group)
        else:
            # then we want to add the temp data var to a data list
            data.append(answer_group)
            # and reset the group variable
            answer_group = []
    return data


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


def calculate_all_yes_answers(data):
    answers_count = 0
    for answer_group in data:
        intersection = set.intersection(*answer_group)
        answers_count += len(set.intersection(*answer_group))
    print(f"YES Answers count: {answers_count}")


def count_answers(data):
    count = []
    print(data)
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
