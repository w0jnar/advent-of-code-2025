import re


# part one
def total_count_from_file(file_name):
    total = 0
    with open(file_name) as f:
        for line in f:
            ranges = line.split(',')
    for range_str in ranges:
        start, end = int(range_str.split('-')[0]), int(range_str.split('-')[1])
        for i in range(start, end + 1):
            if re.fullmatch(r"^(\d+)\1$", str(i)):
                total += i
    return total


# part two
def total_count_from_file_part_two(file_name):
    total = 0
    with open(file_name) as f:
        for line in f:
            ranges = line.split(',')
    for range_str in ranges:
        start, end = int(range_str.split('-')[0]), int(range_str.split('-')[1])
        for i in range(start, end + 1):
            if re.fullmatch(r"^(\d+)\1+$", str(i)):
                total += i
    return total


if __name__ == "__main__":
    total = total_count_from_file('day02\\input_example.txt')
    print(f'Total: {total}')

    total = total_count_from_file('day02\\input.txt')
    print(f'Total: {total}')

    total = total_count_from_file_part_two('day02\\input_example.txt')
    print(f'Total: {total}')

    total = total_count_from_file_part_two('day02\\input.txt')
    print(f'Total: {total}')
