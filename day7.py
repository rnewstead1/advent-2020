import re

DATA_FILE = './data/day7.txt'


def get_contents(inner):
    pieces = re.findall("([0-9]+) (.+) bag", inner.rstrip())
    if len(pieces) == 0:
        return {}
    return {'num': pieces[0][0], 'color': pieces[0][1]}


def get_rules(line):
    split_line = re.split('contain', line)
    color = re.findall('(.+) bag', split_line[0])[0]
    contents = [get_contents(inner) for inner in (split_line[1].split(','))]
    return {'color': color, 'contents': contents}


def contains_color(contents, color):
    for bag in contents:
        if bag and bag['color'] == color:
            return True
    return False


with open(DATA_FILE) as file:
    rules = [get_rules(line) for line in file.readlines()]

    def bag_colors(color):
        bags = set()
        for rule in rules:
            if contains_color(rule['contents'], color):
                found = rule['color']
                bags.add(found)
                bags |= bag_colors(found)
        return bags

    print(f'Number of available rules: {len(bag_colors("shiny gold"))}')

    def total_bags(color):
        total = 0
        for rule in rules:
            if rule['color'] == color:
                for bag in rule['contents']:
                    if bag:
                        num_of_bags = int(bag['num'])
                        total += num_of_bags
                        total += num_of_bags * total_bags(bag['color'])
        return total

    print(f'Total bags: {total_bags("shiny gold")}')
