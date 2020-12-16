import re

DATA_FILE = './data/day16.txt'
rule_pattern = re.compile('.+: (?P<lower_1>[0-9]+)-(?P<upper_1>[0-9]+) or (?P<lower_2>[0-9]+)-(?P<upper_2>[0-9]+)')


def get_rule(line):
    rule_match = rule_pattern.match(line)
    if not rule_match:
        print(f'lin: {line}')
    range_1 = int(rule_match.group('lower_1')), int((rule_match.group('upper_1')))
    range_2 = int(rule_match.group('lower_2')), int((rule_match.group('upper_2')))
    return range_1, range_2


def get_ticket(line):
    return [int(num) for num in line.split(',')]


def apply_rule(rule, val):
    for val_range in rule:
        if val_range[0] <= val <= val_range[1]:
            return True
    return False


def get_invalid(ticket):
    for num in ticket:
        num_valid = False
        for rule in rules:
            if apply_rule(rule, num):
                num_valid = True
                break
        if not num_valid:
            return num
    return 0


with open(DATA_FILE) as file:
    lines = file.readlines()

    end_of_rule_block = lines.index('your ticket:\n') - 1
    rules = [get_rule(line) for line in lines[:end_of_rule_block]]

    start_of_nearby_tickets_block = lines.index('nearby tickets:\n') + 1
    nearby_tickets = [get_ticket(line) for line in lines[start_of_nearby_tickets_block:]]

    invalid_tickets = [get_invalid(ticket) for ticket in nearby_tickets]

    print(f'ticket scanning error rate: {sum(invalid_tickets)}')
