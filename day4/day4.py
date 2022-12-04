import pdb


def read_input(input_file):
    """
    Read in .txt input, each line is item in a list, and convert to int
    """
    with open(input_file) as f:
        #input_list = [line.rstrip().split(',') for line in f]
        input_list = []
        elf_sector_coverage = {}

        for i, line in enumerate(f):
            #print("")
            line = line.rstrip().split(',')

            elf_coverage = []
            for elf, srange in enumerate(line):
                start, end = srange.split('-')
                sections = list(range(int(start),int(end)+1))
                #print(f"Elf {elf}: {sections}")
                elf_coverage.append(sections)

            elf_sector_coverage[i] = elf_coverage

    return elf_sector_coverage

def part_1():
    elf_sector_coverage = read_input('input.txt')

    subset_counter = 0
    for i, item in elf_sector_coverage.items():

        if (set(item[0]).issubset(item[1])) or (set(item[1]).issubset(item[0])):
            subset_counter += 1

    print(subset_counter)

def part_2():
    elf_sector_coverage = read_input('input.txt')
    no_overlap_counter = 0

    for i, item in elf_sector_coverage.items():

        if set(item[0]).isdisjoint(item[1]):
            no_overlap_counter += 1

    print(len(elf_sector_coverage) - no_overlap_counter)

part_2()

