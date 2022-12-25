import parse as p
from functools import reduce

f = open('test_input.txt','r')
input_text = f.read()

# $ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k

EXCLUDE_LIST = []
path = ''

def process_terminal_log(input):
    split_cd =  [line.split('\n') for line in input_text.strip().split('$ cd')]
    print(split_cd, "\n")
    res = {}
    for dir in split_cd:
        if dir not in [[''], [' ..','']]:
            key, value = make_folder(dir)
            res.update({key:value})
    return res

def make_folder(raw_list):
    folder = {'type' : 'folder',
        'size' : 0}
    # outer_folder['name'] = raw_list[0].strip()
    folder.update({'child_items':raw_list[raw_list.index('$ ls')+1:]})
    return raw_list[0].strip() ,folder

def process_file(file):
    parse_file = p.compile('{:d} {}')
    return parse_file.parse(file)

# res['a'] = res['a'].update({'size':100})
# res['a']['size'] = 1000

# for dir in list(process_terminal_log(input_text).keys):
#     print(dir)

res = process_terminal_log(input_text)
print(res)

def calculate_size(dir, start_path = '/'):
    file_size = 0
    for file in dir[start_path]['child_items']:
        print(file)
        if file == '' or file is None:
            pass
        elif file.startswith('dir '):
            dir_name = p.parse('dir {}', file)[0]
            print(dir_name)
            file_size += calculate_size(dir, start_path = dir_name)[0]
            dir[dir_name].update({'size':file_size})
        else:
            size, file_name = process_file(file)
            file_size += size
            print(f"File name -> {file_name} / Size -> {size}")
    # Update outmost size
    dir[start_path].update({'size':file_size})
    return file_size, dir

updated_size = calculate_size(process_terminal_log(input_text))[1]
print(updated_size)
filter_size = list(filter(lambda x: (x <= 100000),[s['size'] for s in list(updated_size.values())]))
print(reduce(lambda x, y: x+y,filter_size))