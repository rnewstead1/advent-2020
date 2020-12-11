from collections import Counter

DATA_FILE = './data/day10.txt'


alternatives_for_number_of_diffs = {
    2: 2,
    3: 4,
    4: 7
}


def arrangements(diffs):
    alternatives = 1
    counter = 0
    for diff in diffs:
        if diff == 1:
            counter += 1
        if diff == 3:
            alternatives *= alternatives_for_number_of_diffs.get(counter, 1)
            counter = 0
    return alternatives


with open(DATA_FILE) as file:
    lines = file.readlines()

    sorted_adapters = [0, *sorted(lines, key=lambda line: int(line))]
    differences = []
    for index, adapter in enumerate(sorted_adapters):
        difference = int(sorted_adapters[index + 1]) - int(adapter) if index + 1 < len(sorted_adapters) else 3
        differences.append(difference)

    counts = Counter(differences)
    print(f'differences: {counts[3] * counts[1]}')

    distinct_arrangements = arrangements(differences)
    print(f'distinct arrangements: {distinct_arrangements}')
