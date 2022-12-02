import pdb

def read_input(input_file):
    """
    Read in .txt input, each line is item in a list, and convert to int
    """
    with open(input_file) as f:
        input_list = [(line.rstrip()[0], line.rstrip()[2]) for line in f]

    return input_list


def shape_score(shape):
    if shape == 'A':
        return 1
    elif shape == 'B':
        return 2
    elif shape == 'C':
        return 3
    elif shape == 'X':
        return 1
    elif shape == 'Y':
        return 2
    elif shape == 'Z':
        return 3

def determine_play(p1, p2):

    strategies = {
        'X': {'Name': 'Lose', 'Score': 0, 'Strategy_Map': {'A':'Z', 'B': 'X', 'C':'Y'}},
        'Y': {'Name': 'Draw', 'Score': 3, 'Strategy_Map': {'A':'X', 'B': 'Y', 'C':'Z'}},
        'Z': {'Name': 'Win', 'Score': 6, 'Strategy_Map': {'A':'Y', 'B': 'Z', 'C':'X'}},
    }

    score = 0
    move = strategies[p2]['Strategy_Map'][p1]
    score += strategies[p2]['Score']
    score += shape_score(move)

    return score


input = read_input('input.txt')
print(input)

round_scores = []
for round in input:
    p1, p2 = round
    round_scores.append(determine_play(p1, p2))

print(sum(round_scores))