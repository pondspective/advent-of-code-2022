from parse import compile, parse
from functools import reduce

f = open('2023-python/day4.txt','r')
input_text = f.read()

card_instance_cache = {}
def create_num_set(nums_str):
    res = [int(num) for num in nums_str.split(" ") if num != ""]
    return set(res)

def count_win_numbers(input):
    cnt_win_nums = []
    for line in input.split("\n"):
        card = parse("Card {id}: {winning_num} | {num_to_check}", line).named
        card['winning_num'] = create_num_set(card['winning_num'])
        card['num_to_check'] = create_num_set(card['num_to_check'])
        cnt_win_nums.append(len(card['winning_num'].intersection(card['num_to_check'])))
    return cnt_win_nums
    
def part_1(input):
    cnt_win_nums = count_win_numbers(input)
    return reduce((lambda x, y: x + y),map(lambda cnt: 2**(cnt-1) if cnt > 0 else 0, cnt_win_nums))

def part_2(input):
    arr = count_win_numbers(input)
    for i in range(0,len(arr)):
        cnt_card_instances(i,arr)
    print(card_instance_cache)
    return sum(card_instance_cache.values())
    
def cnt_card_instances(index,arr):
    sum = 0
    if arr[index] == 0:
        # print(f"Card : {index+1}, end loop base case, res : 1")
        card_instance_cache[index] = 1
        return 1
    if index in card_instance_cache.keys():
        return card_instance_cache[index]
    for i in range (index+1,index+1+arr[index]):
        res = cnt_card_instances(i,arr)
        # print(f"Card : {index+1}, call func : cnt_card_instances({i},arr), res : {res}")
        sum += res
    card_instance_cache[index] = sum+1
    return card_instance_cache[index]

print(part_1(input_text))
print(part_2(input_text))
