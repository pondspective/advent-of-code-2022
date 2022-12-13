f = open('input.txt','r')
input_text = f.read()

test_text = 'bvwbjplbgvbhsrlpgdmjqwftvncz'

def has_duplicate_char(txt):
    check = []
    for chr in txt:
        if chr not in check:
            check.append(chr)
        else:
            print(f"{chr} is duplicate")
            return True
    return False

def part1(input):
    for index in range(0, len(input) - 3):
        if has_duplicate_char(input[index:index+4]) == False:
            print(f"{input[index:index+4]} is not duplicate")
            return index+4

def part2(input):
    for index in range(0, len(input) - 13):
        if has_duplicate_char(input[index:index+14]) == False:
            print(f"{input[index:index+14]} is not duplicate")
            return index+14

print(part1(input_text))
print(part2(input_text))