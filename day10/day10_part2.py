import pdb

def read_input(input_file):
    """
    Read in .txt input, each line is item in a list, and convert to int
    """
    with open(input_file) as f:
        lines = [line.strip() for line in f]

    return lines




# signal_strength = cycle_number * X
# eval_signals_at = [20,60, 100, 140, 180, 200]

commands = read_input('input.txt')
X = 1
cycle_number = 0
cycle_resets = [*range(39,259,40)]
height = 6
width = 40
pixels = [[' ' for j in range(width)] for i in range(height)]

class Sprite:
    def __init__(self):

        self.x2 = 1
        self.x1 = self.x2 - 1
        self.x3 = self.x2 + 1
        self.pos = [self.x1, self.x2, self.x3]

    def update_position(self, value):
        self.x2 += value
        self.x1 = self.x2 - 1
        self.x3 = self.x2 + 1
        self.pos = [self.x1, self.x2, self.x3]

def draw_pixel(cycle_number, sprite):

    row_number = cycle_number // 40
    row_pos = cycle_number % 40

    if row_pos in sprite.pos:
        pixels[row_number][row_pos] = '#'
    else:
        pixels[row_number][row_pos] = '.'

def run_command(command, X, cycle_number, sprite):

    #print(f"Running {command} | Starting X = {X}, cycle # = {cycle_number}")

    if command[:4] == 'addx':
        command, value = command.split(' ')

        # Cycle 1
        draw_pixel(cycle_number, sprite)
        cycle_number += 1
        # Cycle 2
        draw_pixel(cycle_number, sprite)
        cycle_number += 1

        #pdb.set_trace()
        sprite.update_position(int(value))

    elif command[:4] == 'noop':
        draw_pixel(cycle_number, sprite)
        cycle_number += 1

    return X, cycle_number, sprite


sprite_1 = Sprite()

for command in commands:
    X, cycle_number, sprite_1 = run_command(command, X, cycle_number, sprite_1)

for line in pixels:
    print(''.join(line))
# def chunks(lst, n):
#     """Yield successive n-sized chunks from lst."""
#     for i in range(0, len(lst)-n):
#         yield lst[i:i + n]
#
# for chunk in chunks(pixels, 40):
#     print(chunk)