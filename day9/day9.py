import pdb
from copy import deepcopy

head_visited_positions = [[0,0]]
tail_visited_positions = [[0,0]]

def read_input(input_file):
    """
    Read in .txt input, each line is item in a list, and convert to int
    """
    with open(input_file) as f:
        lines = [line.strip() for line in f]
        commands = []
        for command in lines:
            direction, val = command.split(' ')
            commands.append((direction, int(val)))

    return commands



def run_command(command, head_pos, tail_pos):

    direction = command[0]
    value = command[1]

    for i in range(value):
        head_pos, tail_pos = update_position(head_pos, tail_pos, direction)


def tail_attached(head_pos, tail_pos):

    if (abs(head_pos[0] - tail_pos[0])) > 1 or (abs(head_pos[1] - tail_pos[1])) > 1:
        return False
    else:
        return True

def update_position(head_pos, tail_pos, direction):

    head_initial = deepcopy(head_pos)

    #pdb.set_trace()
    if direction == 'L':
        head_pos[0] -= 1
        if not tail_attached(head_pos, tail_pos):
            tail_pos[0] = head_initial[0]
            tail_pos[1] = head_initial[1]

    elif direction == 'R':
        head_pos[0] += 1
        if not tail_attached(head_pos, tail_pos):
            tail_pos[0] = head_initial[0]
            tail_pos[1] = head_initial[1]

    elif direction == 'U':
        head_pos[1] += 1
        if not tail_attached(head_pos, tail_pos):
            tail_pos[0] = head_initial[0]
            tail_pos[1] = head_initial[1]

    elif direction == 'D':
        head_pos[1] -= 1
        if not tail_attached(head_pos, tail_pos):
            tail_pos[0] = head_initial[0]
            tail_pos[1] = head_initial[1]
    else:
        raise ValueError

    print(f"Head: {head_pos}, Tail:{tail_pos}")

    head_visited_positions.append(deepcopy(head_pos))
    tail_visited_positions.append(deepcopy(tail_pos))

    return head_pos, tail_pos

commands = read_input('input.txt')
print(commands)

head_pos = [0,0]
tail_pos = [0,0]

for command in commands:
    print("="*50)
    print(f"{command}, | Head: {head_pos} | Tail: {tail_pos}")
    print("=" * 50)
    run_command(command,head_pos,tail_pos)

tail_visited_positions_set = set(tuple(pos) for pos in tail_visited_positions)
head_visited_positions_set = set(tuple(pos) for pos in head_visited_positions)

print(f"Tail Visits: #{len(tail_visited_positions_set)} | {tail_visited_positions_set}")
print(f"Head Visits: #{len(head_visited_positions_set)} | {head_visited_positions_set}")