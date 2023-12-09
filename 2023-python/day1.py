def extract_number(raw_text):
    res = list(filter(lambda char: 57 >= ord(char) >= 48, raw_text))
    return int("".join([res[0], res[-1]]))

def transform_spelled_numbers(raw_text):
    valid_digits = ["one","two","three","four","five","six","seven","eight","nine"]
    first_digit, last_digit = None, None
    first_number_index, last_number_index = len(raw_text)+1,-1
    for digit in valid_digits:
        curr_index, curr_rindex = raw_text.find(digit), raw_text.rfind(digit)
        if curr_index < first_number_index and curr_index != -1:
            first_number_index = curr_index
            first_digit = digit
        if curr_rindex > last_number_index:
            last_number_index = curr_rindex
            last_digit = digit
    raw_text = raw_text if first_digit is None else str(valid_digits.index(first_digit) + 1).join(raw_text.split(first_digit[:-1], 1))
    raw_text = raw_text if last_digit is None else str(valid_digits.index(last_digit) + 1).join(raw_text.rsplit(last_digit[:-1], 1))
    return raw_text

def part_1(input):
    sum = 0
    for line in input.split("\n"):
        sum += extract_number(line)
    return sum

def part_2(input):
    sum = 0
    for line in input.split("\n"):
        sum += extract_number(transform_spelled_numbers(line))
    return sum

f = open('2023-python/day1.txt','r')
input_text = f.read()

print(part_1(input_text))
print(part_2(input_text))


