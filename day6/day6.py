f = open('input.txt','r')
input_text = f.read()

test_text = 'bvwbjplbgvbhsrlpgdmjqwftvncz'

def has_duplicate_char(txt):
    check = []
    for chr in txt:
        if chr not in check:
            check.append(chr)
        else:
            return True
    return False

def count_start_packet(input, gap):
    for index in range(0, len(input) - gap + 1):
        if has_duplicate_char(input[index:index + gap]) == False:
            print(f"{input[index:index + gap]} is not duplicate")
            return index + gap

def part1(input):
    return count_start_packet(input, 4)

def part2(input):
    return count_start_packet(input, 14)

print(part1(input_text))
print(part2(input_text))