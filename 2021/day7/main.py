import statistics
from math import floor, ceil
from decimal import *
import time

def save_input():
    with open("input2") as f:
        input_string = f.read()
    numbers = list(map(int, input_string.split(",")))
    return numbers


def calculate_cost_part_2(goal, input_data):
    cost = 0
    for data in input_data:
        distance = abs(goal - data)
        cost += (1 + distance) * distance / 2
    return cost


def calculate_cost_part_1(goal, input_data):
    cost = 0
    for data in input_data:
        distance = abs(goal - data)
        cost += distance
    return cost


def part1(input_data):
    max_value, min_value = max(input_data), min(input_data)
    cost = []
    for goal in range(min_value, max_value + 1):
        cost.append(calculate_cost_part_1(goal, input_data))
    return min(cost)


def part2(input_data):
    max_value, min_value = max(input_data), min(input_data)
    cost = []
    for goal in range(min_value, max_value + 1):
        cost.append(calculate_cost_part_1(goal, input_data))
    return min(cost)


def test(input_data):
    # max_value, min_value = max(input_data), min(input_data)
    mean_1 = floor(statistics.mean(input_data))
    mean_2 = ceil(statistics.mean(input_data))
    cost1 = calculate_cost_part_2(mean_1, input_data)
    cost2 = calculate_cost_part_2(mean_2, input_data)
    return min(cost1, cost2)

def calc(input_data):
    count1, count2 = 0, 0
    for data in input_data:
        if data < 471:
            count1 += 1
        elif data > 473:
            count2 += 1
    print(count1, count2)
    print(len(input_data))
    print(sum(input_data)/len(input_data))
    print('472.437 ', calculate_cost_part_2(472.437, input_data))
    print('472.436 ', calculate_cost_part_2(472.436, input_data))
    print('472.438 ', calculate_cost_part_2(472.438, input_data))
    print('472.434 ', calculate_cost_part_2(472.434, input_data))
    print('472.531 ', calculate_cost_part_2(472.531, input_data))
    print('472.237 ', calculate_cost_part_2(472.237, input_data))
    print('472.637 ', calculate_cost_part_2(472.637, input_data))


def main():
    input_data = save_input()
    print(part1(input_data))
    # print(part2(input_data))
    # ans = part1(input_data), part2(input_data)
    # print("part1: ", ans[0], " part2: ", ans[1])


if __name__ == "__main__":
    input_data = save_input()
    print(calc(input_data))
