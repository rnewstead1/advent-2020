from collections import Counter

DATA_FILE = './data/day10.txt'


with open(DATA_FILE) as file:
    lines = file.readlines()

    sorted_adapters = [0, *sorted(lines, key=lambda line: int(line))]
    differences = []
    for index, adapter in enumerate(sorted_adapters):
        difference = int(sorted_adapters[index + 1]) - int(adapter) if index + 1 < len(sorted_adapters) else 3
        differences.append(difference)

    counts = Counter(differences)
    print(f'differences: {counts[3] * counts[1]}')
