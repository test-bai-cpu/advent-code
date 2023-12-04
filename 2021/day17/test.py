
def get_five_x_five_tile_area_for_each_num(num):
    matrix = []
    for i in range(5):
        row = []
        for j in range(5):
            if i == 0 and j == 0:
                row.append(num)
                continue
            if j == 0:
                new_num = matrix[i-1][j]
            else:
                new_num = row[j-1]
            if new_num == 9:
                row.append(1)
                continue
            row.append(new_num + 1)
        matrix.append(row)

    return matrix

import math
import sys

def save_input():
    with open("input2") as f:
        input_string = f.read()
    lines = input_string.splitlines()
    matrix = []
    for line in lines:
        matrix.append(list(map(int, list(line))))

    return matrix


def part1(grid):
    if not grid or not grid[0]:
        return 0

    rows, columns = len(grid), len(grid[0])
    dp = [[0] * columns for _ in range(rows)]
    dp[0][0] = grid[0][0]
    for i in range(1, rows):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
    for j in range(1, columns):
        dp[0][j] = dp[0][j - 1] + grid[0][j]
    for i in range(1, rows):
        for j in range(1, columns):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

    return dp[rows - 1][columns - 1]


def solution(grid):
    if not grid or not grid[0]:
        return 0
    rows, columns = len(grid), len(grid[0])
    dp = [[0] * columns for _ in range(rows)]
    dp[0][0] = 0

    dist = [[math.inf] * columns for _ in range(rows)]
    dist[0][0] = 0

    visit = [[False] * columns for _ in range(rows)]

    for i in range(1, rows):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
    for j in range(1, columns):
        dp[0][j] = dp[0][j - 1] + grid[0][j]

    for m in range(1, rows):
        for k in range(1, columns):
            i1, j1 = (-1, -1)
            min_dist = math.inf
            for i in range(1, rows):
                for j in range(1, columns):
                    if (not visit[i][j]) and dist[i][j] < min_dist:
                        i1, j1 = (i,j)
                        min_dist = dist[i][j]
            if i1 == -1 or j1 == -1:
                return
            visit[i1][j1] = True
            for i in range(1, rows):
                for j in range(1, columns):
                    if visit[i][j] == False:
                        pass



    return dp[rows - 1][columns - 1]


def solution3(name_list, grid, s):
    for i, name in enumerate(name_list):
        if name == s:
            s = i
            break;
    print("name list: ", len(name_list))
    dist = [math.inf for x in range(len(name_list))]  # s到所有点的距离，初始化为最大值
    dist[s] = 0  # s到s的距离为0
    min_point = s  # 距离s最短的点为s
    T = set()  # 存放已经算出最短距离的点，初始化为空
    print("Start iteration")
    # 开始循环
    while (len(T) < len(name_list)):  # 一直循环直至T包含了所有点
        print(len(T))
        T.add(min_point)  # 将距离最短的点加入到T中
        min_point_dict = get_min_point(grid, min_point)
        # print(min_point, min_point_dict)
        for i in min_point_dict:  # 遍历min_point的所有直接相连的点
            w = min_point_dict[i]
            # print("enum", i, w, dist)
            if i not in T and w > 0:  # 只需要更新不属于T的、权值大于0的点
                dist[i] = min(dist[i], dist[min_point] + min_point_dict[i])  # 取最小值
        # 选出不属于T的距离的最小值
        min_dist = math.inf
        for i, d in enumerate(dist):
            if i not in T and d > 0 and d < min_dist:
                min_dist = d
                min_point = i

    print(dist[-1])
    #return dict((name_list[i], d) for i, d in enumerate(dist))  # 将结果集中的点索引换为点名称，放入到词典中
    return dist[-1]


def solution4(name_list, grid, s):
    s = 0
    # len(name_list) = 250000
    dist = [math.inf for x in range(len(name_list))]
    dist[s] = 0
    min_point = s
    T = set()
    try:
        while (len(T) < len(name_list)):
            # print(len(T))
            T.add(min_point)
            min_point_dict = get_min_point(grid, min_point)
            for i in min_point_dict:
                w = min_point_dict[i]
                if i not in T and w > 0:
                    dist[i] = min(dist[i], dist[min_point] + min_point_dict[i])

            min_dist = math.inf
            for i in range(len(dist)):
                d = dist[i]
                if i not in T and d > 0 and d < min_dist:
                    min_dist = d
                    min_point = i
    except KeyboardInterrupt:
        print(len(T))

    print(dist[-1])
    return dist[-1]

def get_min_point(grid, min_point_index):
    rows, cols = len(grid), len(grid[0])
    row = min_point_index // cols
    col = min_point_index % cols
    # min_points = [math.inf] * rows * cols
    min_points = {}
    min_points[row * cols + col] = 0

    try:
        if col == 0:
            raise IndexError
        min_points[row * cols + col - 1] = grid[row][col - 1]
    except IndexError:
        pass
    try:
        min_points[row * cols + col + 1] = grid[row][col + 1]
    except IndexError:
        pass
    try:
        if row == 0:
            raise IndexError
        min_points[(row - 1) * cols + col] = grid[row - 1][col]
    except IndexError:
        pass
    try:
        min_points[(row + 1) * cols + col] = grid[row + 1][col]
    except IndexError:
        pass

    return min_points


def part2(grid):
    single_rows, single_columns = len(grid), len(grid[0])
    # extend_matrix = [[0]*50]*50 not possible, means copy all rows, if change one, change all
    extend_matrix = [[0] * single_columns * 5 for _ in range(single_rows * 5)]
    rows, cols = len(extend_matrix), len(extend_matrix[0])

    for i in range(rows):
        for j in range(cols):
            if i < single_rows and j < single_columns:
                extend_matrix[i][j] = grid[i][j]
                continue
            if i < single_columns:
                new_num = extend_matrix[i][j - single_columns]
            else:
                new_num = extend_matrix[i - single_rows][j]
            if new_num == 9:
                extend_matrix[i][j] = 1
                continue
            extend_matrix[i][j] = new_num + 1


    name_list = []
    for i in range(rows):
        for j in range(cols):
            name_list.append((i, j))
    s = (0, 0)

    print("getting matrix")
    return solution4(name_list, extend_matrix, s)

    #extend_matrix = [[1,2,3],[4,5,6],[7,8,9]]
    #rows, cols = len(extend_matrix), len(extend_matrix[0])
    #
    # print("here1")
    # name_list = []
    # for i in range(rows):
    #     for j in range(cols):
    #         name_list.append((i, j))
    # s = (0, 0)
    # print("here2", rows, cols)
    # MAX = sys.maxsize
    # size_matrix = rows * cols
    # # w = [[0] * size_matrix for _ in range(size_matrix)]
    # w = []
    # for i in range(size_matrix):
    #     row1 = []
    #     for j in range(size_matrix):
    #         if i == j:
    #             row1.append(0)
    #         else:
    #             row1.append(math.inf)
    #     w.append(row1)
    #
    # print(rows, cols, size_matrix)
    # for i in range(rows):
    #     for j in range(cols):
    #         try:
    #             if j == 0:
    #                 raise IndexError
    #             w[i * cols + j][i * cols + j - 1] = extend_matrix[i][j - 1]
    #             w[i * cols + j - 1][i * cols + j] = extend_matrix[i][j]
    #         except IndexError:
    #             pass
    #         try:
    #             w[i * cols + j][i * cols + j + 1] = extend_matrix[i][j + 1]
    #             w[i * cols + j + 1][i * cols + j] = extend_matrix[i][j]
    #         except IndexError:
    #             pass
    #         try:
    #             if i == 0:
    #                 raise IndexError
    #             w[i * cols + j][(i - 1) * cols + j] = extend_matrix[i - 1][j]
    #             w[(i - 1) * cols + j][i * cols + j] = extend_matrix[i][j]
    #         except IndexError:
    #             pass
    #         try:
    #             w[i * cols + j][(i + 1) * cols + j] = extend_matrix[i + 1][j]
    #             w[(i + 1) * cols + j][i * cols + j] = extend_matrix[i][j]
    #         except IndexError:
    #             pass




def part3():
    MAX = sys.maxsize
    W = [[0,9,4,MAX],
         [9,0,3,1],
         [4,3,0,1],
         [MAX,1,1,0]]
    name_list = ['A','B','C','D']
    print(solution3(name_list,W,'A'))

def main():
    data_input = save_input()
    ans = part2(data_input)
    # ans = part3()

if __name__ == "__main__":
    main()
