# part one
def total_count_from_file(file_name: str) -> int:
    total = 0
    ranges = []
    ingredients = []
    with open(file_name) as f:
        for line in f:
            if "-" in line:
                split_line = [int(i) for i in line[:-1].split("-")]
                ranges.append(range(split_line[0], split_line[1] + 1))
            elif line != "\n":
                ingredients.append(int(line[:-1]))
    for ingredient in ingredients:
        for r in ranges:
            if ingredient in r:
                total += 1
                break
    return total


# part two
def total_count_from_file_part_two(file_name: str) -> int:
    total = 0
    ranges = []
    with open(file_name) as f:
        for line in f:
            if "-" in line:
                split_line = [int(i) for i in line[:-1].split("-")]
                ranges.append((split_line[0], split_line[1]))
            elif line == "\n":
                break
    ranges.sort()
    right = -1
    for r in ranges:
        left = max((right + 1), r[0])
        right = max(right, r[1])
        total += max(0, (right - left + 1))
    return total


if __name__ == "__main__":
    total = total_count_from_file('day05\\input_example.txt')
    print(f'Total: {total}')

    total = total_count_from_file('day05\\input.txt')
    print(f'Total: {total}')

    total = total_count_from_file_part_two('day05\\input_example.txt')
    print(f'Total: {total}')

    total = total_count_from_file_part_two('day05\\input.txt')
    print(f'Total: {total}')
