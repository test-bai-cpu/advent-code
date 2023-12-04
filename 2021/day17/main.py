import math


def save_input():
    with open("input2") as f:
        input_string = f.read()
    lines = input_string.splitlines()
    matrix = []
    for line in lines:
        matrix.append(line.split(","))

    return matrix

def part1():
    x = [281, 311]
    y = [-74, -54]
    v_0_x_min = math.ceil(0.5 * (-1 + math.sqrt(1 + 8 * x[0])))
    print("v_0_x_min: ", v_0_x_min)
    initial_vel = []
    for v_0_x in range(v_0_x_min, 400):
        for v_0_y in range(-100, 100):
            for t in range(1, 150):
                if v_0_y > 0 and t < 2 * v_0_y + 2:
                    continue
                if t <= v_0_x:
                    S_x = (2 * v_0_x - t + 1) * 0.5 * t
                else:
                    S_x = (v_0_x+ 1) * v_0_x * 0.5
                S_y = -0.5 * t * t + v_0_y * t + 0.5 * t
                if x[1] >= S_x >= x[0] and y[0] <= S_y <= y[1]:
                    initial_vel.append((v_0_x, v_0_y))
                    print("here", t, v_0_x, v_0_y, v_0_y*(v_0_y+1)*0.5)
                    break
    return len(initial_vel)


def main():
    ans = part1()
    print(ans)


if __name__ == "__main__":
    main()
