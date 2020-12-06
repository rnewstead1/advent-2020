from functools import reduce

DATA_FILE = './data/day6.txt'


def get_groups(lines):
    groups = []

    def group(lines, start_index):
        try:
            end_index = lines.index('', start_index)
        except ValueError:
            end_index = len(lines)
        groups.append(lines[start_index:end_index])
        return end_index + 1

    i = 0
    while i < len(lines):
        i = group(lines, i)

    return groups


def any_yes_answers(sum, group):
    yes_answers = set()
    for persons_answers in group:
        for answer in persons_answers:
            yes_answers.add(answer)
    return sum + len(yes_answers)


def all_yes_answers(sum, group):
    def as_set(answers):
        answer_set = set()
        for answer in answers:
            answer_set.add(answer)
        return answer_set

    all_answers = [as_set(persons_answers) for persons_answers in group]
    return sum + len(all_answers[0].intersection(*all_answers[1:]))


with open(DATA_FILE) as file:
    groups = get_groups([line.rstrip() for line in file.readlines()])

    sum_of_any_yes = reduce(any_yes_answers, groups, 0)
    print(f'sum of any yes answers: {sum_of_any_yes}')

    sum_of_all_yes = reduce(all_yes_answers, groups, 0)
    print(f'sum of any yes answers: {sum_of_all_yes}')
