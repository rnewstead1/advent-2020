DATA_FILE = './data/day12.txt'
all_directions = ['N', 'E', 'S', 'W']


def north(position, value):
    return position[0], position[1] + value


def south(position, value):
    return position[0], position[1] - value


def east(position, value):
    return position[0] + value, position[1]


def west(position, value):
    return position[0] - value, position[1]


def right(current, value):
    current_direction_index = all_directions.index(current[2])
    new_direction_index = int((current_direction_index + value / 90) % len(all_directions))
    new_direction = all_directions[new_direction_index]

    return current[0], current[1], new_direction


def left(current, value):
    return right(current, 360 - value)


def move_forward(current, value):
    return move_ship[current[2]](current, value)


def move_ship_towards(compass_point):
    return lambda position, value: (*compass_point((position[0], position[1]), value), position[2])


move_ship = {
    'F': move_forward,
    'N': move_ship_towards(north),
    'S': move_ship_towards(south),
    'E': move_ship_towards(east),
    'W': move_ship_towards(west),
    'R': right,
    'L': left
}


def all_ship_moves(instructions):
    current = 0, 0, 'E'
    for instruction in instructions:
        action = instruction[0]
        value = int(instruction[1:])
        current = move_ship[action](current, value)
    return current


def move_beacon_towards(compass_point):
    return lambda ship, beacon, value: (ship, compass_point(beacon, value))


def move_ship_toward_beacon(ship, beacon, value):
    return (north(east(ship, value * beacon[0]), value * beacon[1])), beacon


def rotation_times(value):
    return int((value / 90) % 4)


def right_around_ship(ship, beacon, value):
    return ship, rotate(beacon, beacon_right, rotation_times(value))


def rotate(beacon, direction, times):
    for i in range(times):
        beacon = direction(beacon)
    return beacon


def beacon_right(beacon):
    return beacon[1], beacon[0] * -1


def beacon_left(beacon):
    return beacon[1] * -1, beacon[0]


def left_around_ship(ship, beacon, value):
    return ship, rotate(beacon, beacon_left, rotation_times(value))


move_beacon = {
    'F': move_ship_toward_beacon,
    'N': move_beacon_towards(north),
    'S': move_beacon_towards(south),
    'E': move_beacon_towards(east),
    'W': move_beacon_towards(west),
    'R': right_around_ship,
    'L': left_around_ship
}


def all_beacon_moves(instructions):
    ship = 0, 0
    beacon = 10, 1
    for instruction in instructions:
        action = instruction[0]
        value = int(instruction[1:])
        ship, beacon = move_beacon[action](ship, beacon, value)
    return ship


def manhattan_distance(end_position):
    return abs(end_position[0]) + abs(end_position[1])


with open(DATA_FILE) as file:
    lines = file.readlines()

    ship_final_position = all_ship_moves(lines)
    print(f'manhattan distance for ship only: {manhattan_distance(ship_final_position)}')

    ship_with_beacon_final_position = all_beacon_moves(lines)
    print(f'manhattan distance for ship with beacon: {manhattan_distance(ship_with_beacon_final_position)}')
