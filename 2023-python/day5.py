from parse import compile, parse
from functools import reduce

f = open('2023-python/day5.txt','r')
input_text = f.read()

test_case = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

def process_map(input):
    maps = input.split("\n\n")
    seeds = maps.pop(0)
    parsed_seeds = parse("seeds: {items}", seeds).named
    transformed_seeds = [int(seed) for seed in parsed_seeds['items'].split(" ")]
    source_to_dest, transformed_maps = {}, {}
    for map_ in maps:
        lines = map_.split("\n")
        map_name = lines.pop(0)
        parsed_map_name = parse("{from_}-to-{to_} map:", map_name).named
        source_to_dest[parsed_map_name['from_']] = parsed_map_name['to_']
        lst = []
        for line in lines:
            tmp_item = {}
            tmp_item['destination'], tmp_item['source_start'], tmp_item['length'] = [int(item) for item in line.split(" ")]
            tmp_item['source_end'] = tmp_item['source_start'] + tmp_item['length'] - 1
            tmp_item['diff'] = tmp_item['destination'] - tmp_item['source_start']
            tmp_item['destination_end'] = tmp_item['source_end'] + tmp_item['diff']
            lst.append(tmp_item)
        lst = sorted(lst, key=lambda d: d['destination']) 
        transformed_maps[parsed_map_name['to_']] = lst
    return transformed_maps, source_to_dest, transformed_seeds

def convert_to(number,from_,to_,maps,source_dest):
    while True:
        dest = source_dest[from_]
        map_ = maps[dest]
        for item in map_:
            if item['source_start'] <= number <= item['source_end']:
                print(f"Convert {from_} -> {dest} : {number} -> {number+item['diff']}")
                number = number+item['diff']
                break
        if (source_dest[from_] == to_):
            return number
        from_ = dest

def bruteforce_generate_series(lst):
    series = []
    for i in range(0,int(len(lst)/2)):
        print(lst[i*2], lst[i*2+1])
        series += [num for num in range(lst[i*2], lst[i*2]+lst[i*2+1])]
    return series

def part_1(input):
    transformed_maps, source_to_dest, seeds = process_map(input)
    converted = []
    for seed in seeds:
        res = convert_to(seed,"seed","location",transformed_maps, source_to_dest)
        print(res)
        converted.append(res)
    return min(converted)

# print(process_map(input_text)[0])
# print(part_1(input_text))
transformed_maps, source_to_dest, seeds = process_map(input_text)
min_ = 99999999999
for i in range(0,int(len(seeds)/2)):
    print(seeds[i*2], seeds[i*2+1])
    for num in range(seeds[i*2], seeds[i*2]+seeds[i*2+1]):
        res = convert_to(num,"seed","location",transformed_maps, source_to_dest)
        min_ = res if min_ > res else min_
print(min_)