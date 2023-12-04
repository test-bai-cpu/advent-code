import numpy as np
import heapq
import statistics


def save_input():
    with open("input2") as f:
        input_string = f.read()
    lines = input_string.strip().splitlines()
    return lines


def part1(input_data):
    total = 0
    for line in input_data:
        syntax_list = list(line)
        list_1 = []
        for syntax in syntax_list:
            if syntax in ['(', '[', '{', '<']:
                list_1.append(syntax)
            else:
                if (list_1[-1], syntax) in [('(', ')'), ('[', ']'), ('{', '}'), ('<', '>')]:
                    list_1.pop()
                else:
                    if syntax == ')':
                        total += 3
                    elif syntax == ']':
                        total += 57
                    elif syntax == '}':
                        total += 1197
                    else:
                        total += 25137
                    break
    return total



def get_mul_num(list_1):
    #print(list_1)
    num = 0
    for part in list_1:
        num = num * 5
        if part == '{':
            num += 3
        elif part == '(':
            num += 1
        elif part == '[':
            num += 2
        elif part == '<':
            num += 4
    #print(num)

    return num


def part2(input_data):
    num_list = []
    for line in input_data:
        syntax_list = list(line)
        list_1 = []
        if_corrupted = False
        for syntax in syntax_list:
            if syntax in ['(', '[', '{', '<']:
                list_1.append(syntax)
            else:
                if (list_1[-1], syntax) in [('(', ')'), ('[', ']'), ('{', '}'), ('<', '>')]:
                    list_1.pop()
                else:
                    if_corrupted = True
                    break
        if not if_corrupted:
            list_1.reverse()
            num_list.append(get_mul_num(list_1))

    return statistics.median(num_list)


def main():
    input_data = save_input()
    print(part2(input_data))
    # print(part2(input_data))
    # ans = part1(input_data), part2(input_data)
    # print("part1: ", ans[0], " part2: ", ans[1])


if __name__ == "__main__":
    main()
