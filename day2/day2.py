from functools import reduce

f = open('input.txt','r')
input_text = f.read()

INPUT_TEST = """A Y
B X
C Z"""

get_result = {
    21:'win',
    22:'lose',
    23:'draw',
    24:'win',
    25:'lose'
}

outcome_score = {
    'lose':0,
    'draw':3,
    'win':6
}

end_round = {
    'X':'lose'
    ,'Y':'draw'
    ,'Z':'win'
}

def process_strategy(input):
    return [line.split(" ") for line in input.split('\n')]

def rps_selected_score(rps):
    return ord(rps) - 87

def get_symbol_by_outcome(opponent, outcome):
    res = ord(opponent) + list(get_result.values()).index(outcome) + 21
    return chr(res if 88 <= res <= 90 else res+3)


def calculate_score_p1(opponent, you):
    outcome = get_result[ord(you) - ord(opponent)]
    return outcome_score[outcome] + rps_selected_score(you)

def calculate_score_p2(opponent, you):
    end_round_res = end_round[you]
    return outcome_score[end_round_res] + rps_selected_score(get_symbol_by_outcome(opponent, end_round_res))

def part1(input):
    strategy_raw = process_strategy(input)
    return reduce(lambda x, y: x+y,[calculate_score_p1(i[0],i[1]) for i in strategy_raw])

def part2(input):
    strategy_raw = process_strategy(input)
    return reduce(lambda x, y: x+y,[calculate_score_p2(i[0],i[1]) for i in strategy_raw])

print(part1(input_text))
print(part2(input_text))




