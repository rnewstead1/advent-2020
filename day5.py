DATA_FILE = './data/day5.txt'
seat_ids = []

def bitwise_shift(code, one_symbol):
    number = 0
    for char in code:
        val = 1 if char == one_symbol else 0
        number <<= 1
        number |= val
    return number

def add_seat_id(seat_code):
    row = bitwise_shift(seat_code[0:7], 'B')
    column = bitwise_shift(seat_code[7:10], 'R')
    seat_id = row * 8 + column
    seat_ids.append(seat_id)

with open(DATA_FILE) as file:
    for line in file:
        add_seat_id(line.rstrip())

print(f'Highest seat id: {max(seat_ids)}.')

