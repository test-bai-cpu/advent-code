import statistics
from math import floor, ceil
from decimal import *
import time

def save_input():
    with open("input2") as f:
        input_string = f.read()
    lines = input_string.strip().splitlines()

    return lines


def part1(input_data):
    count = 0
    for line in input_data:
        digits = line.split(" | ")[1].split(" ")
        print(digits)
        for digit in digits:
            if len(digit) in [2, 3, 4, 7]:
                print(digit)
                count += 1
    return count

def check_diff(digit1, digit2):
    diff = list(set(digit1).symmetric_difference(set(digit2)))
    return diff

def get_index(decode_list, digit):
    for i in range(len(decode_list)):
        decode = decode_list[i]
        if set(digit) == set(decode):
            return i

def part2(input_data):
    sum_num = 0
    decode_list = ['0']*10
    for line in input_data:
        digits = line.split(" | ")[0].split(" ")
        for digit in digits:
            if len(digit) == 2:
                decode_list[1] = digit
            elif len(digit) == 3:
                decode_list[7] = digit
            elif len(digit) == 4:
                decode_list[4] = digit
            elif len(digit) == 7:
                decode_list[8] = digit
        diff_1_4 = check_diff(decode_list[4], decode_list[1])
        for digit in digits:
            if len(digit) == 6:
                if not (decode_list[1][0] in digit and decode_list[1][1] in digit):
                    decode_list[6] = digit
                else:
                    if diff_1_4[0] in digit and diff_1_4[1] in digit:
                        decode_list[9] = digit
                    else:
                        decode_list[0] = digit
            elif len(digit) == 5:
                if decode_list[1][0] in digit and decode_list[1][1] in digit:
                    decode_list[3] = digit
                else:
                    if diff_1_4[0] in digit and diff_1_4[1] in digit:
                        decode_list[5] = digit
                    else:
                        decode_list[2] = digit
        numbers_to_decode = line.split(" | ")[1].split(" ")
        raw_number = ''
        for number in numbers_to_decode:
            raw_number += str(get_index(decode_list, number))
        sum_num += int(raw_number)
    return sum_num










def main():
    input_data = save_input()
    print(part2(input_data))
    # print(part2(input_data))
    # ans = part1(input_data), part2(input_data)
    # print("part1: ", ans[0], " part2: ", ans[1])


if __name__ == "__main__":
    main()
