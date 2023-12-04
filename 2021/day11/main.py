import numpy as np
import heapq
import statistics


def save_input():
    with open("input2") as f:
        input_string = f.read()
    lines = input_string.strip().splitlines()
    matrix = []
    for line in lines:
        matrix.append(list(map(int, list(line))))

    return matrix


def update_matrix_flash(input_data, flash_point, flash_times):
    while flash_point:
        point = flash_point.pop()
        try:
            i = point[0]-1
            j = point[1]-1
            if i < 0 or j < 0:
                raise IndexError
            # does not change zero
            if input_data[i][j] == 9:
                flash_point.append((i, j))
                input_data[i][j] = 0
                flash_times += 1
            elif input_data[i][j] != 0:
                input_data[i][j] += 1
        except IndexError:
            pass
        try:
            i = point[0]+1
            j = point[1]+1
            if i < 0 or j < 0:
                raise IndexError
            # does not change zero
            if input_data[i][j] == 9:
                flash_point.append((i, j))
                input_data[i][j] = 0
                flash_times += 1
            elif input_data[i][j] != 0:
                input_data[i][j] += 1
        except IndexError:
            pass
        try:
            i = point[0]+1
            j = point[1]-1
            if i < 0 or j < 0:
                raise IndexError
            # does not change zero
            if input_data[i][j] == 9:
                flash_point.append((i, j))
                input_data[i][j] = 0
                flash_times += 1
            elif input_data[i][j] != 0:
                input_data[i][j] += 1
        except IndexError:
            pass
        try:
            i = point[0]-1
            j = point[1]+1
            if i < 0 or j < 0:
                raise IndexError
            # does not change zero
            if input_data[i][j] == 9:
                flash_point.append((i, j))
                input_data[i][j] = 0
                flash_times += 1
            elif input_data[i][j] != 0:
                input_data[i][j] += 1
        except IndexError:
            pass
        try:
            i = point[0]
            j = point[1]-1
            if i < 0 or j < 0:
                raise IndexError
            # does not change zero
            if input_data[i][j] == 9:
                flash_point.append((i, j))
                input_data[i][j] = 0
                flash_times += 1
            elif input_data[i][j] != 0:
                input_data[i][j] += 1
        except IndexError:
            pass
        try:
            i = point[0]
            j = point[1]+1
            if i < 0 or j < 0:
                raise IndexError
            # does not change zero
            if input_data[i][j] == 9:
                flash_point.append((i, j))
                input_data[i][j] = 0
                flash_times += 1
            elif input_data[i][j] != 0:
                input_data[i][j] += 1
        except IndexError:
            pass
        try:
            i = point[0]+1
            j = point[1]
            if i < 0 or j < 0:
                raise IndexError
            # does not change zero
            if input_data[i][j] == 9:
                flash_point.append((i, j))
                input_data[i][j] = 0
                flash_times += 1
            elif input_data[i][j] != 0:
                input_data[i][j] += 1
        except IndexError:
            pass
        try:
            i = point[0]-1
            j = point[1]
            if i < 0 or j < 0:
                raise IndexError
            # does not change zero
            if input_data[i][j] == 9:
                flash_point.append((i, j))
                input_data[i][j] = 0
                flash_times += 1
            elif input_data[i][j] != 0:
                input_data[i][j] += 1
        except IndexError:
            pass

    return input_data, flash_times


def check_if_sync(input_data):
    rows = len(input_data)
    cols = len(input_data[0])
    num = -1
    for j in range(rows):
        for k in range(cols):
            if num < 0:
                num = input_data[j][k]
                continue
            if input_data[j][k] != num:
                return False

    return True


def check_synchronizing(input_data, flash_point):
    while flash_point:
        point = flash_point.pop()
        try:
            i = point[0]-1
            j = point[1]-1
            if i < 0 or j < 0:
                raise IndexError
            # does not change zero
            if input_data[i][j] == 9:
                flash_point.append((i, j))
                input_data[i][j] = 0
            elif input_data[i][j] != 0:
                input_data[i][j] += 1
        except IndexError:
            pass
        try:
            i = point[0]+1
            j = point[1]+1
            if i < 0 or j < 0:
                raise IndexError
            # does not change zero
            if input_data[i][j] == 9:
                flash_point.append((i, j))
                input_data[i][j] = 0
            elif input_data[i][j] != 0:
                input_data[i][j] += 1
        except IndexError:
            pass
        try:
            i = point[0]+1
            j = point[1]-1
            if i < 0 or j < 0:
                raise IndexError
            # does not change zero
            if input_data[i][j] == 9:
                flash_point.append((i, j))
                input_data[i][j] = 0
            elif input_data[i][j] != 0:
                input_data[i][j] += 1
        except IndexError:
            pass
        try:
            i = point[0]-1
            j = point[1]+1
            if i < 0 or j < 0:
                raise IndexError
            # does not change zero
            if input_data[i][j] == 9:
                flash_point.append((i, j))
                input_data[i][j] = 0
            elif input_data[i][j] != 0:
                input_data[i][j] += 1
        except IndexError:
            pass
        try:
            i = point[0]
            j = point[1]-1
            if i < 0 or j < 0:
                raise IndexError
            # does not change zero
            if input_data[i][j] == 9:
                flash_point.append((i, j))
                input_data[i][j] = 0
            elif input_data[i][j] != 0:
                input_data[i][j] += 1
        except IndexError:
            pass
        try:
            i = point[0]
            j = point[1]+1
            if i < 0 or j < 0:
                raise IndexError
            # does not change zero
            if input_data[i][j] == 9:
                flash_point.append((i, j))
                input_data[i][j] = 0
            elif input_data[i][j] != 0:
                input_data[i][j] += 1
        except IndexError:
            pass
        try:
            i = point[0]+1
            j = point[1]
            if i < 0 or j < 0:
                raise IndexError
            # does not change zero
            if input_data[i][j] == 9:
                flash_point.append((i, j))
                input_data[i][j] = 0
            elif input_data[i][j] != 0:
                input_data[i][j] += 1
        except IndexError:
            pass
        try:
            i = point[0]-1
            j = point[1]
            if i < 0 or j < 0:
                raise IndexError
            # does not change zero
            if input_data[i][j] == 9:
                flash_point.append((i, j))
                input_data[i][j] = 0
            elif input_data[i][j] != 0:
                input_data[i][j] += 1
        except IndexError:
            pass

        if check_if_sync(input_data):
            return input_data, True

    return input_data, False


def part1(input_data):
    rows = len(input_data)
    cols = len(input_data[0])
    flash_point = []
    flash_times = 0
    for i in range(100):
        for j in range(rows):
            for k in range(cols):
                if input_data[j][k] == 9:
                    flash_point.append((j, k))
                    input_data[j][k] = 0
                    flash_times += 1
                else:
                    input_data[j][k] += 1
        input_data, flash_times = update_matrix_flash(input_data, flash_point, flash_times)
    return flash_times


def part2(input_data):
    rows = len(input_data)
    cols = len(input_data[0])
    flash_point = []
    flash_times = 0
    for i in range(100000):
        for j in range(rows):
            for k in range(cols):
                if input_data[j][k] == 9:
                    flash_point.append((j, k))
                    input_data[j][k] = 0
                    flash_times += 1
                else:
                    input_data[j][k] += 1
        if check_if_sync(input_data):
            return i+1
        input_data, if_sync = check_synchronizing(input_data, flash_point)
        if if_sync:
            return i+1
    return i+1


def main():
    input_data = save_input()
    print(part2(input_data))
    # print(part2(input_data))
    # ans = part1(input_data), part2(input_data)
    # print("part1: ", ans[0], " part2: ", ans[1])


if __name__ == "__main__":
    main()