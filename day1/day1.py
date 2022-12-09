from functools import reduce

INPUT_TEST = '''\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
'''

################## PART1 ##################

f = open('input.txt','r')
input_text = f.read()
# print(input_text)
total_calories = []
sum = 0
for line in input_text.split("\n"):
    if line != '':
        sum = sum + int(line)
    else:
        total_calories.append(sum)
        sum = 0 # reset sum after append

elf_number = total_calories.index(max(total_calories))+1

print(f"Max calories -> {max(total_calories)}")
print(f"Elf that carried most calories -> {elf_number}")


################## PART2 ##################
print(reduce(lambda x, y: x+y,sorted(total_calories, reverse=True)[:3]))