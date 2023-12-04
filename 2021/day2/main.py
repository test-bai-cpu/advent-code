def save_input():
    with open("input") as f:
        input_str = f.read()
    data = input_str.strip().splitlines()
    return data


def part1(data):
    hor = 0
    dep = 0
    for move in data:
        directory = move.split(" ")[0]
        dis = int(move.split(" ")[1])
        if directory == "forward":
            hor += dis
        elif directory == "down":
            dep -= dis
        elif directory == "up":
            dep += dis
    
    return abs(hor * dep)


def part2(data):
    hor, dep, aim = 0, 0, 0
    for move in data:
        directory = move.split(" ")[0]
        dis = int(move.split(" ")[1])
        if directory == "forward":
            hor += dis
            dep += dis * aim
        elif directory == "down":
            aim += dis
        elif directory == "up":
            aim -= dis
    
    return abs(hor * dep)


input_data = save_input()
ans = part1(input_data), part2(input_data)
print("part1: ", ans[0], " part2: ", ans[1])
