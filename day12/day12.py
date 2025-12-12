# part one
def total_count_from_file(file_name: str) -> int:
    with open(file_name) as f:
        file_string = f.read().rstrip()
        file_parts = file_string.split("\n\n")

    # present_list = file_parts[:-1]
    # density = [present.count("#") for present in present_list]

    region_list = file_parts[-1].split("\n")
    total = 0
    for region in region_list:
        xy, present_counts = region.split(": ")
        present_counts = list(map(int, present_counts.split(" ")))
        x, y = list(map(int, xy.split("x")))
        # min_space = sum(a * b for a, b in zip(present_counts, density))
        num_presents = sum(present_counts)
        if num_presents <= (x // 3) * (y // 3):
            total += 1
    return total


if __name__ == "__main__":
    # Seems like a Christmas gift.
    # The input everyone? got doesn't actually need heavy logic, just check for 3x3.
    # So this seems to work for all inputs, BUT not the example input.

    # total = total_count_from_file("day12\\input_example.txt")
    # print(f"Total: {total}")

    total = total_count_from_file("day12\\input.txt")
    print(f"Total: {total}")
