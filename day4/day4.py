from functools import reduce
import math

f = open('input.txt','r')
input_text = f.read()

INPUT_TEST = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

def process_assignment_list(input):
    res = [line.split(",") for line in input.split("\n")]
    return res

def extract_start_end(str):
    start_end = str.split('-')
    return {'start':int(start_end[0])
            ,'end':int(start_end[1])
            ,'length':int(start_end[1]) - int(start_end[0]) + 1}

def is_between(compare_num ,lower, upper):
    return lower <= compare_num <= upper

def is_fully_overlapse(task1, task2):
    if task1['length'] > task2['length']:
        return (task1['start'] <= task2['start']) & (task1['end'] >= task2['end'])
    elif task1['length'] < task2['length']:
        return (task1['start'] >= task2['start']) & (task1['end'] <= task2['end'])
    else:
        return (task1['start'] == task2['start']) & (task1['end'] == task2['end'])

def is_overlapse(task1, task2):
    if task1['length'] < task2['length']:
        tmp = task1
        task1 = task2
        task2 = tmp
    return is_between(compare_num=task2['start'], lower=task1['start'], upper=task1['end']) | \
        is_between(compare_num=task2['end'], lower=task1['start'], upper=task1['end'])
    

def part1(input):
    count = 0
    for tasks in process_assignment_list(input):
        elf1_task = extract_start_end(tasks[0])
        elf2_task = extract_start_end(tasks[1])
        print(f"elf1 -> {tasks[0]}, elf2 -> {tasks[1]}, fully overlapse ? -> {is_fully_overlapse(elf1_task,elf2_task)}")
        count += 1 if is_fully_overlapse(elf1_task,elf2_task) else 0
    return count
    
def part2(input):
    count = 0
    for tasks in process_assignment_list(input):
        elf1_task = extract_start_end(tasks[0])
        elf2_task = extract_start_end(tasks[1])
        print(f"elf1 -> {tasks[0]}, elf2 -> {tasks[1]}, overlapse ? -> {is_overlapse(elf1_task,elf2_task)}")
        count += 1 if is_overlapse(elf1_task,elf2_task) else 0
    return count

print(part1(input_text))
print(part2(input_text))
