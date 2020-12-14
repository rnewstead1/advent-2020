import re

DATA_FILE = './data/day14.txt'
mask_pattern = re.compile('mask = (?P<mask>[X|0|1]+)')
instruction_pattern = re.compile('mem\\[(?P<index>[0-9]+)\\] = (?P<value>[0-9]+)')


def get_instruction_groups(lines):
    groups = []
    group = {}
    for line in lines:
        mask_match = mask_pattern.match(line)
        if mask_match:
            if group:
                groups.append(group)
            group = {'mask': mask_match.group('mask'), 'instructions': []}
        else:
            instruction_match = instruction_pattern.match(line)
            index = int(instruction_match.group('index'))
            value = int(instruction_match.group('value'))
            group['instructions'].append((index, value))
    groups.append(group)
    return groups


def get_memory(groups):
    memory = {}
    for group in groups:
        zeros_mask = int(group['mask'].replace('X', '1'), 2)
        ones_mask = int(group['mask'].replace('X', '0'), 2)
        for instruction in group['instructions']:
            value_after_ones_mask = ones_mask | instruction[1]
            value_after_zeros_mask = zeros_mask & value_after_ones_mask
            memory[instruction[0]] = value_after_zeros_mask
    return memory


with open(DATA_FILE) as file:
    lines = file.readlines()
    instruction_groups = get_instruction_groups(lines)

    print(f'sum of memory values: {sum(get_memory(instruction_groups).values())}')
