DATA_FILE = './data/day22.txt'


def play_round(deck_one, deck_two):
    one_go = deck_one[0]
    two_go = deck_two[0]
    if one_go > two_go:
        deck_one.append(one_go)
        deck_one.append(two_go)
    elif two_go > one_go:
        deck_two.append(two_go)
        deck_two.append(one_go)
    else:
        raise Exception('No one won the round')
    return deck_one[1:], deck_two[1:]


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


with open(DATA_FILE) as file:
    lines = file.readlines()
    player_one_deck, player_two_deck = get_starting_decks(lines)

    while no_winner(player_one_deck, player_two_deck):
        player_one_deck, player_two_deck = play_round(player_one_deck, player_two_deck)

    winner = get_winner(player_one_deck, player_two_deck)
    winning_score = get_winning_score(winner)
    print(f'Winning score: {winning_score}')
