import re


# part one/two
def total_count_from_file(file_name: str, is_part_two: bool = False) -> int:
    total = 0
    if is_part_two:
        regex = r"^(\d+)\1+$"
    else:
        regex = r"^(\d+)\1$"
    with open(file_name) as f:
        for line in f:
            ranges = line.split(",")
            for range_str in ranges:
                start, end = int(range_str.split(
                    "-")[0]), int(range_str.split("-")[1])
                for i in range(start, end + 1):

                    if re.fullmatch(regex, str(i)):
                        total += i
    return total


if __name__ == "__main__":
    total = total_count_from_file("day02\\input_example.txt")
    print(f"Total: {total}")

    total = total_count_from_file("day02\\input.txt")
    print(f"Total: {total}")

    total = total_count_from_file("day02\\input_example.txt", True)
    print(f"Total: {total}")

    total = total_count_from_file("day02\\input.txt", True)
    print(f"Total: {total}")
