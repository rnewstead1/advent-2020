input = '418976235'


def get_destination_index(current, remaining):
    highest = max(remaining)
    lowest = min(remaining)
    destination_value = current - 1 if current - 1 >= lowest else highest
    destination_index = None
    while destination_index is None:
        for i, cup in enumerate(remaining):
            if cup == destination_value:
                destination_index = i
                break
        destination_value = destination_value - 1 if destination_value - 1 >= lowest else highest
    return destination_index


def remove_three_cups(cups, i):
    return [(get_cup(cups, i)), (get_cup(cups, i)), (get_cup(cups, i))]


def get_cup(cups, i):
    cup_index = get_next_cup_index(cups, i)
    cup = cups.pop(cup_index)
    return cup


def get_next_cup_index(cups, i):
    return i + 1 if i + 1 < len(cups) else 0


def move(cups, times):
    i = 0
    for _ in range(times):
        current = cups[i]
        three_cups = remove_three_cups(cups, i)
        destination_index = get_destination_index(current, cups)
        cups[destination_index + 1:destination_index + 1] = three_cups
        i = (cups.index(current) + 1) % len(cups)


cups = [int(char) for char in input]
move(cups, 100)

index_of_one = cups.index(1)
ordered = ''.join([str(i) for i in [*cups[index_of_one + 1:], *cups[:index_of_one]]])
print(f'ordered: {ordered}')
