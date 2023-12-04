import numpy as np


def save_input():
    with open("input") as f:
        data = f.readlines()
    input = []
    for item in data:
        input.append(item.strip())
    return input


def bin_to_dec(list_bin):
    list_bin = [str(num) for num in list_bin]
    num1 = "".join(list_bin)
    dec = int(num1, 2)
    
    return dec


def solution_part1(input):
    digits_num = len(input[0])
    digits = [0] * digits_num
    for b_num in input:
        for i in range(digits_num):
            digits[i] += int(b_num[i])
    print(digits_num, digits, input)
    input_length = len(input)
    gamma = []
    epsilon = []
    for num in digits:
        if num > input_length // 2:
            gamma.append(1)
            epsilon.append(0)
        else:
            gamma.append(0)
            epsilon.append(1)
    print(gamma, epsilon)
    return bin_to_dec(gamma) * bin_to_dec(epsilon)


def get_initial_sum(input):
    digits_num = len(input[0])
    digits = [0] * digits_num
    for b_num in input:
        for i in range(digits_num):
            digits[i] += int(b_num[i])
    return digits  


def get_all_position_info(input):
    digits_num = len(input[0])
    all_position = np.zeros(shape=(digits_num, len(input)))
    digits = [0] * digits_num
    for i in range(len(input)):
        for j in range(digits_num):
            all_position[j][i] = input[i][j]
    return all_position


def get_all_position_info_2(input):
    digits_num = len(input[0])
    all_position = np.zeros(shape=(len(input), digits_num))
    digits = [0] * digits_num
    for i in range(len(input)):
        for j in range(digits_num):
            all_position[i][j] = input[i][j]
    return all_position


def get_count(col_num, num1, num2):
    input_matrix = get_all_position_info_2(save_input())
    col1 = input_matrix[:, col_num]
    col2 = input_matrix[:, col_num + 1]
    count = 0
    for i in range(len(col2)):
        if col1[i] == num1 and col2[i] == num2:
            count += 1
    return count


INPUT_MATRIX = get_all_position_info_2(save_input())


def update_matrix(col_num, current_bool):
    rows, columns = INPUT_MATRIX.shape
    for i in range(rows):
        if INPUT_MATRIX[i][col_num] != current_bool:
            INPUT_MATRIX[i, :] = -1


def get_count_update(col_num, num1, num2):
    col1 = INPUT_MATRIX[:, col_num]
    col2 = INPUT_MATRIX[:, col_num + 1]
    count = 0
    for i in range(len(col2)):
        if col1[i] == num1 and col2[i] == num2:
            count += 1
    return count


def get_only_left_row():
    rows, columns = INPUT_MATRIX.shape

    for i in range(rows):
        if INPUT_MATRIX[i][0] != -1:
            return INPUT_MATRIX[i]


def solution_part2(input):
    initial_sum = get_initial_sum(input)
    current_bool = initial_sum[0] > len(input) // 2
    oxygen_num = []
    co2_num = []
    
    for i in range(len(initial_sum)):
        oxygen_num.append(int(current_bool))

        if i == len(initial_sum) - 1:
            break

        update_matrix(i, current_bool)

        if current_bool:
            sum_1 = get_count_update(i, 1, 1)
            sum_0 = get_count_update(i, 1, 0)
            
        else:
            sum_1 = get_count_update(i, 0, 1)
            sum_0 = get_count_update(i, 0, 0)
        
        if sum_0 + sum_1 == 1:
            left_row = [int(num) for num in get_only_left_row()]
            return left_row
        
        current_bool = sum_1 >= sum_0

    return oxygen_num
 

def solution_part3(input):
    initial_sum = get_initial_sum(input)
    current_bool = initial_sum[0] < len(input) // 2
    co2_num = []
    
    for i in range(len(initial_sum)):
        co2_num.append(int(current_bool))

        if i == len(initial_sum) - 1:
            break

        update_matrix(i, current_bool)

        if current_bool:
            sum_1 = get_count_update(i, 1, 1)
            sum_0 = get_count_update(i, 1, 0)
            
        else:
            sum_1 = get_count_update(i, 0, 1)
            sum_0 = get_count_update(i, 0, 0)
        
        if sum_0 + sum_1 == 1:
            left_row = [int(num) for num in get_only_left_row()]
            return left_row
        current_bool = sum_1 < sum_0

    return co2_num




oxygen_num = solution_part2(save_input())
dec_1 = bin_to_dec(oxygen_num)

print(dec_1)