from shapely import Polygon, box


# part one
def total_count_from_file(file_name: str) -> int:
    file_list: list[tuple] = []
    with open(file_name) as f:
        for line in f:
            file_list.append(tuple([int(i) for i in line[:-1].split(",")]))
    # Build map of areas and sort
    area_map = []
    for p1 in file_list:
        for p2 in file_list:
            x1, y1 = p1
            x2, y2 = p2
            area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
            area_map.append((area, p1, p2))
    area_map.sort()
    return area_map[-1][0]


# part two
def total_count_from_file_part_two(file_name: str) -> int:
    file_list: list[tuple] = []
    with open(file_name) as f:
        for line in f:
            file_list.append(tuple([int(i) for i in line[:-1].split(",")]))
    shape = Polygon(file_list)
    output = 0
    for p1 in file_list:
        for p2 in file_list:
            x1, y1 = p1
            x2, y2 = p2
            min_x = min(x1, x2)
            max_x = max(x1, x2)
            min_y = min(y1, y2)
            max_y = max(y1, y2)
            rect = box(min_x, min_y, max_x, max_y)
            if rect.within(shape):
                area = (abs(x2 - x1) + 1) * (abs(y2 - y1) + 1)
                if area > output:
                    output = area
    return output


if __name__ == "__main__":
    total = total_count_from_file("day09\\input_example.txt")
    print(f"Total: {total}")

    total = total_count_from_file("day09\\input.txt")
    print(f"Total: {total}")

    total = total_count_from_file_part_two("day09\\input_example.txt")
    print(f"Total: {total}")

    total = total_count_from_file_part_two("day09\\input.txt")
    print(f"Total: {total}")
