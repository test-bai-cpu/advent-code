import math


def save_input():
    with open("input") as f:
        input_string = f.read()
    numbers = list(input_string)
    bin_list = []
    for number in numbers:
        res = bin(int(number, 16))[2:]
        if len(res) < 4:
            res = '0'*(4-len(res)) + res
        bin_list.extend(res)
    return bin_list


def parse_limit_length_digit_of_packages(version_sum, input_data):
    if input_data == '0'*len(input_data):
        print("now finish")
        return version_sum

    version = int("".join(input_data[:3]), 2)
    version_sum += version
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
                    continue_index = i+1
                    break
        literal_value = int("".join(labels), 2)
    else:
        indicator = input_data[6]
        if indicator == '0':
            sub_package_digit_length = int("".join(input_data[7:22]), 2)
            sub_package_total = input_data[22:(22+sub_package_digit_length)]
            version_sum = parse_limit_length_digit_of_packages(version_sum, sub_package_total)
            continue_index = 22+sub_package_digit_length

        elif indicator == '1':
            sub_package_numbers = int("".join(input_data[7:18]), 2)
            version_sum, continue_sub_index = parse_limit_number_of_packages(
                version_sum, sub_package_numbers, input_data[18:]
            )
            continue_index = continue_sub_index + 18
        else:
            raise ValueError

    if continue_index <= len(input_data) - 2:
        version_sum = parse_limit_length_digit_of_packages(version_sum, input_data[continue_index:])

    return version_sum


def parse_one_package_with_longer_digits(version_sum, input_data):
    if input_data == '0'*len(input_data):
        print("now finish")
        return version_sum, None

    version = int("".join(input_data[:3]), 2)
    version_sum += version
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
                    continue_index = i+1
                    break
        literal_value = int("".join(labels), 2)
    else:
        indicator = input_data[6]
        if indicator == '0':
            sub_package_digit_length = int("".join(input_data[7:22]), 2)
            sub_package_total = input_data[22:(22+sub_package_digit_length)]
            version_sum = parse_limit_length_digit_of_packages(version_sum, sub_package_total)
            continue_index = 22+sub_package_digit_length

        elif indicator == '1':
            sub_package_numbers = int("".join(input_data[7:18]), 2)
            version_sum, continue_sub_index = parse_limit_number_of_packages(
                version_sum, sub_package_numbers, input_data[18:]
            )
            continue_index = continue_sub_index + 18
        else:
            raise ValueError

    return version_sum, continue_index


def parse_limit_number_of_packages(version_sum, sub_package_numbers, input_data):
    continue_index = 0
    for i in range(sub_package_numbers):
        tmp_index = continue_index
        version_sum, continue_index = parse_one_package_with_longer_digits(
            version_sum, input_data[continue_index:]
        )
        continue_index = tmp_index + continue_index

    return version_sum, continue_index


def part1(input_data):
    print(input_data)
    literal_package = []
    operator_package = []
    version_sum = int("".join(input_data[:3]), 2)
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
        literal_value = int("".join(labels), 2)
    else:
        indicator = input_data[6]
        if indicator == '0':
            sub_package_digit_length = int("".join(input_data[7:22]), 2)
            sub_package_total = input_data[22:(22+sub_package_digit_length)]
            version_sum = parse_limit_length_digit_of_packages(version_sum, sub_package_total)
        elif indicator == '1':
            sub_package_numbers = int("".join(input_data[7:18]), 2)
            version_sum, continue_index = parse_limit_number_of_packages(
                version_sum, sub_package_numbers, input_data[18:]
            )
        else:
            raise ValueError
        return version_sum


def main():
    data_input = save_input()
    ans = part1(data_input)
    print(ans)


if __name__ == "__main__":
    main()
