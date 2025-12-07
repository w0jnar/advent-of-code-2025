import collections


# part one/two
def total_count_from_file(file_name: str, is_part_two: bool = False) -> int:
    total = 0
    file_list: list[list[str]] = []
    with open(file_name) as f:
        for line in f:
            file_list.append(list(line[:-1]))
    s_position = file_list[0].index("S")
    paths = collections.defaultdict(lambda: 0)
    paths[s_position] = 1
    for i in range(len(file_list) - 1):
        for j, count in list(paths.items()):
            char = file_list[i + 1][j]

            if char == "^":
                total += 1
                paths[j - 1] += count
                paths[j + 1] += count
                del paths[j]
    if not is_part_two:
        return total
    return sum(paths.values())


if __name__ == "__main__":
    total = total_count_from_file("day07\\input_example.txt")
    print(f"Total: {total}")

    total = total_count_from_file("day07\\input.txt")
    print(f"Total: {total}")

    total = total_count_from_file("day07\\input_example.txt", True)
    print(f"Total: {total}")

    total = total_count_from_file("day07\\input.txt", True)
    print(f"Total: {total}")
