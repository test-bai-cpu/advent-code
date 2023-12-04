import numpy as np
import heapq
import statistics
from copy import deepcopy
from pprint import pprint


def save_input():
    with open("input") as f:
        input_string = f.read()
    parts = input_string.strip().split("\n\n")
    lines = parts[0].splitlines()
    matrix = []
    for line in lines:
        matrix.append(list(map(int, line.split(","))))
    folds = parts[1].splitlines()
    fold_list = []
    for fold in folds:
        content = fold.split("=")
        fold_list.append([content[0][-1], int(content[1])])

    return matrix, fold_list


def fold_with_x(result, fold):
    new_result = set()
    return_result = []
    for point in result:
        x = point[0]
        y = point[1]
        if x > fold:
            x = 2*fold - x
        new_result.add((x, y))

    for res in new_result:
        return_result.append(list(res))
    return return_result

def fold_with_y(result, fold):
    new_result = set()
    return_result = []
    for point in result:
        x = point[0]
        y = point[1]
        if y > fold:
            y = 2*fold - y
        new_result.add((x, y))

    for res in new_result:
        return_result.append(list(res))
    return return_result


def part2(matrix, fold_list):
    result = matrix
    for fold in fold_list:
        if fold[0] == 'x':
            result = fold_with_x(result, fold[1])
        elif fold[0] == 'y':
            result = fold_with_y(result, fold[1])
    print(result)
    print(parse(result))
    return len(result)


def part1(matrix, fold_list):
    result = matrix
    for fold in fold_list:
        if fold[0] == 'x':
            result = fold_with_x(result, fold[1])
        elif fold[0] == 'y':
            result = fold_with_y(result, fold[1])
        break
    print(result)
    return len(result)


def parse(result):
    new = []
    for i in result:
        new.append((i[0], i[1]))
    return new


def main():
    matrix, fold_list = save_input()
    print(part2(matrix, fold_list))
    #visit = {"a": 0, "b": 1, "c": 1}
    #print(check_visit(visit, "a"))
    # print(part2(input_data))
    # ans = part1(input_data), part2(input_data)
    # print("part1: ", ans[0], " part2: ", ans[1])


if __name__ == "__main__":
    main()
