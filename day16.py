import re

DATA_FILE = './data/day16.txt'
rule_pattern = re.compile('(?P<name>.+): (?P<lower_1>[0-9]+)-(?P<upper_1>[0-9]+) or (?P<lower_2>[0-9]+)-(?P<upper_2>[0-9]+)')


def get_rule(line):
    rule_match = rule_pattern.match(line)
    name = rule_match.group('name')
    range_1 = int(rule_match.group('lower_1')), int((rule_match.group('upper_1')))
    range_2 = int(rule_match.group('lower_2')), int((rule_match.group('upper_2')))
    return name, range_1, range_2


def get_ticket(line):
    return [int(num) for num in line.split(',')]


def rule_applies(rule, val):
    for val_range in rule[1:]:
        if val_range[0] <= val <= val_range[1]:
            return True
    return False


def get_invalid_values(ticket):
    for num in ticket:
        valid = False
        for rule in rules:
            if rule_applies(rule, num):
                valid = True
                break
        if not valid:
            return num
    return 0

def is_valid(ticket):
    for num in ticket:
        valid = False
        for rule in rules:
            if rule_applies(rule, num):
                valid = True
                break
        if not valid:
            return False
    return True


def get_possible_rules(rules, num):
    possible = set()
    for rule in rules:
        if rule_applies(rule, num):
            possible.add(rule[0])
    if len(possible) == 0:
        print(f'no rules apply for: {num}')
    return possible


def get_index_rule_map(tickets, rules):
    index_rule_map = {}
    for valid_ticket in tickets:
        for index, num in enumerate(valid_ticket):
            possible_rules = get_possible_rules(rules, num)
            add_possible_rules_to_map(index_rule_map, index, possible_rules)
            discard_spares_if_only_one_rule_for_index(index_rule_map)
            for rule in rules:
                discard_spares_if_rule_only_found_once(rule, index_rule_map)
    return index_rule_map


def discard_spares_if_rule_only_found_once(rule, rule_map):
    rule_found = []
    for key in rule_map.keys():
        if rule in rule_map[key]:
            rule_found.append(key)
    if len(rule_found) == 1:
        rule_map[rule_found[0]] = rule


def discard_spares_if_only_one_rule_for_index(rule_map):
    for key in rule_map.keys():
        rules = rule_map[key]
        if len(rules) == 1:
            rule = rules.pop()
            rules.add(rule)
            for other_key in rule_map.keys():
                if other_key != key:
                    rule_map[other_key].discard(rule)


def add_possible_rules_to_map(rule_map, index, possible_rules):
    if index in rule_map.keys():
        existing_rules = rule_map[index]
        rule_map[index] = existing_rules.intersection(possible_rules)
    else:
        rule_map[index] = possible_rules


def get_product(ticket):
    product = 1
    for index, num in enumerate(ticket):
        rule = index_rule_map[index].pop()
        if rule.startswith('departure'):
            product *= num
    return product


with open(DATA_FILE) as file:
    lines = file.readlines()

    end_of_rule_block = lines.index('your ticket:\n') - 1
    rules = [get_rule(line) for line in lines[:end_of_rule_block]]

    start_of_nearby_tickets_block = lines.index('nearby tickets:\n') + 1
    nearby_tickets = [get_ticket(line) for line in lines[start_of_nearby_tickets_block:]]

    invalid_values = [get_invalid_values(ticket) for ticket in nearby_tickets]
    print(f'ticket scanning error rate: {sum(invalid_values)}')

    valid_tickets = [ticket for ticket in nearby_tickets if is_valid(ticket)]
    index_rule_map = get_index_rule_map(valid_tickets, rules)

    your_ticket = get_ticket(lines[end_of_rule_block + 2:][0])
    print(f'Product: {get_product(your_ticket)}')
