import pdb
from copy import deepcopy
import numpy as np



class Knot:
    def __init__(self, id):
        self.pos = [0,0]
        self.id = id
        self.positions_visited = [[0,0]]

    def __str__(self):
        return f"Knot #{self.id}"

    def __repr__(self):
        return f"Knot #{self.id}"

    def move(self, direction):

        self.prev_pos = deepcopy(self.pos)

        if direction == 'L':
            self.pos[0] -= 1
        elif direction == 'R':
            self.pos[0] += 1
        elif direction == 'U':
            self.pos[1] += 1
        elif direction == 'D':
            self.pos[1] -= 1
        else:
            raise ValueError

        self.positions_visited.append(deepcopy(self.pos))

    def update_position(self, new_position):
        self.prev_pos = deepcopy(self.pos)
        self.pos = new_position
        self.positions_visited.append(new_position)

    def get_distinct_positions_visited(self):
        return set(tuple(pos) for pos in self.positions_visited)





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




def update_positions(knots, direction):

    for i in range(len(knots)):

        # Move the head knot
        if i == 0:
            knots[i].move(direction)
            print(f"Moving {knots[i]} | {knots[i].prev_pos} -> {knots[i].pos}")
            continue

        # For each subsequent knot, check if the one before it is too far away
        # and thus needs to be pulled to new position
        x_diff = (knots[i-1].pos[0] - knots[i].pos[0])
        y_diff = (knots[i-1].pos[1] - knots[i].pos[1])
        if (abs(knots[i].pos[0] - knots[i-1].pos[0])) > 1 or (abs(knots[i].pos[1] - knots[i-1].pos[1])) > 1:
            # Update the position
            # print(f"Moving {knots[i]} | {knots[i].pos} -> {knots[i-1].prev_pos}")
            # knots[i].update_position(knots[i-1].prev_pos)

            x_diff_sign = -1 if x_diff < 0 else 1
            y_diff_sign = -1 if y_diff < 0 else 1

            # If it's in either the same row or column, then just move in the same direction
            if x_diff == 0:
                new_x = deepcopy(knots[i].pos[0])
                new_y = deepcopy(knots[i].pos[1]) + (y_diff_sign * 1)
                print(f"Moving {knots[i]} | {knots[i].pos} -> {[new_x, new_y]}")
                knots[i].update_position([new_x, new_y])

            elif y_diff == 0:
                new_x = deepcopy(knots[i].pos[0]) + (x_diff_sign * 1)
                new_y = deepcopy(knots[i].pos[1])
                print(f"Moving {knots[i]} | {knots[i].pos} -> {[new_x, new_y]}")
                knots[i].update_position([new_x, new_y])

            # If it is in different row AND column, it will need to move diagonally
            else:
                new_x = deepcopy(knots[i].pos[0]) + (x_diff_sign * 1)
                new_y = deepcopy(knots[i].pos[1]) + (y_diff_sign * 1)
                print(f"Moving {knots[i]} | {knots[i].pos} -> {[new_x, new_y]}")
                knots[i].update_position([new_x, new_y])



tail_visited_positions = [[0,0]]
n_knots = [*range(10)]
knots = []
knots = [Knot(i) for i in n_knots]
commands = read_input('input.txt')


for command in commands:

    direction = command[0]
    value = command[1]

    print("="*50)
    print(f"COMMAND: {command[0]} {command[1]}")
    print("=" * 50)
    for _ in range(value):
        update_positions(knots, direction)
        print("-"*50)

print(knots[9].positions_visited)
print(knots[9].get_distinct_positions_visited())
print(len(knots[9].get_distinct_positions_visited()))

# tail_visited_positions_set = set(tuple(pos) for pos in tail_visited_positions)
# head_visited_positions_set = set(tuple(pos) for pos in head_visited_positions)
#print(f"{tail_visited_positions}")
#print(f"Tail Visits: #{len(tail_visited_positions_set)} | {tail_visited_positions_set}")
# print(f"Head Visits: #{len(head_visited_positions_set)} | {head_visited_positions_set}")