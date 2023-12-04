from collections import deque


def part1():
    cnt = 0
    with open("input") as f:
        last_num = int(f.readline())
        while True:
            try:
                num = int(f.readline())
                if num > last_num:
                    cnt += 1
                last_num = num
            except ValueError:
                break

    return cnt


def part2():
    cnt = 0
    last_sum = -1
    with open("input") as f:
        # set a fix length container, FIFO
        window_nums = deque([int(f.readline()), int(f.readline())], maxlen=3)
        while True:
            try:
                window_nums.append(int(f.readline()))
                this_sum = sum(window_nums)
                if this_sum > last_sum:
                    cnt += 1
                last_sum = this_sum
            except ValueError:
                break

    return cnt - 1


ans = part1(), part2()
print("part1: ", ans[0], " part2: ", ans[1])
