
def save_input():
    with open("input2") as f:
        input_str = f.read()

    # same as readlines(), and better, convert
    # 00100
    # 11110
    # 10110
    # 10111
    # 10101
    # 01111
    # 00111
    # 11100
    # 10000
    # 11001
    # 00010
    # 01010
    # to ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
    input_bin_list = input_str.strip().splitlines()
    # convert '10010', a string, to 18, a decimal int
    # x = '10010'
    # int(x, base=2)
    # input_data = [int(x, base=2) for x in input_bin_list]
    return input_bin_list


def count_bit(numbers, digit_index):
    zero_count, one_count = 0, 0
    for number in numbers:
        digit = number[digit_index]
        if digit == '1':
            one_count += 1
        elif digit == '0':
            zero_count += 1
    if zero_count > one_count:
        most_common_bit, least_common_bit = ('0', '1')
    elif one_count > zero_count:
        most_common_bit, least_common_bit = ('1', '0')
    else:  # one_count == zero_count
        most_common_bit, least_common_bit = ('1', '0')

    return most_common_bit, least_common_bit


def count_bit_without_disable(numbers, digit_index, disable_dict, disable_count, life_support_type):
    zero_count, one_count = 0, 0
    for i in range(len(numbers)):
        if not disable_dict[i]:
            digit = numbers[i][digit_index]
            if digit == '1':
                one_count += 1
            elif digit == '0':
                zero_count += 1

    if zero_count > one_count:
        most_common_bit, least_common_bit = ('0', '1')
    elif one_count > zero_count:
        most_common_bit, least_common_bit = ('1', '0')
    else:  # one_count == zero_count
        most_common_bit, least_common_bit = ('1', '0')

    if life_support_type == "oxygen":
        keep_bit = most_common_bit
    else:  # life_support_type == "co2"
        keep_bit = least_common_bit

    for i in range(len(numbers)):
        digit = numbers[i][digit_index]
        if (not disable_dict[i]) and (digit != keep_bit):
            disable_dict[i] = True
            disable_count += 1

    return disable_dict, disable_count


def find_available_num(numbers, disable_dict):
    for i in range(len(numbers)):
        if not disable_dict[i]:
            return int(numbers[i], base=2)


def get_num_of_life_support(input_data, life_support_type):
    disable_dict = {i: False for i in range(len(input_data))}
    disable_count = 0
    length = len(input_data[0])
    for i in range(length):
        disable_dict, disable_count = count_bit_without_disable(
            input_data, i, disable_dict, disable_count, life_support_type
        )
        if disable_count == len(input_data) - 1:
            return find_available_num(input_data, disable_dict)


# O(MN), M is digit nums of each value, N is number of inputs
def part1(input_data):
    length = len(input_data[0])
    gamma_rate, epsilon_rate = "", ""
    for i in range(length):
        most_common_bit, least_common_bit = count_bit(input_data, i)
        gamma_rate += most_common_bit
        epsilon_rate += least_common_bit
    return int(gamma_rate, base=2) * int(epsilon_rate, base=2)


def part2(input_data):
    oxygen = get_num_of_life_support(input_data, "oxygen")
    co2 = get_num_of_life_support(input_data, "co2")
    return oxygen * co2


def main():
    input_data = save_input()
    ans = part1(input_data), part2(input_data)
    print("part1: ", ans[0], " part2: ", ans[1])


if __name__ == "__main__":
    main()
