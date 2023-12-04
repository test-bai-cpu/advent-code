import numpy as np


def save_input_example():
    with open("input2") as f:
        data = f.readlines()
    input = []
    position_matrix = np.zeros(shape=(len(data), 4))

    i = 0
    j = 0

    for item in data:
        cord = []
        for charac in item:
            if charac == "\n":
                i = i + 1
                j = 0
            elif charac not in [",", " ", "-", ">", "\n"]:
                position_matrix[i][j] = charac
                j += 1

    return position_matrix

def save_input3():
    with open("input2") as f:
        data = f.readlines()
    input = []
    position_matrix = np.zeros(shape=(len(data), 4))

    i = 0
    j = 0
    num = []

    put_num = False
    for item in data:
        cord = []
        for charac in item:
            if charac not in [",", " ", "-", ">", "\n"]:
                put_num = True
                num.append(charac)
            if charac in [",", " ", "-", ">", "\n"]:
                if put_num:
                    num = "".join(num)
                    position_matrix[i][j] = int(num)
                    j += 1
                    num = []
                    put_num = False
            if charac == "\n":
                i = i + 1
                j = 0

    num = "".join(num)
    position_matrix[i][j] = int(num)

    return position_matrix


def save_input():
    with open("input") as f:
        input_string = f.read()
    input_list = input_string.strip().splitlines()
    position_matrix = np.zeros(shape=(len(input_list), 4))
    for i in range(len(input_list)):
        point_1, point_2 = input_list[i].split(" -> ")
        coordinate_list = point_1.split(",")
        coordinate_list.extend(point_2.split(","))
        position_matrix[i, :] = [int(i) for i in coordinate_list]

    return position_matrix


def check_input_cord(input_cord):
    map_cord = []
    max1 = np.amax(input_cord, axis=0)
    min1 = np.amin(input_cord, axis=0)
    x_min = min(min1[0], min1[2])
    y_min = min(min1[1], min1[3])
    x_max = max(max1[0], max1[2])
    y_max = max(max1[1], max1[3])
    
    position_matrix = np.zeros(shape=(int(y_max) + 1, int(x_max) + 1))
    for line in input_cord:
        if line[0] == line[2]:
            for j in range(int(min(line[1], line[3])), int(max(line[1], line[3]) + 1)):
                position_matrix[j][int(line[0])] += 1
        elif line[1] == line[3]:
            for j in range(int(min(line[0], line[2])), int(max(line[0], line[2])) + 1):
                position_matrix[int(line[1])][j] += 1
        elif (line[2] - line[0] + line[3] - line[1] == 0) or (line[2] - line[0] == line[3] - line[1]):
            if_add = False
            if line[0] < line[2]:
                if line[1] < line[3]:
                    if_add = True
                j = int(line[1])
            else:
                if line[3] < line[1]:
                    if_add = True
                j = int(line[3])
            for i in range(int(min(line[0], line[2])), int(max(line[0], line[2])) + 1):
                position_matrix[j][i] += 1
                if if_add:
                    j += 1
                else:
                    j -= 1
        else:
            continue
    
    return len(position_matrix[position_matrix>=2])


input_cord = save_input()
print(input_cord)
#output_cord = check_input_cord(input_cord)
#print(output_cord)