import string


def read_input(input_file):
    """
    Read in .txt input, each line is item in a list, and convert to int
    """
    with open(input_file) as f:
        input_list = [line.rstrip() for line in f]

    return input_list

input = read_input('input.txt')

def create_azAz_dict():
    my_l = [l for l in string.ascii_lowercase] + [l for l in string.ascii_uppercase]
    return {l: i+1 for i, l in enumerate(my_l)}


def part_1():
    input = read_input('input.txt')
    azAz_d = create_azAz_dict()
    duplicates = []
    for rucksack in input:

        half = int(len(rucksack) / 2)
        # print(half)
        c1 = rucksack[0:half]
        c2 = rucksack[half:len(rucksack)]

        intersection = list(set(c1).intersection(set(c2)))
        if len(intersection) > 1:
            raise ValueError
        print(f"Duplicate: {intersection[0]}, Value: {azAz_d[intersection[0]]}")
        duplicates.append(azAz_d[intersection[0]])

    print(sum(duplicates))




def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def part_2():
    azAz_d = create_azAz_dict()
    input = read_input('input.txt')
    badge_item_vals = []

    for group in chunks(input, 3):
        badge_item = list(set(group[0]).intersection(group[1]).intersection((group[2])))[0]
        print(f"{badge_item}: {azAz_d[badge_item]}")
        badge_item_vals.append(azAz_d[badge_item])

    print(sum(badge_item_vals))

part_2()
#part_1()