from functools import reduce

f = open('input.txt','r')
input_text = f.read()

INPUT_TEST = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

def process_rucksack(input):
    return [spilt_compartments(line) for line in input.split('\n')]

def spilt_compartments(str):
    return [str[:int(len(str)/2)],str[int(len(str)/2):]]

def to_priority(rucksack):
    res = []
    for item in rucksack:
        priority = ord(item) - 38 if item.isupper() else ord(item) - 96
        res.append(priority)
    return res
            

def find_duplicate_number(c1, c2):
    c1 = sorted(c1)
    c2 = sorted(c2)

    print(c1, c2)

    for i in range(0,int(len(c1)/2)):
        for j in range(0,int(len(c2)/2)):
            if c1[i] == c2[j]:
                print(c1[i] ,'is duplicate')
                return c1[i]
            elif c1[i] > c2[j]:
                print(f"c1 -> {i},{c1[i]}")
                print(f"c2 -> {j},{c2[j]}")
                j += 1
            # elif c1[i] < c2[j]:
            #     print(f"c1 -> {i},{c1[i]}")
            #     print(f"c2 -> {j},{c2[j]}")
            #     i += 1

print([find_duplicate_number(to_priority(compartment[0]), to_priority(compartment[1])) for compartment in process_rucksack(INPUT_TEST)])
