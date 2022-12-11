import re
import math
from copy import deepcopy
import pdb

def read_input(input_file):
    """
    Read in .txt input, each line is item in a list, and convert to int
    """
    monkeys = []
    with open(input_file) as f:

        monkey_groups = f.read().split('\n\n')
        for monkey in monkey_groups:
            monkey_lines = monkey.split('\n')
            monkey_lines = [line.strip() for line in monkey_lines]

            monkeys.append(monkey_lines)

    return monkeys


class Monkey:
    def __init__(self, monkey_info):
        self.id = int(monkey_info[0][-2]) # this will break if > 10 monkeys
        self.items = [int(item) for item in re.findall(r'(\d+)', monkey_info[1])]
        self.operation = re.findall(r'(?:=\s)(.+)', monkey_info[2])[0]
        self.test_val = int(re.findall(r'(\d+)', monkey_info[3])[0])
        self.test_true_monkey_id = int(monkey_info[4][-1])
        self.test_false_monkey_id = int(monkey_info[5][-1])
        self.inspection_counter = 0

    def __str__(self):
        return f"Monkey #{self.id}"

    def __repr__(self):
        return f"Monkey #{self.id}"


    def catch_item(self, item):
        self.items.append(item)

    def throw_item(self, item, monkey_id):
        print(f"Throwing item {item} to {monkey_id}")
        # Throw to the other monkey
        monkey_id.catch_item(item)
        # Remove the item from monkey's belongings
        self.items.remove(item)

    def run_operation(self,item):
        self.inspection_counter += 1
        operation_func = lambda old: eval(self.operation)
        print(f"Worry level: {item} -> ", end="")
        self.items[self.items.index(item)] = operation_func(item)
        print(f"{operation_func(item)}")
        return operation_func(item)

    def run_div_3_floor(self,item):
        self.items[self.items.index(item)] = math.floor(item / 3)
        print(f"Worry level: {item} -> {math.floor(item / 3)}")
        return math.floor(item / 3)

    def run_lcm_modulo(self,item,lcm):
        self.items[self.items.index(item)] = item % lcm
        print(f"Worry level: {item} -> {item % lcm}")
        return item % lcm

    def run_test(self,item):
        test_func = lambda x: x % self.test_val == 0

        if test_func(item):
            self.throw_item(item, monkey_dict[self.test_true_monkey_id])

        elif not test_func(item):
            self.throw_item(item, monkey_dict[self.test_false_monkey_id])




input = read_input('input.txt')

# Create dict of Monkeys
monkey_dict = {}
for i, monkey_info in enumerate(input):
    monkey_dict[i] = Monkey(monkey_info)

for round in range(1,10001):

    divisors = []
    for i, monkey in monkey_dict.items():
         divisors.append(monkey.test_val)
    lowest_common_multiple = math.lcm(*divisors)

    for i, monkey in monkey_dict.items():
        print("="*50)
        print(f"{monkey}")
        print("=" * 50)

        print(f"ITEMS: {monkey.items}")
        item_copy = deepcopy(monkey.items)
        for item in item_copy:
            print(f"Processing item: {item}", end="\n\n")

            item = monkey.run_operation(item)
            #item = monkey.run_div_3_floor(item)
            item = monkey.run_lcm_modulo(item,lowest_common_multiple)
            monkey.run_test(monkey.items[monkey.items.index(item)])

    print("=" * 50)
    print(f"END OF ROUND #{round}")
    print("=" * 50)
    inspections = []
    for i, monkey in monkey_dict.items():
        print(f"{monkey} | {monkey.items} | Inspections: {monkey.inspection_counter}")
        inspections.append(monkey.inspection_counter)

    inspections = sorted(inspections)
    monkey_business = inspections[-1] * inspections[-2]
    print(monkey_business)


