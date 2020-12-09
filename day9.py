DATA_FILE = './data/day9.txt'


def check_preamble(preamble, number):
    for test in preamble:
        difference_to_next_num = number - test
        if difference_to_next_num in preamble:
            return True
    return False


def find_bad_number(numbers, preamble_length):
    preamble_start_index = 0
    preamble_end_index = 0 + preamble_length
    for i in range(preamble_length, len(numbers)):
        preamble = set(int(number) for number in numbers[preamble_start_index:preamble_end_index])
        next_num = int(numbers[i])
        if not check_preamble(preamble, next_num):
            return next_num
        preamble_start_index += 1
        preamble_end_index += 1


def encryption_weakness(bad_number, numbers, start_index):
    contiguous_range = []
    for i in range(start_index, len(numbers)):
        contiguous_range.append(int(numbers[i]))
        range_sum = sum(contiguous_range)
        if range_sum == bad_number:
            return max(contiguous_range) + min(contiguous_range)
        elif range_sum > bad_number:
            return encryption_weakness(bad_number, numbers, start_index + 1)


with open(DATA_FILE) as file:
    lines = file.readlines()

    bad_number = find_bad_number(lines, 25)
    print(f'bad number: {bad_number}')

    weakness = encryption_weakness(bad_number, lines, 0)
    print(f'weakness: {weakness}')
