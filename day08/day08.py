import collections
import math


class MergeFind:
    def __init__(self, size: int):
        self.mf = {i: i for i in range(size)}

    def find(self, element: int) -> int:
        if element == self.mf[element]:
            return element
        self.mf[element] = self.find(self.mf[element])
        return self.mf[element]

    def merge(self, element_1: int, element_2: int):
        self.mf[self.find(element_1)] = self.find(element_2)


# part one/two
def total_count_from_file(file_name: str, is_part_two: bool = False) -> int:
    file_list: list[tuple] = []
    with open(file_name) as f:
        for line in f:
            file_list.append(tuple([int(i) for i in line[:-1].split(",")]))
    # Build map of distances and sort
    dist_map = []
    for i, p1 in enumerate(file_list):
        for j, p2 in enumerate(file_list):
            distance = math.dist(p1, p2)
            if i > j:
                dist_map.append((distance, i, j))
    dist_map.sort()
    # Number of pairs from problem.
    pairs = 1000
    if "example" in file_name:
        pairs = 10
    # Create a merge-find to create essentially a graph of junction boxes
    mf = MergeFind(len(file_list))
    output = 0
    connections = 0
    for t, (_, i, j) in enumerate(dist_map):
        # Part one
        if not is_part_two and t == pairs:
            sizes = collections.defaultdict(int)
            for x in range(len(file_list)):
                sizes[mf.find(x)] += 1
            sorted_sizes = sorted(sizes.values())
            output = sorted_sizes[-1] * sorted_sizes[-2] * sorted_sizes[-3]
        if mf.find(i) != mf.find(j):
            connections += 1
            # Part two
            if is_part_two and connections == len(file_list) - 1:
                output = file_list[i][0] * file_list[j][0]
            mf.merge(i, j)
    return output


if __name__ == "__main__":
    total = total_count_from_file("day08\\input_example.txt")
    print(f"Total: {total}")

    total = total_count_from_file("day08\\input.txt")
    print(f"Total: {total}")

    total = total_count_from_file("day08\\input_example.txt", True)
    print(f"Total: {total}")

    total = total_count_from_file("day08\\input.txt", True)
    print(f"Total: {total}")
