passwords = []


def start(file):
    data = getData(file)
    count = 0
    for item in data:
        policy = item[0]
        letter = item[1][:-1]
        password = item[2]

        if (password_is_valid_revised(policy, letter, password)):
            count += 1

    print(count)


def password_is_valid(policy, letter, password):
    occurences = password.count(letter)
    policy = policy.split("-")
    policy_range = range(int(policy[0]), int(policy[1]) + 1)
    if occurences in policy_range:
        return True


def password_is_valid_revised(policy, letter, password):
    policy = policy.split("-")
    index_pos_1 = int(policy[0]) - 1
    index_pos_2 = int(policy[1]) - 1
    if (
        password[index_pos_1] == letter and password[index_pos_2] != letter
        or
        password[index_pos_2] == letter and password[index_pos_1] != letter
    ):
        return True


def getData(file):
    with open(file) as file:
        for line in file:
            passwords.append(line.split())
    return passwords


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        start(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
