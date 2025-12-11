from functools import cache


class TreeNode:
    def __init__(self, name: str):
        self.name = name
        self.children: list[TreeNode] = []

    def add_child(self, node: "TreeNode"):
        self.children.append(node)

    def print_tree(self, level: int = 0):
        print("  " * level + str(self.name))
        for child in self.children:
            child.print_tree(level + 1)

    def build_tree_from_dict(self, device_dict: dict[str, list[str]]):
        children = device_dict[self.name]
        for child in children:
            child_node = TreeNode(child)
            child_node.build_tree_from_dict(device_dict)
            self.add_child(child_node)

    def count_paths_to_node(self, name: str) -> int:
        if self.name == name:
            return 1
        total_paths = 0
        for child in self.children:
            total_paths += child.count_paths_to_node(name)
        return total_paths

    def list_all_paths(self) -> list[list[str]]:
        if not self.children:
            return [[self.name]]
        paths = []
        for child in self.children:
            for path in child.list_all_paths():
                paths.append([self.name] + path)
        return paths


def initialize_dict(file_name: str) -> dict[str, list[str]]:
    device_dict: dict[str, list[str]] = {"out": []}
    with open(file_name) as f:
        for line in f:
            key, value = line.split(":")
            device_dict[key] = value.split()
    return device_dict


# part one
def total_count_from_file(file_name: str) -> int:
    device_dict = initialize_dict(file_name)
    node = TreeNode("you")
    node.build_tree_from_dict(device_dict)
    return node.count_paths_to_node("out")


# part two
def total_count_from_file_part_two(file_name: str) -> int:
    device_dict = initialize_dict(file_name)

    @cache
    def dfs(name: str, dac: bool, fft: bool) -> int:
        if name == "out":
            return fft and dac
        total = 0
        for child in device_dict[name]:
            if child == "dac":
                total += dfs(child, True, fft)
            elif child == "fft":
                total += dfs(child, dac, True)
            else:
                total += dfs(child, dac, fft)
        return total

    return dfs("svr", False, False)
    # node = TreeNode("svr")
    # node.build_tree_from_dict(device_dict)
    # return sum([1 for i in node.list_all_paths() if i[-1]
    #             == "out" and "dac" in i and "fft" in i])


if __name__ == "__main__":
    total = total_count_from_file("day11\\input_example.txt")
    print(f"Total: {total}")

    total = total_count_from_file("day11\\input.txt")
    print(f"Total: {total}")

    total = total_count_from_file_part_two("day11\\input_example_part_two.txt")
    print(f"Total: {total}")

    total = total_count_from_file_part_two("day11\\input.txt")
    print(f"Total: {total}")
