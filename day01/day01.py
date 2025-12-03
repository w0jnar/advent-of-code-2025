# part 1
def total_count_from_file(file_name):
    password_count = 0
    position = 50
    with open(file_name) as f:
        for line in f:
            direction, number_of_rotations = line[0], int(line[1:-1])
            if direction == 'L':
                position = (position - number_of_rotations) % 100
            else:
                position = (position + number_of_rotations) % 100
            if position == 0:
                password_count += 1
    return password_count


# part 2
def total_count_from_file_part_2(file_name):
    password_count = 0
    position = 50
    with open(file_name) as f:
        for line in f:
            direction, number_of_rotations = line[0], int(line[1:-1])
            if direction == 'L':
                was_position_positive = position > 0
                position -= number_of_rotations
                is_position_negative = position < 0
                if position == 0 or (was_position_positive and is_position_negative):
                    password_count += 1
                while position < 0:
                    if position <= -100:
                        password_count += 1
                    position += 100
            else:
                position += number_of_rotations
                while position > 99:
                    position -= 100
                    password_count += 1
            # print(f'{direction} {number_of_rotations} {position} {password_count}')
    return password_count


if __name__ == "__main__":
    total = total_count_from_file('day01\\input_example.txt')
    print(f'Password: {total}')

    total = total_count_from_file('day01\\input.txt')
    print(f'Password: {total}')

    total = total_count_from_file_part_2('day01\\input_example.txt')
    print(f'Password: {total}')

    total = total_count_from_file_part_2('day01\\input.txt')
    print(f'Password: {total}')
