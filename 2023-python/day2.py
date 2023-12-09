from parse import compile, parse
import functools 

PART1_CUBE_LIMIT = {"red":12,"green":13,"blue":14}

def part_1(input):
    res = 0
    for line in input.split("\n"):
        game = parse("Game {id}:{cubes}", line).named
        for round in game['cubes'].split(";"):
            is_possible = True
            for revealed_cube_raw in round.split(","):
                revealed_cube = parse("{num} {color}", revealed_cube_raw.strip()).named
                if PART1_CUBE_LIMIT[revealed_cube['color']] < int(revealed_cube['num']):
                    is_possible = False
                    break
            if is_possible == False:
                break
        if is_possible:
            res += int(game['id'])
    return res

def part_2(input):
    res = 0
    for line in input.split("\n"):
        game = parse("Game {id}:{cubes}", line).named
        least_possible_cubes = {"red":0,"green":0,"blue":0}
        for round in game['cubes'].split(";"):
            for revealed_cube_raw in round.split(","):
                revealed_cube = parse("{num} {color}", revealed_cube_raw.strip()).named
                least_possible_cubes[revealed_cube['color']] = max(least_possible_cubes[revealed_cube['color']], int(revealed_cube['num']))
        res += functools.reduce(lambda a, b: a*b,least_possible_cubes.values())
    return res

f = open('2023-python/day2.txt','r')
input_text = f.read()

print(part_1(input_text))
print(part_2(input_text))