import statistics
from math import floor, ceil
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
    median = statistics.median(input_data)
    cost = calculate_cost_part_1(median, input_data)
    return cost


def part2(input_data):
    mean_value = statistics.mean(input_data)
    cost = None
    print(mean_value - 0.5, mean_value, mean_value + 0.5)
    for i in range(floor(mean_value - 0.5), ceil(mean_value + 0.5)):
        cost_new = calculate_cost_part_2(i, input_data)
        if not cost or cost_new < cost:
            cost = cost_new
            print(i, cost)
    return cost

def part3(input_data):
    mean_floor = floor(statistics.mean(input_data))
    mean_ceil = ceil(statistics.mean(input_data))
    cost_floor = calculate_cost_part_2(mean_floor, input_data)
    cost_ceil = calculate_cost_part_2(mean_ceil, input_data)
    print(mean_floor, cost_floor)
    print(mean_ceil, cost_ceil)
    print('472.437 ', calculate_cost_part_2(472.437, input_data))
    print('472.531 ', calculate_cost_part_2(472.531, input_data))
    print('472.031 ', calculate_cost_part_2(472.031, input_data))
    print('473.031 ', calculate_cost_part_2(473.031, input_data))
    return min(cost_ceil, cost_floor)

def main_time():
    input_data = save_input()
    start_time = time.time()
    for i in range(1000):
        part2(input_data)
    print("--- %s seconds ---" % (time.time() - start_time))
    # print(part2(input_data))
    # ans = part1(input_data), part2(input_data)
    # print("part1: ", ans[0], " part2: ", ans[1])


def main():
    input_data = save_input()
    res = part3(input_data)
    print(res)


if __name__ == "__main__":
    main()
