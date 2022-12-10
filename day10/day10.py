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
cycle_evaluations = [*range(20,260,40)]
X_evaluations = []

def run_command(command, X, cycle_number):

    #print(f"Running {command} | Starting X = {X}, cycle # = {cycle_number}")

    if command[:4] == 'addx':
        command, value = command.split(' ')
        cycle_number += 1
        if cycle_number in cycle_evaluations:
            print(f"Cycle {cycle_number}: X={X}")
            X_evaluations.append(X)
        cycle_number += 1
        if cycle_number in cycle_evaluations:
            print(f"Cycle {cycle_number}: X={X}")
            X_evaluations.append(X)
        X += int(value)


    elif command[:4] == 'noop':
        cycle_number += 1
        if cycle_number in cycle_evaluations:
            print(f"Cycle {cycle_number}: X={X}")
            X_evaluations.append(X)

    #print(f"Finished {command} | Ending X = {X}, cycle # = {cycle_number}")

    return X, cycle_number



for command in commands:
    X, cycle_number = run_command(command, X, cycle_number)

print(sum(cycle * X for cycle, X in zip(cycle_evaluations, X_evaluations)))


X cotrols horizontal (x) position of the 'sprite'.
Sprite is 3 pixels wide
X sets middle position of the sprite
width = 40
height = 6