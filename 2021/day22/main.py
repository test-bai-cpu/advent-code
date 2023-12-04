from pprint import pprint


def save_input():
    with open("input2", "r") as f:
        input_string = f.read()
    reboot_steps = []
    for line in input_string.splitlines():
        content = line.split(" ")
        reboot_step = []
        reboot_step.append(content[0])
        position = []
        raw_string = content[1].split(",")
        for cord in raw_string:
            position.extend(list(map(int, cord.split("=")[1].split(".."))))
        reboot_step.append(position)
        reboot_steps.append(reboot_step)
    return reboot_steps


def get_cube_intersection(cube1, cube2):
    ax1, ax2, ay1, ay2, az1, az2 = tuple(cube1)
    bx1, bx2, by1, by2, bz1, bz2 = tuple(cube2)
    max_x = max(ax1, bx1)
    min_x = min(ax2, bx2)
    max_y = max(ay1, by1)
    min_y = min(ay2, by2)
    max_z = max(az1, bz1)
    min_z = min(az2, bz2)

    if min_x - max_x >= 0 and min_y - max_y >= 0  and min_z - max_z >= 0:
        return max_x, min_x, max_y, min_y, max_z, min_z


def solution(reboot_steps):
    on_cube_nums = 0
    off_areas = []
    for d in reversed(reboot_steps):
        operation, cube = d[0], d[1]
        x1, x2, y1, y2, z1, z2 = tuple(cube)
        if operation == 'on':
            off_cubes = []
            for area in off_areas:
                intersection_area = get_cube_intersection(area, cube)
                if intersection_area:
                    off_cubes.append(('on', intersection_area))
            on_cube_nums += (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1)
            on_cube_nums -= solution(off_cubes)
        off_areas.append(cube)

    return on_cube_nums


def main():
    res = solution(save_input())
    print(res)

if __name__ == "__main__":
    main()
