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


def get_number_at_position(x, initial):
    numbers = initial
    while len(numbers) != x:
        next_number = get_next_number(numbers)
        numbers.append(next_number)
    return numbers[-1]


x = 2020
print(f'{x}th number: {get_number_at_position(x, input_list)}')
