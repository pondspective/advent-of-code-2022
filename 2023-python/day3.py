def process_engine_schematic(input):
    return [list(line) for line in input.split("\n")]

def is_symbol(char):
    return not (char.isdigit() or char == '.')

def detect_neighbor_around_range(arr, row, col_start, col_end, condition_func):
    neighbor_pos = []
    for y in range(row - 1, row + 2):
        for x in range(col_start - 1, col_end + 2):
            # position not out of range
            if (x < 0) or (y < 0) or (y >= len(arr)) or (x >= len(arr[0])):
                continue
            # not input position
            elif (y == row and col_start <= x <= col_end):
                continue
            else:
                if condition_func(arr[y][x]):
                    print(f"Detect {arr[y][x]} at pos {x, y}")
                    neighbor_pos.append([x, y])
    return neighbor_pos

def has_neighbor_around_range(arr, row, col_start, col_end, condition_func):
    return len(detect_neighbor_around_range(arr, row, col_start, col_end, condition_func)) > 0

def find_char_pos(arr, row, col, direction):
    next_char = arr[row][col]
    is_digit = True
    while is_digit:
        col += direction
        if col < 0 or col >= len(arr[0]):
            break
        next_char = arr[row][col]
        is_digit = next_char.isdigit()
    return col - direction

def find_number_pos_forward(arr, row, col):
    return find_char_pos(arr, row, col, 1)

def find_number_pos_backward(arr, row, col):
    return find_char_pos(arr, row, col, -1)

def part_1(input):
    arr = process_engine_schematic(input)
    res, number, end_col = 0, 0, -1
    for y_pos in range(len(arr)):
        for x_pos in range(len(arr[0])):
            if (end_col != -1) and (x_pos <= end_col):
                if x_pos == end_col: end_col = -1
                continue
            if arr[y_pos][x_pos].isdigit():
                end_col = find_number_pos_forward(arr, y_pos, x_pos)
                number = int("".join(arr[y_pos][x_pos:end_col+1]))
                if has_neighbor_around_range(arr, y_pos, x_pos, end_col, is_symbol):
                    res = res + number
    return res

def part_2(input):
    arr = process_engine_schematic(input)
    res = 0
    for y_pos in range(len(arr)):
        for x_pos in range(len(arr[0])):
            if arr[y_pos][x_pos] != '*': continue
            neighbor_pos = detect_neighbor_around_range(arr, y_pos, x_pos, x_pos,str.isdigit)
            check_num_index = []
            neighbor_product = 1
            for pos in neighbor_pos:
                x, y = pos
                first, last = find_number_pos_backward(arr, y, x), find_number_pos_forward(arr, y, x)
                if [y, first, last] not in check_num_index:
                    number = int("".join(arr[y][first:last+1]))
                    print(number)
                    neighbor_product *= number
                    check_num_index.append([y, first, last])
            res = neighbor_product + res if len(check_num_index) == 2 else res
    return res

f = open('2023-python/day3.txt','r')
input_text = f.read()

print(part_1(input_text))
print(part_2(input_text))

