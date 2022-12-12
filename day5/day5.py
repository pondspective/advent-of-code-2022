from collections import defaultdict
import re
import itertools

def parse_input(filename):
    with open(filename, "r", encoding="utf8") as f:
        stacks_str, commands = f.read().split("\n\n")

    # transform command
    regex = r"move (\d) from (\d) to (\d)"
    matches = re.finditer(regex, commands, re.MULTILINE)
    command_list = []
    for i in matches:
        command_list.append([int(param) for param in i.groups()])

    # transform stacks
    s_items, s_number = stacks_str.split("\n ")
    # [|] is empty stack
    stack_items = list(map(lambda x: x.strip().split(" "), s_items.replace("    ", " [|]").split("\n")))
    stack_items_tsp =  [stack[::-1] for stack in list(map(list, itertools.zip_longest(*stack_items, fillvalue=None)))]
    stack_nb = [int(num) for num in s_number.strip().split("   ")]
    stacks_dict = dict(zip(stack_nb, stack_items_tsp))

    return stacks_dict, command_list

stacks, commands = parse_input('test_input.txt')
print(stacks)
for command in commands:
    round, source, des = command
    print(f"Round -> {round} / Source -> {source} / Dest -> {des}")
    for i in range(0,round):
        if (len(stacks[source]) == 0):
            break
        if(stacks[source][-1] == '[|]'):
            stacks[source].pop()
        
        item = stacks[source].pop()
        stacks[des].append(item)
        print(f"Move {item} from {source} to {des} , #{i+1}")
    print(stacks)

        




