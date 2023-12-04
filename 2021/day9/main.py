import numpy as np
import heapq

def save_input():
    with open("input2") as f:
        input_string = f.read()
    lines = input_string.strip().splitlines()
    return lines


def part1(input_data):
    help_row = ['a'*len(input_data[0])]
    help_matrix = help_row + input_data + help_row
    res = []
    for i in range(len(help_matrix)):
        help_matrix[i] = 'a' + help_matrix[i] + 'a'
    for i in range(1, len(input_data) + 1):
        for j in range(1, len(input_data[0]) + 1):
            b = help_matrix[i][j - 1]
            d = help_matrix[i - 1][j]
            c = help_matrix[i + 1][j]
            a = help_matrix[i][j + 1]
            raw_nums = [a, b, c, d]
            nums = []
            for raw_num in raw_nums:
                if not raw_num == 'a':
                    nums.append(int(raw_num))
            if help_matrix[i][j] != 'a' and int(help_matrix[i][j]) < min(nums):
                res.append(int(help_matrix[i][j]) + 1)

    return sum(res)


def get_adjent_nums(point, help_matrix, nums_set, nums_list):
    i = point[0]
    j = point[1]

    a = help_matrix[i][j+1]
    if a not in ['a', '9']:
        before_set_length = len(nums_set)
        nums_set.add((i, j+1))
        after_set_length = len(nums_set)
        if after_set_length > before_set_length:
            nums_list.append((i, j+1))
    b = help_matrix[i][j-1]
    if b not in ['a', '9']:
        before_set_length = len(nums_set)
        nums_set.add((i, j-1))
        after_set_length = len(nums_set)
        if after_set_length > before_set_length:
            nums_list.append((i, j-1))
    c = help_matrix[i+1][j]
    if c not in ['a', '9']:
        before_set_length = len(nums_set)
        nums_set.add((i+1, j))
        after_set_length = len(nums_set)
        if after_set_length > before_set_length:
            nums_list.append((i+1, j))
    d = help_matrix[i-1][j]
    if d not in ['a', '9']:
        before_set_length = len(nums_set)
        nums_set.add((i-1, j))
        after_set_length = len(nums_set)
        if after_set_length > before_set_length:
            nums_list.append((i-1, j))

    return nums_list, nums_set


def find_basin_size(i, j, help_matrix):
    nums_set = {(i, j)}
    nums_list = [(i, j)]
    if_change = 0
    while nums_list:
        point = nums_list.pop()
        before_set_length = len(nums_set)
        nums_list, nums_set = get_adjent_nums(point, help_matrix, nums_set, nums_list)
        after_set_length = len(nums_set)
        if after_set_length == before_set_length:
            if_change += 1
        if if_change > 200:
            break
    return len(nums_set)


def part2(input_data):
    help_row = ['a'*len(input_data[0])]
    help_matrix = help_row + input_data + help_row
    size = []
    for i in range(len(help_matrix)):
        help_matrix[i] = 'a' + help_matrix[i] + 'a'
    for i in range(1, len(input_data) + 1):
        for j in range(1, len(input_data[0]) + 1):
            b = help_matrix[i][j - 1]
            d = help_matrix[i - 1][j]
            c = help_matrix[i + 1][j]
            a = help_matrix[i][j + 1]
            raw_nums = [a, b, c, d]
            nums = []
            for raw_num in raw_nums:
                if not raw_num == 'a':
                    nums.append(int(raw_num))
            if help_matrix[i][j] != 'a' and int(help_matrix[i][j]) < min(nums):
                size.append(find_basin_size(i, j, help_matrix))
    res = heapq.nlargest(3, size)
    mul = 1
    for num in res:
        mul *= num
    return mul










def main():
    input_data = save_input()
    print(part2(input_data))
    # print(part2(input_data))
    # ans = part1(input_data), part2(input_data)
    # print("part1: ", ans[0], " part2: ", ans[1])


if __name__ == "__main__":
    main()
