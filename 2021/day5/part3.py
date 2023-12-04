import re
from typing import List, Tuple, Union, Any
from pprint import pprint


def load_data(infile_path: str) -> List[List[Union[str, Any]]]:
    data = []
    with open(infile_path, 'r', encoding='ascii') as infile:
        for line in infile:
            split_data = \
                re.match(r'(\w+) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)$',
                         line).groups()
            data.append([split_data[0]] + [int(i) for i in split_data[1:]])
    return data


def overlapping(cube1, cube2):
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


def count_lit_cubes(data):
    lit_count = 0
    counted_zones = []
    for d in reversed(data):
        mode, box = d[0], d[1:]
        x1, x2, y1, y2, z1, z2 = box
        if mode == 'on':
            dead_cubes = []
            for overlap_box in [overlapping(zone, box) for zone in counted_zones]:
                if overlap_box:
                    dead_cubes.append(('on', *overlap_box))
            lit_count += (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1)
            lit_count -= count_lit_cubes(dead_cubes)
        counted_zones.append(box)
    return lit_count


def part_2(infile_path: str) -> int:
    data = load_data(infile_path)
    lit_count = count_lit_cubes(data)
    return lit_count


if __name__ == '__main__':
    part2_answer = part_2("./input")
    print(f'Part 2: {part2_answer}')