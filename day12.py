DATA_FILE = './data/example12.txt'
all_directions = ['N', 'E', 'S', 'W']


def north(current, value):
    return current[0], current[1] + value, current[2]


def south(current, value):
    return current[0], current[1] - value, current[2]


def east(current, value):
    return current[0] + value, current[1], current[2]


def west(current, value):
    return current[0] - value, current[1], current[2]


def right(current, value):
    current_direction_index = all_directions.index(current[2])
    new_direction_index = int((current_direction_index + value / 90) % len(all_directions))
    new_direction = all_directions[new_direction_index]

    return current[0], current[1], new_direction


def left(current, value):
    return right(current, 360 - value)


def move_forward(current, value):
    return move[current[2]](current, value)


move = {
    'F': move_forward,
    'N': north,
    'S': south,
    'E': east,
    'W': west,
    'R': right,
    'L': left
}


def move_all(instructions):
    current = 0, 0, 'E'
    for instruction in instructions:
        action = instruction[0]
        value = int(instruction[1:])
        current = move[action](current, value)
    return current


def manhattan_distance(end_position):
    return abs(end_position[0]) + abs(end_position[1])


with open(DATA_FILE) as file:
    lines = file.readlines()
    final_position = move_all(lines)

    print(f'final_position: {final_position}')
    print(f'manhattan distance: {manhattan_distance(final_position)}')