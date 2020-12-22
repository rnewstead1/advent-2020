input_list = [0,3,6]


def last_index_of(value, numbers_list):
    try:
        last_index = len(numbers_list) - 1 - numbers_list[::-1].index(value)
    except ValueError:
        last_index = None
    return last_index


def get_next_number(numbers):
    last_index = last_index_of(numbers[-1], numbers[:-1])
    if last_index is not None:
        return len(numbers) -1 - last_index
    else:
        return 0


def get_number_at_slow(x, initial):
    numbers = initial
    while len(numbers) != x:
        next_number = get_next_number(numbers)
        numbers.append(next_number)
    return numbers[-1]


def get_number_at_position(x, numbers, next_number):
    indexed = {int(i): index for index, i in enumerate(numbers, start=1)}
    next_index = len(input_list) + 1
    all_numbers = numbers
    while next_index != x:
        all_numbers.append(next_number)
        if next_number in indexed.keys():
            last_index = indexed[next_number]
            indexed[next_number] = next_index
            next_number = next_index - last_index
        else:
            indexed[next_number] = next_index
            next_number = 0
        next_index += 1
    return next_number


x = 30000000
print(f'{x}th number: {get_number_at_position(x, [int(i) for i in input_list], 0)}')
