from pprint import pprint
from copy import deepcopy

def save_input():
    with open("input", "r") as f:
        input_string = f.read()
    input_list = [list(line) for line in input_string.splitlines()]
    return input_list


def print_map(input_map):
    string_map = ["".join(line) for line in input_map]
    pprint("\n".join(string_map))


def solution(region_map):
    rows, columns = len(region_map), len(region_map[0])
    # new_map_1 = [[0] * columns for _ in range(rows)]
    step_num = 0
    operation = True
    # print_map(region_map)
    while operation:
        operation = False
        new_map_1 = deepcopy(region_map)
        for i in range(rows):
            for j in range(columns):
                try:
                    if region_map[i][j] == ">" and region_map[i][j + 1] == ".":
                        new_map_1[i][j] = "."
                        new_map_1[i][j + 1] = ">"
                        operation = True
                except IndexError:
                    if region_map[i][j] == ">" and region_map[i][0] == ".":
                        new_map_1[i][j] = "."
                        new_map_1[i][0] = ">"
                        operation = True
        new_map_2 = deepcopy(new_map_1)
        for i in range(rows):
            for j in range(columns):
                try:
                    if new_map_1[i][j] == "v" and new_map_1[i + 1][j] == ".":
                        new_map_2[i][j] = "."
                        new_map_2[i + 1][j] = "v"
                        operation = True
                except IndexError:
                    if new_map_1[i][j] == "v" and new_map_1[0][j] == ".":
                        new_map_2[i][j] = "."
                        new_map_2[0][j] = "v"
                        operation = True
        region_map = deepcopy(new_map_2)
        step_num += 1
        # print("€€€###")
        # print(step_num)
        # print_map(new_map_2)
        # print("€€€###")
        # if step_num > 59:
        #     break

    return step_num


def main():
    res = solution(save_input())
    print(res)


if __name__ == "__main__":
    main()
