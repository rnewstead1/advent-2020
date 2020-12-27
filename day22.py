DATA_FILE = './data/day22.txt'


def play_round(card_one, deck_one, card_two, deck_two):
    if card_one > card_two:
        deck_one.append(card_one)
        deck_one.append(card_two)
    elif card_two > card_one:
        deck_two.append(card_two)
        deck_two.append(card_one)
    else:
        raise Exception('No one won the round')
    return deck_one, deck_two


def get_winner(deck_one, deck_two):
    return deck_one if len(deck_one) != 0 else deck_two


def get_winning_score(deck):
    score = 0
    length = len(deck)
    for index, val in enumerate(deck):
        score += (length - index) * val
    return score


def get_starting_decks(lines):
    player_one_index = lines.index('Player 1:\n')
    player_two_index = lines.index('Player 2:\n')
    player_one_deck = [int(line.rstrip()) for line in lines[player_one_index + 1:player_two_index - 1]]
    player_two_deck = [int(line.rstrip()) for line in lines[player_two_index + 1:]]
    return player_one_deck, player_two_deck


def no_winner(deck_one, deck_two):
    return len(deck_one) != 0 and len(deck_two) != 0


def play_combat(deck_one, deck_two):
    one = deck_one.copy()
    two = deck_two.copy()
    while no_winner(one, two):
        one, two = play_round(one.pop(0), one, two.pop(0), two)
    return get_winner(one, two)


def can_recurse(current_card, deck):
    return current_card <= len(deck)


def play_recursive_combat(one, two):
    deck_one = one.copy()
    deck_two = two.copy()
    history = set()
    while no_winner(deck_one, deck_two):
        if (tuple(deck_one), tuple(deck_two)) in history:
            return deck_one, []
        else:
            history.add((tuple(deck_one), tuple(deck_two)))
            card_one = deck_one.pop(0)
            card_two = deck_two.pop(0)
            if can_recurse(card_one, deck_one) and can_recurse(card_two, deck_two):
                copy_one, copy_two = play_recursive_combat(deck_one[:card_one].copy(), deck_two[:card_two].copy())
                if len(copy_one) != 0:
                    deck_one.append(card_one)
                    deck_one.append(card_two)
                else:
                    deck_two.append(card_two)
                    deck_two.append(card_one)
            else:
                deck_one, deck_two = play_round(card_one, deck_one, card_two, deck_two)
    return deck_one, deck_two


with open(DATA_FILE) as file:
    lines = file.readlines()
    player_one_deck, player_two_deck = get_starting_decks(lines)

    combat_winner = play_combat(player_one_deck, player_two_deck)
    print(f'Winning combat score: {get_winning_score(combat_winner)}')

    recursive_combat_winner = get_winner(*(play_recursive_combat(player_one_deck, player_two_deck)))
    print(f'Winning recursive combat score: {get_winning_score(recursive_combat_winner)}')
