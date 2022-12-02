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

def determine_victory(p1, p2):

    if p1 == 'A':
        if p2 == 'X':
            return 3
        elif p2 == 'Y':
            return 6
        elif p2 == 'Z':
            return 0

    elif p1 == 'B':
        if p2 == 'X':
            return 0
        elif p2 == 'Y':
            return 3
        elif p2 == 'Z':
            return 6

    elif p1 == 'C':
        if p2 == 'X':
            return 6
        elif p2 == 'Y':
            return 0
        elif p2 == 'Z':
            return 3




input = read_input('input.txt')
print(input)


round_scores = []
for round in input:
    p1, p2 = round
    score = 0
    score += shape_score(p2)
    score += determine_victory(p1, p2)
    round_scores.append(score)

print(sum(round_scores))