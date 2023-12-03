from pprint import pprint


def save_input():
    with open("input") as f:
        input_str = f.read()
    data = input_str.strip().splitlines()
    return data

def check_if_grab_sets_possible(grab_sets, red=None, green=None, blue=None):
    for grab_set in grab_sets:
        pairs = grab_set.split(',')
        color_dict = {}
        for pair in pairs:
            count, color = pair.strip().split(' ')
            color_dict[color] = int(count)
        for color, count in color_dict.items():
            variable_value = locals()[color]
            if variable_value and variable_value < count:
                return False
            
    return True
            

def part1(data):
    sum = 0
    for game in data:
        game_index = game.split(":")[0].split(" ")[1]
        grab_sets = game.split(":")[1].split(";")
        if check_if_grab_sets_possible(grab_sets, red=12,green=13,blue=14):
            sum += int(game_index)
            
    return sum

def get_power_of_game(grab_sets):
    minimum_required = {"red": 0, "green": 0, "blue": 0}
    
    for grab_set in grab_sets:
        pairs = grab_set.split(',')
        color_dict = {}
        for pair in pairs:
            count, color = pair.strip().split(' ')
            color_dict[color] = int(count)
        for color, count in color_dict.items():
            color_mini = minimum_required[color]
            if color_mini < count:
                minimum_required[color] = count

    power_of_game = minimum_required["red"] * minimum_required["green"] * minimum_required["blue"] 
    return power_of_game

def part2(data):
    sum = 0
    for game in data:
        grab_sets = game.split(":")[1].split(";")
        sum += get_power_of_game(grab_sets)
            
    return sum    


input_data = save_input()
print("part1: ", part1(input_data))
print("part2: ", part2(input_data))