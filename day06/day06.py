import math


# part one
def total_count_from_file(file_name: str) -> int:
    total = 0
    nested_list: list[list[str]] = []
    with open(file_name) as f:
        for i, line in enumerate(f):
            for j, num in enumerate(line.split()):
                if i == 0:
                    nested_list.append([num])
                else:
                    nested_list[j].append(num)
    for column in nested_list:
        operator = column[-1]
        nums = [int(x) for x in column[:-1]]
        if operator == "*":
            total += math.prod(nums)
        else:
            total += sum(nums)
    return total


# part two
def total_count_from_file_part_two(file_name: str) -> int:
    total = 0
    file_list = []
    longest_line_length = 0
    with open(file_name) as f:
        for line in f:
            file_list.append(line[:-1])
            if len(line[:-1]) > longest_line_length:
                longest_line_length = len(line[:-1])
    padded_line_list = []
    for line in file_list:
        padded_line_list.append(list(line.ljust(longest_line_length, " ")))
    # rotate the list as a matrix, 270 degrees, then convert to a whitespace stripped string
    rotated_list = [("".join(i)).strip()
                    for i in list(zip(*padded_line_list))[::-1]]
    current_list = []
    for line in rotated_list:
        # Just a number row
        if line.isdigit():
            current_list.append(int(line))
        # Last element of current_list
        elif "*" in line or "+" in line:
            operator = line[-1]
            current_list.append(int(line[:-1]))
            if operator == "*":
                total += math.prod(current_list)
            else:
                total += sum(current_list)
            current_list = []
    return total


if __name__ == "__main__":
    total = total_count_from_file("day06\\input_example.txt")
    print(f"Total: {total}")

    total = total_count_from_file("day06\\input.txt")
    print(f"Total: {total}")

    total = total_count_from_file_part_two("day06\\input_example.txt")
    print(f"Total: {total}")

    total = total_count_from_file_part_two("day06\\input.txt")
    print(f"Total: {total}")
