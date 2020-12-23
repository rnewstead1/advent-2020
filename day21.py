DATA_FILE = './data/day21.txt'


def get_allergens(line):
    return line[line.index('contains') + 8:line.index(')')].replace(' ', '').split(',')


def get_foods(line):
    return set((line[:line.index(' (')].split(' ')))


def get_allergen_map(lines):
    allergen_map = {}
    for line in lines:
        allergens = get_allergens(line)
        foods = get_foods(line)
        for allergen in allergens:
            if allergen in allergen_map.keys():
                current_foods = allergen_map[allergen]
                allergen_map[allergen] = current_foods.intersection(foods)
            else:
                allergen_map[allergen] = foods
    return allergen_map


def get_foods_with_allergies(allergen_map):
    return set.union(*allergen_map.values())


def get_all_foods(lines):
    all_foods = {}
    for line in lines:
        foods = get_foods(line)
        for food in foods:
            if food in all_foods.keys():
                appearances = all_foods[food] + 1
                all_foods[food] = appearances
            else:
                all_foods[food] = 1
    return all_foods


def get_appearances(foods, appearance_map):
    total = 0
    for food in foods:
        total += appearance_map[food]
    return total


with open(DATA_FILE) as file:
    lines = file.readlines()

    all_foods = get_all_foods(lines)
    allergen_map = get_allergen_map(lines)

    foods_with_allergies = get_foods_with_allergies(allergen_map)
    foods_without_allergies = all_foods.keys() - foods_with_allergies

    appearances = get_appearances(foods_without_allergies, all_foods)
    print(f'Number of appearances of food without allergies: {appearances}')
