# part one
def total_count_from_file(file_name: str) -> int:
    file_map = []
    with open(file_name) as f:
        for line in f:
            if len(file_map) == 0:
                file_map.append(list('.' * (len(line) + 1)))
            file_map.append(list(f'.{line[0:-1]}.'))
    file_map.append(file_map[0])
    total = 0
    for i, line in enumerate(file_map):
        for j, char in enumerate(line):
            if char == '@':
                total += process_cell(file_map, i, j)
    return total


# part two
def total_count_from_file_part_two(file_name: str) -> int:
    file_map = []
    with open(file_name) as f:
        for line in f:
            if len(file_map) == 0:
                file_map.append(list('.' * (len(line) + 1)))
            file_map.append(list(f'.{line[0:-1]}.'))
    file_map.append(file_map[0])
    total = 0
    rolls_to_be_removed = []
    while True:
        for i, line in enumerate(file_map):
            for j, char in enumerate(line):
                if char == '@':
                    if process_cell(file_map, i, j) == 1:
                        total += 1
                        rolls_to_be_removed.append((i, j))
        if len(rolls_to_be_removed) > 0:
            for roll in rolls_to_be_removed:
                file_map[roll[0]][roll[1]] = '.'
            rolls_to_be_removed = []
        else:
            break
    return total


def process_cell(file_map: list[list[str]], i: int, j: int) -> int:
    counter = 0
    # above
    if file_map[i - 1][j - 1] == '@':
        counter += 1
    if file_map[i - 1][j] == '@':
        counter += 1
    if file_map[i - 1][j + 1] == '@':
        counter += 1
    # same row
    if file_map[i][j - 1] == '@':
        counter += 1
    if file_map[i][j + 1] == '@':
        counter += 1
    # below
    if file_map[i + 1][j - 1] == '@':
        counter += 1
    if file_map[i + 1][j] == '@':
        counter += 1
    if file_map[i + 1][j + 1] == '@':
        counter += 1

    if counter >= 4:
        return 0
    else:
        return 1


if __name__ == "__main__":
    total = total_count_from_file('day04\\input_example.txt')
    print(f'Total: {total}')

    total = total_count_from_file('day04\\input.txt')
    print(f'Total: {total}')

    total = total_count_from_file_part_two('day04\\input_example.txt')
    print(f'Total: {total}')

    total = total_count_from_file_part_two('day04\\input.txt')
    print(f'Total: {total}')
