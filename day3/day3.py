from functools import reduce
import math

f = open('input.txt','r')
input_text = f.read()

INPUT_TEST = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

def process_rucksack(input, spilt_compartment = True):
    if spilt_compartment:
        return [spilt_compartments(line) for line in input.split('\n')]
    else:
        return [line for line in input.split('\n')]

# split rucksack into 2 compartments
def spilt_compartments(str):
    return [str[:int(len(str)/2)],str[int(len(str)/2):]]

def to_priority(rucksack):
    res = []
    for item in rucksack:
        priority = ord(item) - 38 if item.isupper() else ord(item) - 96
        res.append(priority)
    return res

# group three rucksack into badges
def group_badges(rucksacks):
    badges = []
    for n in range (0,math.ceil(len(rucksacks)/3)):
        tmp = [rucksacks[3*n + i] for i in range(0,3)]
        print(tmp)
        badges.append(tmp)
    return badges


def find_duplicate_number(c1, c2):
    c1 = sorted(c1)
    c2 = sorted(c2)

    print(c1, c2)

    for i in range(0,int(len(c1))):
        for j in range(0,int(len(c2))):
            if c1[i] == c2[j]:
                print(c1[i] ,'is duplicate')
                return c1[i]
            elif c1[i] > c2[j]:
                print(f"c1 -> {i},{c1[i]}")
                print(f"c2 -> {j},{c2[j]}")
                j += 1

def find_many_duplicate_numbers(c1, c2):
    c1 = sorted(c1)
    c2 = sorted(c2)

    print(c1, c2)

    dup_nums = []
    for i in range(0,int(len(c1))):
        for j in range(0,int(len(c2))):
            if c1[i] == c2[j]:
                print(c1[i] ,'is duplicate')
                dup_nums.append(c1[i])
                j += 1
            elif c1[i] > c2[j]:
                print(f"c1 -> {i},{c1[i]}")
                print(f"c2 -> {j},{c2[j]}")
                j += 1
    
    print(f"Duplicate Nums List -> {dup_nums}")
    return(dup_nums)

def part1(input):
    priority_scores = [find_duplicate_number(to_priority(compartment[0]), to_priority(compartment[1])) for compartment in process_rucksack(input)]
    return reduce(lambda x, y: x+y,priority_scores)

def part2(input):
    res = []
    badges = group_badges(process_rucksack(input, spilt_compartment=False))
    for badge in badges:
        badge = [to_priority(c) for c in badge]
        dup_1_2 = find_many_duplicate_numbers(badge[0], badge[1])
        res.append(find_duplicate_number(dup_1_2, badge[2]))
    
    return reduce(lambda x, y: x+y,res)

print(part1(input_text))
print("*************************************")
print(part2(input_text))