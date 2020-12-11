from functools import reduce

DATA_FILE = './data/day11.txt'
directions = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]


def get_layout(line):
    return [char for char in line.rstrip()]


def val_at(index, in_list):
    if 0 <= index < len(in_list):
        return in_list[index]
    return None


def current_row(row, column):
    left = (val_at(column - 1, row))
    right = (val_at(column + 1, row))
    return [left, right]


def adjacent_row(row, column):
    return [(val_at(column - 1, row)), row[column], (val_at(column + 1, row))]


def is_occupied(seat):
    return seat == '#'


def total_occupied(total, current):
    return total + 1 if is_occupied(current) else total


def count_adjacent_occupied_seats(row, column_index, row_above, row_below):
    current = current_row(row, column_index)
    above = adjacent_row(row_above, column_index) if row_above else []
    below = adjacent_row(row_below, column_index) if row_below else []
    adjacent = current + above + below

    return reduce(total_occupied, adjacent, 0)


def get_new_seat(number_of_adjacent_occupied_seats, position):
    if position == '#':
        return '#' if number_of_adjacent_occupied_seats < 4 else 'L'
    else:
        return '#' if number_of_adjacent_occupied_seats == 0 else 'L'


def occupied_seat_rules(layout, seat, row_index, column_index):
    if seat == '.':
        return seat
    else:
        row_above = layout[row_index - 1] if row_index > 0 else []
        row_below = layout[row_index + 1] if row_index < len(layout) - 1 else []
        adjacent_occupied_seats = count_adjacent_occupied_seats(layout[row_index], column_index, row_above, row_below)
        return get_new_seat(adjacent_occupied_seats, seat)


def is_seat(seat):
    return seat in ('#', 'L')


def index_in(row_index, column_index, layout):
    return 0 <= row_index < len(layout) and 0 <= column_index < len(layout[0])


def apply_rules(layout, rules):
    new_layout = []
    for row_index in range(len(layout)):
        new_row = []
        for column_index in range(len(layout[row_index])):
            new_row.append(rules(layout, layout[row_index][column_index], row_index, column_index))
        new_layout.append(new_row)
    return new_layout


def get_new_visible_seat(layout, seat, row_index, column_index):
    visible_occupied_seats = 0
    if seat == '.':
        return seat
    else:
        for direction in directions:
            visible_occupied_seats += get_visible_occupied_seats(column_index, direction, layout, row_index)
        if seat == '#':
            return '#' if visible_occupied_seats < 5 else 'L'
        elif seat == 'L':
            return '#' if visible_occupied_seats == 0 else 'L'


def get_visible_occupied_seats(column_index, direction, layout, row_index):
    new_seat = 'no one sits on the floor'
    new_column_index = column_index
    new_row_index = row_index
    while not is_seat(new_seat):
        new_column_index += direction[0]
        new_row_index += direction[1]
        if index_in(new_row_index, new_column_index, layout):
            new_seat = layout[new_row_index][new_column_index]
            if is_occupied(new_seat):
                return 1
        else:
            return 0
    return 0


def count_occupied_seats_in_row(row):
    return reduce(total_occupied, row, 0)


def count_occupied_seats(layout):
    return reduce(lambda acc, curr: acc + count_occupied_seats_in_row(curr), layout, 0)


def print_layout(layout):
    print('-------')
    for line in layout:
        print(line)
    print('-------')


def find_equilibrium(first_layout, rules):
    previous_layout = []
    next_layout = first_layout
    while previous_layout != next_layout:
        previous_layout = next_layout
        next_layout = apply_rules(next_layout, rules)
    return next_layout


with open(DATA_FILE) as file:
    lines = file.readlines()
    layout = [get_layout(line) for line in lines]

    occupied_seat_rule_count = count_occupied_seats(find_equilibrium(layout, occupied_seat_rules))
    print(f'occupied seats by occupied seat rules: {occupied_seat_rule_count}')

    visible_seat_rule_count = count_occupied_seats(find_equilibrium(layout, get_new_visible_seat))
    print(f'occupied seats by visible seat rules: {visible_seat_rule_count}')
