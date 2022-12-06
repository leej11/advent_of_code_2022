import pdb

def read_stack_map(input_file):
    """
    Read in .txt input, each line is item in a list, and convert to int
    """
    with open(input_file) as f:
        lines = f.readlines()

    stack_map = []
    for line in lines:
        if line == '\n':
            break
        stack_map.append(line)

    return stack_map


def read_instructions(input_file):
    """
    Read in .txt input, each line is item in a list, and convert to int
    """
    with open(input_file) as f:
        lines = f.readlines()

    instructions = []
    for line in lines:
        if line[:4] == 'move':
            instructions.append(line.strip())

    return instructions


stack_map = read_stack_map('input.txt')
print(stack_map)

stack_map_n_cols = int(stack_map[-1][-2:-1])

lines = []
for line in stack_map[:-1]:
    tmp_line = []

    for i in range(1, stack_map_n_cols+1):

        zero_i = i-1
        location = (zero_i * 4) + 1

        if len(line) < location:
            tmp_line.append(' ')
        else:
            tmp_line.append(line[location])

    lines.append(tmp_line)

print(lines)
# Initialize the crate column dict
crate_dict = {}
for i in range(1,stack_map_n_cols+1):
    crate_dict[i] = []


for line_i, line in enumerate(lines, start=1):

    for i, crate in enumerate(line, start=1):
        if crate != ' ':
            if line_i == 1:
                crate_dict[i].append(crate)
            else:
                crate_dict[i].insert(0,crate)

print(crate_dict)


instructions = read_instructions('input.txt')



def follow_instructions(crate_dict, instructions):

    for instruction in instructions:

        x = instruction.split(' ')
        quantity = int(x[1])
        from_col = int(x[3])
        to_col = int(x[5])

        for i in range(quantity):

            copy = crate_dict[from_col].pop(-1)
            #copy = crate_dict[from_col][-1]
            crate_dict[to_col].append(copy)

    return crate_dict


def follow_instructions_part_2(crate_dict, instructions):

    for instruction in instructions:

        x = instruction.split(' ')
        quantity = int(x[1])
        from_col = int(x[3])
        to_col = int(x[5])

        copy = crate_dict[from_col][-quantity:]
        del crate_dict[from_col][-quantity:]
        # Adjoin the copied items
        crate_dict[to_col] = crate_dict[to_col] + copy

    return crate_dict

print(instructions)

print(crate_dict)

def get_final_answer(crate_dict):
    result = ''
    for i in range(1,stack_map_n_cols+1):
        result += str(crate_dict[i][-1])

    print(result)

instructions = read_instructions('input.txt')
crate_dict = follow_instructions_part_2(crate_dict, instructions)
get_final_answer(crate_dict)