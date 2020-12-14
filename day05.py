DATA_FILE = './data/day5.txt'

def bitwise_shift(code, one_symbol):
    number = 0
    for char in code:
        val = 1 if char == one_symbol else 0
        number <<= 1
        number |= val
    return number

def missing_seat_id(ids):
    ids.sort()
    missing_id = 0

    for i, id in enumerate(ids):
        next_seat_id = ids[i + 1]
        if next_seat_id - id != 1:
          missing_id = id + 1
          break

    return missing_id

def all_seat_ids(seat_codes):
    seat_ids = []
    for seat_code in seat_codes:
        row = bitwise_shift(seat_code[0:7], 'B')
        column = bitwise_shift(seat_code[7:10], 'R')
        seat_id = row * 8 + column
        seat_ids.append(seat_id)
    return seat_ids

with open(DATA_FILE) as file:
    seat_ids = all_seat_ids(file)

print(f'Highest seat id: {max(seat_ids)}.')
print(f'My seat id: {missing_seat_id(seat_ids)}')
