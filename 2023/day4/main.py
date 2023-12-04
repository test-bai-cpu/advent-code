from pprint import pprint


def save_input():
    with open("input") as f:
    # with open("sampleinput") as f:
        input_str = f.read()
    data = input_str.strip().splitlines()
    return data


def get_win_nums(row):
    win_part, my_part = row.split('|')
    win_nums = [int(num) for num in win_part.split() if num.isdigit()]
    my_nums = [int(num) for num in my_part.split() if num.isdigit()]
    win_cnt = 0
    for num in my_nums:
        if num in win_nums:
            win_cnt += 1
            
    return win_cnt


def part1(data):
    sum = 0
    for row in data:
        win_cnt = get_win_nums(row)
        if win_cnt > 0:
            sum += 2 ** (win_cnt - 1)

    return sum


def part2(data):
    win_list = [0 for _ in range(len(data))]
    
    for i, row in enumerate(data):
        card_num = i + 1
        card_copy_num = win_list[i]
        win_cnt = get_win_nums(row)
        copy_cards = [i+card_num for i in range(1, win_cnt + 1)]
        for copy_card in copy_cards:
            win_list[copy_card - 1] += (card_copy_num+1)
    
    return sum(win_list) + len(data)
        

input_data = save_input()
print("part1: ", part1(input_data))
print("part2: ", part2(input_data))