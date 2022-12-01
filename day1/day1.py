from itertools import groupby
from typing import List, Dict


def read_input(input_file):
    """
    Read in .txt input, each line is item in a list, and convert to int
    """
    with open(input_file) as f:
        input_list = ['' if line.rstrip() == '' else int(line.rstrip()) for line in f]

    return input_list


# define separator keys
def split_condition(x):
    return x in {''}


def get_top_elves(n: int, elf_dict: Dict[int, List[int]], agg='sum'):
    """

    :param n: Top 'n' elves to be returned
    :param elf_dict: Dict of elves and their associated list of snacks (in terms of calories)
    :param agg: If we want to look at SUM of calories for each elf, use 'sum'
    :return:
    """
    if agg=='sum':
        for i in elf_dict.keys():
            elf_dict[i] = sum(elf_dict[i])

    top_n_elf_keys = sorted(elf_dict, key=elf_dict.get, reverse=True)[:n]
    return top_n_elf_keys


if __name__ == '__main__':
    input = read_input('input.txt')
    # define groupby object
    grouper = groupby(input, key=split_condition)
    # convert to dictionary via enumerate
    res = dict(enumerate((list(j) for i, j in grouper if not i), 1))

    top_elves = get_top_elves(3, res, 'sum')

    total_calories = 0
    for top_elf in top_elves:
        total_calories += res[top_elf]

    print(total_calories)
