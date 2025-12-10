import itertools
import z3


class Machine:
    def __init__(self, line: str) -> None:
        light_index = line.index("]")
        joltage_index = line.index("{")
        self.light_diagram = line[1:light_index]
        self.button_wiring = [set(map(int, (i[1:-1].split(","))))
                              for i in line[light_index + 2:joltage_index - 1].split()]
        self.joltage_requirment = [
            int(i) for i in line[joltage_index + 1:-2].split(",")]

    def __str__(self) -> str:
        return f"'{self.light_diagram}' '{self.button_wiring}' '{self.joltage_requirment}'"

    def calc_min_press(self) -> int:
        num_lights = len(self.light_diagram)
        num_buttons = len(self.button_wiring)
        for num_to_press in range(num_buttons + 1):
            for pressed_combination in itertools.combinations(self.button_wiring, num_to_press):
                current_light_list = []
                for light_index in range(num_lights):
                    flip_count = sum(
                        light_index in button_wiring for button_wiring in pressed_combination)
                    is_on = flip_count % 2
                    current_light_list.append(".#"[is_on])
                current_light = "".join(current_light_list)
                if current_light == self.light_diagram:
                    return num_to_press
        return -1

    def calc_min_press_joltage(self) -> int:
        total = 0
        solver = z3.Optimize()
        button_presses = [
            z3.Int(f"button{i}") for i in range(len(self.button_wiring))
        ]
        for press in button_presses:
            solver.add(press >= 0)
        for i, joltage in enumerate(self.joltage_requirment):
            solver.add(sum(button_presses[j] for j, button in enumerate(
                self.button_wiring) if i in button) == joltage)
        solver.minimize(sum(button_presses))
        assert solver.check() == z3.sat
        model = solver.model()
        for press in button_presses:
            total += model[press].as_long()
        return total


# part one
def total_count_from_file(file_name: str) -> int:
    machine_list: list[Machine] = []
    with open(file_name) as f:
        for line in f:
            machine_list.append(Machine(line))
    total = 0
    for machine in machine_list:
        total += machine.calc_min_press()
    return total


# part two
def total_count_from_file_part_two(file_name: str) -> int:
    machine_list: list[Machine] = []
    with open(file_name) as f:
        for line in f:
            machine_list.append(Machine(line))
    total = 0
    for machine in machine_list:
        total += machine.calc_min_press_joltage()
    return total


if __name__ == "__main__":
    total = total_count_from_file("day10\\input_example.txt")
    print(f"Total: {total}")

    total = total_count_from_file("day10\\input.txt")
    print(f"Total: {total}")

    total = total_count_from_file_part_two("day10\\input_example.txt")
    print(f"Total: {total}")

    total = total_count_from_file_part_two("day10\\input.txt")
    print(f"Total: {total}")
