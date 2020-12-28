input = '418976235'
# input = '389125467'


def get_destination_index(current, remaining):
    highest = max(remaining)
    lowest = min(remaining)
    destination_value = current - 1 if current - 1 >= lowest else highest
    while True:
        for i, cup in enumerate(remaining):
            if cup == destination_value:
                return i
        destination_value = destination_value - 1 if destination_value - 1 >= lowest else highest


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


def move_linked(all_the_cups, times):
    cup_next_to = get_links(all_the_cups)

    highest = max(all_the_cups)
    lowest = min(all_the_cups)
    current = all_the_cups[0]

    for _ in range(times):
        cup1 = cup_next_to[current]
        cup2 = cup_next_to[cup1]
        cup3 = cup_next_to[cup2]
        next_cup = cup_next_to[cup3]
        three_cups = [cup1, cup2, cup3]

        destination = current - 1
        while True:
            if destination not in three_cups and destination >= lowest:
                break
            elif destination in three_cups:
                destination -= 1
            elif destination < lowest:
                destination = highest

        cup_next_to_destination = cup_next_to[destination]

        cup_next_to[destination] = cup1
        cup_next_to[cup3] = cup_next_to_destination
        cup_next_to[current] = next_cup
        current = next_cup
    return cup_next_to


def get_links(all_the_cups):
    linked_cups = {}
    for i, number in enumerate(all_the_cups):
        linked_cups[number] = all_the_cups[(i + 1) % len(all_the_cups)]
    return linked_cups


def next_cup(cups, i):
    return cups[(i + 1) % len(cups)]


def get_final_order(linked_cups):
    next_cup = 1
    final_order = []
    for _ in linked_cups:
        final_order.append(next_cup)
        next_cup = linked_cups[next_cup]
    return final_order


def get_cups_after(cups, i):
    index = cups.index(i)
    return ''.join([str(i) for i in [*cups[index + 1:], *cups[:index]]])


cups = [int(char) for char in input]
move(cups, 100)

print(f'ordered: {get_cups_after(cups, 1)}')

original_cups = [int(char) for char in input]
original_links = move_linked(original_cups, 100)

final_order = get_final_order(original_links)
print(f'ordered (linked): {get_cups_after(final_order, 1)}')


many_cups = [*original_cups, *range(max(original_cups) + 1, 1000001)]
many_links = move_linked(many_cups, 10000000)

# 563362809504
next_number = many_links[1]
print(f'product: {next_number * many_links[next_number]}')
