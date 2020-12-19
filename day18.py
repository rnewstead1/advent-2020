import re

DATA_FILE = './data/day18.txt'
number_pattern = re.compile('^(?P<number>[0-9]+)')
operator_pattern = re.compile('^(?P<operator>\\+|\\*)')


def apply_operator(operator, first, second):
    if operator == '+':
        return first + second
    elif operator == '*':
        return first * second


def get_string_in_brackets(input_string):
    bracket_count = 1
    string_in_brackets = ''
    for char in input_string[1:]:
        if bracket_count == 0:
            return string_in_brackets[:-1]
        if char == ')':
            bracket_count -= 1
        elif char == '(':
            bracket_count += 1
        string_in_brackets += char
    return string_in_brackets[:-1]


def parse(input_string):
    remaining = input_string
    total = 0
    previous_operator = None
    while len(remaining) != 0:
        number_match = number_pattern.match(remaining)
        operator_match = operator_pattern.match(remaining)
        if number_match:
            current_number = number_match.group('number')
            if previous_operator:
                total = apply_operator(previous_operator, total, int(current_number))
            else:
                total = int(current_number)
            remaining = remaining[len(current_number):]
        elif operator_match:
            previous_operator = operator_match.group('operator')
            remaining = remaining[1:]
        elif remaining[0] == '(':
            string_in_brackets = get_string_in_brackets(remaining)
            next_number = parse(string_in_brackets)
            if previous_operator:
                total = apply_operator(previous_operator, total, next_number)
            else:
                total = next_number
            remaining = remaining[len(string_in_brackets) + 2:]
    return total


with open(DATA_FILE) as file:
    lines = file.readlines()

    sums = [parse(line.replace(' ', '').rstrip()) for line in lines]
    print(f'sum: {sum(sums)}')
