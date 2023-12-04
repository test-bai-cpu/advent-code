import pprint


def save_input():
    with open("input2") as f:
        input_string = f.read()
    numbers = list(input_string)
    bin_list = ""
    for number in numbers:
        res = bin(int(number, 16))[2:]
        if len(res) < 4:
            res = '0'*(4-len(res)) + res
        bin_list += res
    return bin_list


def sub_package_operation(type_id, sub_package_values):
    if type_id == 0:
        return sum(sub_package_values)
    elif type_id == 1:
        prod_value = 1
        for val in sub_package_values:
            prod_value *= val
        return prod_value
    elif type_id == 2:
        return min(sub_package_values)
    elif type_id == 3:
        return max(sub_package_values)
    elif type_id == 4:
        if len(sub_package_values) > 1:
            raise Exception
        return sub_package_values[0]
    elif type_id == 5:
        if len(sub_package_values) != 2:
            raise Exception
        return int(sub_package_values[0] > sub_package_values[1])
    elif type_id == 6:
        if len(sub_package_values) != 2:
            raise Exception
        return int(sub_package_values[0] < sub_package_values[1])
    elif type_id == 7:
        if len(sub_package_values) != 2:
            raise Exception
        return int(sub_package_values[0] == sub_package_values[1])


def solution(input_bin_list, version_sum, position):
    version_sum += int(input_bin_list[position: position + 3], 2)
    position += 3
    type_id= int(input_bin_list[position: position + 3], 2)
    position += 3

    if type_id == 4:
        literal_value_list = []
        while True:
            literal_value_list.append(input_bin_list[position + 1: position + 5])
            position += 5
            if input_bin_list[position - 5] == '0':
                break
        package_value = int(''.join(literal_value_list), 2)
    else:
        sub_package_values = []
        indicator = input_bin_list[position]
        position += 1
        if indicator == '0':
            package_end_position = position + int(input_bin_list[position:position + 15], 2) + 15
            position += 15
            while position < package_end_position:
                version_sum, position, sub_package_value = solution(input_bin_list, version_sum, position)
                sub_package_values.append(sub_package_value)
        elif indicator == "1":
            sub_package_numbers = int(input_bin_list[position:position + 11], 2)
            position += 11
            for _ in range(sub_package_numbers):
                version_sum, position, sub_package_value = solution(input_bin_list, version_sum, position)
                sub_package_values.append(sub_package_value)

        package_value = sub_package_operation(type_id, sub_package_values)

    return version_sum, position, package_value


def main():
    version_sum = 0
    position = 0
    data_input = save_input()
    version_sum, position, value = solution(data_input, version_sum, position)
    print(value)
    print(version_sum)


if __name__ == "__main__":
    main()
