import concurrent.futures


# part one/two
def total_count_from_file(file_name: str, is_part_two: bool = False) -> int:
    if is_part_two:
        combinations = 12
    else:
        combinations = 2
    file_list = []
    with open(file_name) as f:
        for line in f:
            file_list.append(line[0:-1])
    futures_list = []
    pool = concurrent.futures.InterpreterPoolExecutor()
    for line in file_list:
        futures_list.append(pool.submit(
            process_line, line, combinations))
    concurrent.futures.wait(futures_list)
    total = 0
    for future in futures_list:
        total += future.result()
    return total


def find_next_max_value(line: str, start_index: int, end_index: int) -> tuple[str, int]:
    max = "0"
    index = -1
    for i in range(start_index, end_index):
        num = line[i]
        if index == -1:
            max = num
            index = i
        elif (num > max):
            max = num
            index = i
        if (max == "9"):
            break
    return max, index


def process_line(line: str, combinations: int) -> int:
    max_list = []
    index = 0
    step = combinations - 1
    for _ in range(0, combinations):
        new_max, index = find_next_max_value(line, index, (len(line) - step))
        step -= 1
        index += 1
        max_list.append(new_max)
    return int("".join(max_list))


if __name__ == "__main__":
    total = total_count_from_file("day03\\input_example.txt")
    print(f"Total: {total}")

    total = total_count_from_file("day03\\input.txt")
    print(f"Total: {total}")

    total = total_count_from_file("day03\\input_example.txt", True)
    print(f"Total: {total}")

    total = total_count_from_file("day03\\input.txt", True)
    print(f"Total: {total}")
