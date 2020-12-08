import copy

DATA_FILE = './data/day8.txt'


def run_instructions(instructions):
    visited_instructions = set()
    acc = 0
    index = 0
    terminates_normally = False

    while index not in visited_instructions:
        if index == len(instructions):
            terminates_normally = True
            return acc, terminates_normally
        operator, arg = instructions[index].rstrip().split(' ')
        visited_instructions.add(index)
        if operator == 'acc':
            acc += int(arg)
        index += int(arg) if operator == 'jmp' else 1
    return acc, terminates_normally


def can_swap(operator):
    return operator != 'acc'


def swap(operator):
    return 'jmp' if operator == 'nop' else 'nop'


def terminates(instructions):
    for idx, line in enumerate(instructions):
        operator, arg = instructions[idx].rstrip().split(' ')
        if can_swap(operator):
            changed_lines = copy.deepcopy(instructions)
            changed_lines[idx] = f'{swap(operator)} {arg}'
            acc, terminates_normally = run_instructions(changed_lines)
            if terminates_normally:
                return acc


with open(DATA_FILE) as file:
    lines = file.readlines()

    acc_value_before_infinite_loop = run_instructions(lines)[0]
    print(f'acc value before infinite loop: {acc_value_before_infinite_loop}')
    print(f'acc value when program terminates normally: {terminates(lines)}')
