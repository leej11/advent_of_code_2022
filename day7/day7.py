import re
from pprint import pprint
import pandas as pd
import pdb

def read_input(input_file):
    """
    Read in .txt input, each line is item in a list, and convert to int
    """
    with open(input_file) as f:
        input = f.read()

    input = input.split('$')
    input = [line.strip().split('\n') for line in input]

    return input

input = read_input('input.txt')



curr_dir = '/'
dir_dict = {}
for line in input:

    print(line)
    print(curr_dir)

    if line[0][:2] == 'cd':

        chdir_to = re.findall(r"[^\s]+$", line[0])[0]
        print(chdir_to)
        if chdir_to == '/':
            curr_dir = '/'
            print(f"Changing dir to: {curr_dir}")

        elif chdir_to == '..':
            curr_dir = re.sub(r"\w+\/$", '', curr_dir)
            print(f"Changing dir to: {curr_dir}")
        else:
            curr_dir += (chdir_to + '/')
            print(f"Changing dir to: {curr_dir}")

    elif line[0][:2] == 'ls':

        dir_dict[curr_dir] = {}

        for file_or_dir in line[1:]:
            if file_or_dir[:3] == 'dir':
                pass
                # dir = re.findall(r"[^\s]+$", file_or_dir)[0]
                # dir_dict[curr_dir][file_or_dir] = f'{curr_dir}{dir}/'
            else:
                size, file = file_or_dir.split(' ')
                dir_dict[curr_dir][file] = int(size)

    print('='*50)

pprint(dir_dict)


# Write some code to put children sums in their parents
print("="*50)
print("Beginning summing")
print("="*50)

patterns = {}
for key in dir_dict.keys():
    print("="*50)
    print(key)
    matches = re.findall(r"(/|\w+\/{1})", key)

    for i, match in enumerate(matches):

        dir_string = ''.join(matches[:i+1])
        dir_sum = sum(dir_dict[key].values())
        print(f"{dir_string}: Adding {dir_sum} to it")

        if dir_string not in patterns:
            patterns[dir_string] = 0
        patterns[dir_string] += dir_sum
    #print(matches)

pprint(patterns)
df = pd.DataFrame.from_dict(patterns, orient="index", columns=['size'])
print(df[df['size'] <= 100000].sum())


filesystem_size = 70000000
space_required = 30000000
total_used_space = patterns['/']
remaining_space = filesystem_size - total_used_space

space_to_free_up = space_required - remaining_space

print(f"Used space: {total_used_space}\nRemaining space: {remaining_space}\nSpace to free up: {space_to_free_up}")

print(df[df['size'] >= space_to_free_up].sort_values(by='size').iloc[0]['size'])
