from pprint import pprint

def save_input():
    with open("input") as f:
    # with open("sampleinput") as f:
        input_str = f.read()
    data = input_str.strip().splitlines()
    return data

def list_to_dict(map_list):
    result = {}
    for item in map_list:
        key, value = item.split('=')
        value = tuple(val.strip() for val in value.strip()[1:-1].split(','))
        result[key.strip()] = value
    return result

def part1(data):
    instructions = data[0]
    camel_map = list_to_dict(data[2:])
    current_pos = 'AAA'
    steps = 0
    
    while True:
        for instruction in instructions:
            if instruction == 'L':
                next_pos = camel_map[current_pos][0]
            elif instruction == 'R':
                next_pos = camel_map[current_pos][1]

            steps += 1
            if next_pos == 'ZZZ':
                return steps
            current_pos = next_pos
        
def get_starting_pos(camel_map):
    result = []
    for key, value in camel_map.items():
        if key[2] == 'A':
            result.append(key)
    return result

def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

def lcm(x, y):
    return x * y // gcd(x, y)

def lcm_multiple(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = lcm(result, num)
    return result

def get_steps_to_zz(camel_map, instructions, current_pos):
    steps = 0
    
    while True:
        for instruction in instructions:
            if instruction == 'L':
                next_pos = camel_map[current_pos][0]
            elif instruction == 'R':
                next_pos = camel_map[current_pos][1]

            steps += 1
            if next_pos.endswith('Z'):
                return steps
            current_pos = next_pos


def part2(data):
    instructions = data[0]
    camel_map = list_to_dict(data[2:])
    current_pos_list = get_starting_pos(camel_map)
    steps = []
    for current_pos in current_pos_list:
        steps.append(get_steps_to_zz(camel_map, instructions, current_pos))
    all_steps = lcm_multiple(steps)
    
    return all_steps

input_data = save_input()
print("part1: ", part1(input_data))
print("part2: ", part2(input_data))

