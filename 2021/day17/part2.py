def save_input():
    with open("input2") as f:
        input_string = f.read()
    numbers = list(input_string)
    bin_list = []
    for number in numbers:
        res = bin(int(number, 16))[2:]
        if len(res) < 4:
            res = '0'*(4-len(res)) + res
        bin_list.extend(res)
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


def parse_limit_length_digit_of_packages(value_list, input_data):
    if input_data == '0'*len(input_data):
        print("now finish")
        return value_list

    type_id = int("".join(input_data[3:6]), 2)
    print("type id In this level of fix length package: ", type_id)
    if type_id == 4:
        labels = []
        label_list = []
        for i in range(6, len(input_data)):
            label_list.append(input_data[i])
            if len(label_list) == 5:
                first_digit = label_list[0]
                label = "".join(label_list[1:])
                labels.append(label)
                label_list = []
                if first_digit == '0':
                    continue_index = i+1
                    break
        value_list.append(int("".join(labels), 2))
    else:
        indicator = input_data[6]
        if indicator == '0':
            sub_package_digit_length = int("".join(input_data[7:22]), 2)
            print("Again, 0", sub_package_digit_length)
            sub_package_total = input_data[22:(22+sub_package_digit_length)]
            value_list = parse_limit_length_digit_of_packages(value_list, sub_package_total)
            continue_index = 22 + sub_package_digit_length

        elif indicator == '1':
            sub_package_numbers = int("".join(input_data[7:18]), 2)
            print("Again, 1", sub_package_numbers)
            new_value_list = []
            new_value_list, continue_sub_index = parse_limit_number_of_packages(
                new_value_list, sub_package_numbers, input_data[18:]
            )
            new_value = sub_package_operation(type_id, new_value_list)
            print(input_data[18:continue_sub_index])
            value_list.append(new_value)
            continue_index = continue_sub_index + 18
        else:
            raise ValueError

    print("next wave. continue_index ", continue_index)
    if continue_index <= len(input_data) - 2:
        value_list = parse_limit_length_digit_of_packages(value_list, input_data[continue_index:])

    return value_list


def parse_one_package_with_longer_digits(value_list, input_data):
    if input_data == '0'*len(input_data):
        print("now finish")
        return value_list, None

    new_value_list = []
    type_id = int("".join(input_data[3:6]), 2)
    print("type id in one package: ", type_id)
    if type_id == 4:
        labels = []
        label_list = []
        for i in range(6, len(input_data)):
            label_list.append(input_data[i])
            if len(label_list) == 5:
                first_digit = label_list[0]
                label = "".join(label_list[1:])
                labels.append(label)
                label_list = []
                if first_digit == '0':
                    print("checkcheck", i + 1)
                    continue_index = i+1
                    break
        new_value_list.append(int("".join(labels), 2))
    else:
        indicator = input_data[6]
        if indicator == '0':
            sub_package_digit_length = int("".join(input_data[7:22]), 2)
            print("Againnnn 0", sub_package_digit_length)
            sub_package_total = input_data[22:(22+sub_package_digit_length)]
            new_value_list = parse_limit_length_digit_of_packages(new_value_list, sub_package_total)
            continue_index = 22+sub_package_digit_length
            print(continue_index)

        elif indicator == '1':
            sub_package_numbers = int("".join(input_data[7:18]), 2)
            print("Againnnn 1", sub_package_numbers)
            new_value_list, continue_sub_index = parse_limit_number_of_packages(
                new_value_list, sub_package_numbers, input_data[18:]
            )
            continue_index = continue_sub_index + 18
        else:
            raise ValueError

    value = sub_package_operation(type_id, new_value_list)
    value_list.append(value)
    return value_list, continue_index


def parse_limit_number_of_packages(value_list, sub_package_numbers, input_data):
    continue_index = 0
    for i in range(sub_package_numbers):
        tmp_index = continue_index
        print("continue_index here", continue_index)
        value_list, continue_index = parse_one_package_with_longer_digits(
            value_list, input_data[continue_index:]
        )
        continue_index = tmp_index + continue_index
        print("In subpackage ", i + 1, " the data is: ", input_data[tmp_index:continue_index], "the value list is: ", value_list)

    return value_list, continue_index


def part1(input_data):
    value_list = []
    type_id = int("".join(input_data[3:6]), 2)
    if type_id == 4:
        labels = []
        label_list = []
        for i in range(6, len(input_data)):
            label_list.append(input_data[i])
            if len(label_list) == 5:
                first_digit = label_list[0]
                label = "".join(label_list[1:])
                labels.append(label)
                label_list = []
                if first_digit == '0':
                    break
        value_list.append(int("".join(labels), 2))
    else:
        indicator = input_data[6]
        if indicator == '0':
            print("here0")
            sub_package_digit_length = int("".join(input_data[7:22]), 2)
            sub_package_total = input_data[22:(22+sub_package_digit_length)]
            print(sub_package_digit_length)
            value_list = parse_limit_length_digit_of_packages(value_list, sub_package_total)
            print(value_list)
        elif indicator == '1':
            print("here1")
            sub_package_numbers = int("".join(input_data[7:18]), 2)
            value_list, continue_index = parse_limit_number_of_packages(
                value_list, sub_package_numbers, input_data[18:]
            )
        else:
            raise ValueError

    value = sub_package_operation(type_id, value_list)
    print("final:", type_id, value_list)
    return value


def main():
    data_input = save_input()
    ans = part1(data_input)
    print(ans)


if __name__ == "__main__":
    main()
