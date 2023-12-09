from pprint import pprint

def save_input():
    with open("input") as f:
    # with open("sampleinput") as f:
        input_str = f.read()
    data = input_str.strip().splitlines()
    return data

def finite_differences(nums):
    return [nums[i] - nums[i - 1] for i in range(1, len(nums))]

def get_prediction(sequence, index):
    differences = [sequence]
    while differences[-1]:
        next_level = finite_differences(differences[-1])
        differences.append(next_level)

    differences[-1].append(0)
    
    if index == 0:
        for i in range(len(differences) - 2, -1, -1):
            differences[i].insert(0, differences[i][index] - differences[i + 1][index])
    elif index == -1:
        for i in range(len(differences) - 2, -1, -1):
            differences[i].append(differences[i][-1] + differences[i + 1][-1])
        
    return differences[0][index]

def part1(data):
    output = []
    for row in data:
        sequence = [int(x) for x in row.split()]
        output.append(get_prediction(sequence, -1))
        
    return sum(output)
    
def part2(data):
    output = []
    for row in data:
        sequence = [int(x) for x in row.split()]
        output.append(get_prediction(sequence, 0))
        
    return sum(output)

input_data = save_input()
print("part1: ", part1(input_data))
print("part2: ", part2(input_data))

