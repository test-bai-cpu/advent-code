import math


def save_input():
    with open("input") as f:
        input_string = f.read()
    lines = input_string.splitlines()
    matrix = []
    for line in lines:
        matrix.append(list(map(int, list(line))))

    return matrix


def part1(grid):
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


def solution(size_matrix, grid):
    s = 0
    dist = [math.inf for x in range(size_matrix)]
    dist[s] = 0
    min_point = s
    T = set()
    try:
        while (len(T) < size_matrix):
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

    return dist[-1]


def get_min_point(grid, min_point_index):
    rows, cols = len(grid), len(grid[0])
    row = min_point_index // cols
    col = min_point_index % cols
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

    return solution(rows*cols, extend_matrix)


def main():
    data_input = save_input()
    ans = part2(data_input)
    print(ans)


if __name__ == "__main__":
    main()
