import math, json


def save_input():
    with open("input", "r") as f:
        input_string = f.read()
    lines = input_string.splitlines()
    input_data = []
    for line in lines:
        pairs_line = []
        left_bracket = 0
        right_bracket = 0
        for num in line:
            if num == "[":
                left_bracket += 1
            elif num == "]":
                right_bracket += 1
            elif num == ",":
                pass
            else:
                pairs_line.append([left_bracket - right_bracket, int(num)])
        input_data.append(pairs_line)
    return input_data


def save_input2():
    with open("input", "r") as f:
        input_string = f.read()
    lines = input_string.splitlines()
    return lines


def get_depth_list_for_one_line(sum1):
    pairs_line = []
    left_bracket = 0
    right_bracket = 0
    for num in sum1:
        if num == "[":
            left_bracket += 1
        elif num == "]":
            right_bracket += 1
        elif num == ",":
            pass
        else:
            pairs_line.append([left_bracket - right_bracket, int(num)])
    return pairs_line


def reduce_snailfish(input_line):
    while True:
        input_line, explode_res = explode_snailfish(input_line)
        if explode_res:
            continue

        input_line, split_res = split_snailfish(input_line)
        if not (explode_res or split_res):
            break

    return input_line


def explode_snailfish(input_line):
    for i in range(len(input_line)):
        depth, value = input_line[i][0], input_line[i][1]
        if depth > 4:
            if i > 0:
                input_line[i-1][1] += input_line[i][1]
            if i < len(input_line) - 2:
                input_line[i + 2][1] += input_line[i + 1][1]
            input_line[i:i+2] = [[depth - 1, 0]]
            return input_line, True

    return input_line, False


def split_snailfish(input_line):
    for i in range(len(input_line)):
        depth, value = input_line[i][0], input_line[i][1]
        if value >= 10:
            input_line[i:i + 1] = [[depth + 1, math.floor(value / 2)], [depth + 1, math.ceil(value / 2)]]
            return input_line, True

    return input_line, False


def add_snailfish(input_line1, input_line2):
    input_line1.extend(input_line2)
    for num in input_line1:
        num[0] += 1
    return input_line1


def get_magnitude(input_line):
    tmp_list = []
    for item in input_line:
        if not tmp_list:
            tmp_list.append(item)
        else:
            while True:
                if not tmp_list:
                    tmp_list.append(item)
                    break
                check_pair = tmp_list[-1]
                if check_pair[0] == item[0]:
                    mag = 3 * check_pair[1] + 2 * item[1]
                    tmp_list.pop()
                    item = [check_pair[0] - 1, mag]
                else:
                    tmp_list.append(item)
                    break

    return tmp_list[0][1]


def part1(input_data):
    new_line = None
    for line in input_data:
        if not new_line:
            new_line = reduce_snailfish(line)
        else:
            new_line = add_snailfish(new_line, line)
            new_line = reduce_snailfish(new_line)

    magnitude = get_magnitude(new_line)
    return magnitude


def part2(input_data):
    mags = []
    for i in range(len(input_data) - 1):
        for j in range(i + 1, len(input_data)):
            first_line = get_depth_list_for_one_line(input_data[i])
            second_line = get_depth_list_for_one_line(input_data[j])
            mag1 = get_magnitude(reduce_snailfish(add_snailfish(first_line, second_line)))

            first_line = get_depth_list_for_one_line(input_data[j])
            second_line = get_depth_list_for_one_line(input_data[i])
            mag2 = get_magnitude(reduce_snailfish(add_snailfish(first_line, second_line)))
            mags.extend([mag1, mag2])
    print(max(mags))
    return None


def main():
    ans = part1(save_input2())
    print(ans)

    # test1 = "[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]"
    # #test1 = "[[[[4,3],4],4],[7,[[8,4],9]]]"
    # test2 = get_depth_list_for_one_line(test1)
    # test3 = "[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]"
    # #test3 = "[1,1]"
    # test4 = get_depth_list_for_one_line(test3)
    # print(test2)
    # input1 = add_snailfish(test2, test4)
    # print(input1)
    # input1 = reduce_snailfish(input1)
    # print(input1)
    # for i in range(7):
    #     input1, _ = explode_snailfish(input1)
    #     print("explosive:", input1)
    # for i in range(2):
    #     input1, _ = split_snailfish(input1)
    #     print("split:", input1)
    #     input1, _ = explode_snailfish(input1)
    #     print("explosive:", input1)
    # for i in range(2):
    #     input1, _ = split_snailfish(input1)
    #     print("split:", input1)
    #     input1, _ = split_snailfish(input1)
    #     print("split:", input1)
    #     input1, _ = explode_snailfish(input1)
    #     print("explosive:", input1)
    # for i in range(2):
    #     input1, _ = split_snailfish(input1)
    #     print("split:", input1)
    #     input1, _ = explode_snailfish(input1)
    #     print("explosive:", input1)


    #test11 = "[[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]]"
    #test12 = get_depth_list_for_one_line(test11)
    #print("now")
    #print(reduce_snailfish(test12))
    #input3 =
    #print(explode_snailfish(test2))


if __name__ == "__main__":
    main()
