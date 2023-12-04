from pprint import pprint
from dataclasses import dataclass
import numpy as np

@dataclass
class Point:
    value: int
    marked: bool


def save_input():
    with open("input") as f:
        data = f.readlines()
    input = []
    board = []
    drawn_nums = False
    for item in data:
        if not drawn_nums:
            input.append(item.strip())
            drawn_nums = True
            continue
        item = item.strip()
        if item:
            line = item.split(" ")
            new_list = [num for num in line if num != '']
            board.extend(new_list)
        else:
            board = []
            input.append(board)
    return input


def save_input2():
    with open("input") as f:
        data = f.read()
    numbers, raw_boards = data.strip().split("\n", 1)

    # numbers:
    # string: 7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1  with , in between
    # to list of int: [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10, 16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]
    numbers = list(map(int, numbers.split(",")))

    # separate multiple boards, every board is in format of [22, 13, 17, 11, 0, 8, 2, 23, 4, 24, 21, 9, 14, 16, 7, 6, 10, 3, 18, 5, 1, 12, 20, 15, 19]
    # i.e. list of ints
    raw_boards = raw_boards.strip().split("\n\n")
    boards = []
    for raw_board in raw_boards:
        boards.append(
            [int(x) for x in raw_board.replace("\n", " ").split(" ") if x != ""]
        )

    # save one board: [22, 13, 17, 11, 0, 8, 2, 23, 4, 24, 21, 9, 14, 16, 7, 6, 10, 3, 18, 5, 1, 12, 20, 15, 19],
    # to a matrix
    res_boards = []
    for board in boards:
        flag_matrix = np.zeros(shape=(5, 5))
        board = np.array([[element for element in board[i: i+5]] for i in range(0, 25, 5)])
        res_boards.append(board)
    print(res_boards)


res = save_input2()
pprint(res)
