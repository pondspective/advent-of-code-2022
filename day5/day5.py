from collections import defaultdict
import re
import itertools
from parse import compile

# Expected Result
#     [D]
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# {
#     1 : 'NZ',
#     2 : 'DCM',
#     3 : 'P'
# }

def parse_input(filename):
    with open(filename, "r", encoding="utf8") as f:
        stacks_str, commands = f.read().split("\n\n")

    # transform command
    extract_command = compile("move {:d} from {:d} to {:d}")
    command_list = [list(extract_command.parse(command)) for command in commands.split('\n')]

    # transform stacks
    s_items, s_number = stacks_str.split("\n ")
    rows = s_items.split("\n")
    stack_nb = [int(num) for num in s_number.strip().split("   ")]
    stacks_dict = {}
    for stack in stack_nb:
        items = []
        for i in range(len(rows)-1, -1, -1):
            pos = 4*stack-3
            if (len(rows[i]) > pos):
                if (rows[i][pos] != ' '):
                    items.append(rows[i][pos])
        stacks_dict.update({stack:items})

    return stacks_dict, command_list

def move_item(stack ,source, des):
    if len(stack[source]) != 0:
        item = stack[source].pop()
        stack[des].append(item)
        print(f"Move {item} from {source} to {des}")
    return stack

def move_item_n_times(stack ,source, des, round):
    print(f"+++ Move from {source} to {des} x{round} +++")
    for i in range(0,round):
        stack = move_item(stack, source, des)
    return stack

def move_many_items(stack ,source, des, items):
    items = items if len(stack[source]) >= items else len(stack[source])
    # removed, insert = stack[source][:len(stack[source])-items], stack[source][-items:]
    print(f"Move {items} from {source} to {des}")
    stack[des] = stack[des]+stack[source][-items:]
    stack[source] = stack[source][:len(stack[source])-items]
    print(stack)
    return stack

def part1(path):
    stacks, commands = parse_input(path)
    print(stacks)
    for command in commands:
        round, source, des = command
        stacks = move_item_n_times(stacks, source, des, round)
    print("FINAL STACK")
    print(stacks)
    final_word = "".join([stack[-1] for stack in stacks.values()])
    return final_word

def part2(path):
    stacks, commands = parse_input(path)
    print(stacks)
    for command in commands:
        items, source, des = command
        stacks = move_many_items(stacks, source, des, items)
    final_word = "".join([stack[-1] for stack in stacks.values()])
    return final_word

print(part1('input.txt'))
print(part2('input.txt'))




