import math
import numpy as np


def save_input():
    with open("input", "r") as f:
        input_string = f.read()
    raw_scanners = input_string.split('\n\n')
    scanners = []
    for raw_scanner in raw_scanners:
        scanners.append([list(map(int, item.split(","))) for item in raw_scanner.strip().split("\n")[1:]])
    return scanners


def get_distance_of_points(point1, point2):
    return math.sqrt(pow(point1[0] - point2[0], 2) + pow(point1[1] - point2[1], 2) + pow(point1[2] - point2[2], 2))


def get_scanner_distance(scanners):
    scanners_distance = []
    for scanner in scanners:
        scanner_distance = []
        for i in range(len(scanner)):
            distance_list = []
            for j in range(len(scanner)):
                distance_list.append(get_distance_of_points(scanner[i], scanner[j]))
            scanner_distance.append(distance_list)
        scanners_distance.append(scanner_distance)

    return scanners_distance


def get_same_beacon_in_scanners(scanners, scanners_distance):
    same_beacon_in_scanners = {}
    for i in range(len(scanners_distance)):
        for j in range(i + 1, len(scanners_distance)):
            for point1_index, distance1 in enumerate(scanners_distance[i]):
                for point2_index, distance2 in enumerate(scanners_distance[j]):
                    if len(set(distance1) & set(distance2)) >= 12:
                        try:
                            same_beacon_in_scanners[(i,j)].append((scanners[i][point1_index], scanners[j][point2_index]))
                        except KeyError:
                            same_beacon_in_scanners[(i,j)] = [(scanners[i][point1_index], scanners[j][point2_index])]
    return same_beacon_in_scanners


def get_orientations():
    return [
                [(1, 0, 0), (0, 1, 0), (0, 0, 1)],
                [(1, 0, 0), (0, -1, 0), (0, 0, -1)],
                [(-1, 0, 0), (0, 1, 0), (0, 0, -1)],
                [(-1, 0, 0), (0, -1, 0), (0, 0, 1)],
                [(1, 0, 0), (0, 0, 1), (0, -1, 0)],
                [(1, 0, 0), (0, 0, -1), (0, 1, 0)],
                [(-1, 0, 0), (0, 0, -1), (0, -1, 0)],
                [(-1, 0, 0), (0, 0, 1), (0, 1, 0)],
                [(0, 1, 0), (0, 0, 1), (1, 0, 0)],
                [(0, -1, 0), (0, 0, -1), (1, 0, 0)],
                [(0, 1, 0), (0, 0, -1), (-1, 0, 0)],
                [(0, -1, 0), (0, 0, 1), (-1, 0, 0)],
                [(0, -1, 0), (-1, 0, 0), (0, 0, -1)],
                [(0, 1, 0), (1, 0, 0), (0, 0, -1)],
                [(0, 1, 0), (-1, 0, 0), (0, 0, 1)],
                [(0, -1, 0), (1, 0, 0), (0, 0, 1)],
                [(0, 0, -1), (0, -1, 0), (-1, 0, 0)],
                [(0, 0, 1), (0, -1, 0), (1, 0, 0)],
                [(0, 0, 1), (0, 1, 0), (-1, 0, 0)],
                [(0, 0, -1), (0, 1, 0), (1, 0, 0)],
                [(0, 0, 1), (1, 0, 0), (0, 1, 0)],
                [(0, 0, 1), (-1, 0, 0), (0, -1, 0)],
                [(0, 0, -1), (1, 0, 0), (0, -1, 0)],
                [(0, 0, -1), (-1, 0, 0), (0, 1, 0)]
]


def transform(point, orientation):
    return (point[0] * orientation[0][0] + point[1] * orientation[0][1] + point[2] * orientation[0][2],
            point[0] * orientation[1][0] + point[1] * orientation[1][1] + point[2] * orientation[1][2],
            point[0] * orientation[2][0] + point[1] * orientation[2][1] + point[2] * orientation[2][2])


def check_if_orientation_match(paired_points, orientation):
    distance = None
    for paired_point in paired_points:
        distance_same_ori = get_distance_of_points(paired_point[0], transform(paired_point[1], orientation))
        if not distance:
            distance = distance_same_ori
            continue
        if distance != distance_same_ori:
            return False

    return True


def get_relative_position(point1, point2):
    return [point1[0] - point2[0], point1[1] - point2[1], point1[2] - point2[2]]


def get_manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1]) + abs(point1[2] - point2[2])


def add_points(point1, point2):
    return [point1[0] + point2[0], point1[1] + point2[1], point1[2] + point2[2]]


def add_tuple_points(point1, point2):
    return (point1[0] + point2[0], point1[1] + point2[1], point1[2] + point2[2])


def get_complete_scanner_count(scanner_info):
    count = 0
    for pair in scanner_info:
        if pair[0] == 0:
            count += 1
    return count


def get_inverse_matrix(orientation):
    orientation = np.matrix(orientation)
    inverse_matrix = np.linalg.inv(orientation)
    inverse_orientation = []
    for line in inverse_matrix:
        line = line.tolist()[0]
        inverse_orientation.append((int(line[0]), int(line[1]), int(line[2])))
    return inverse_orientation


def modify_scanner_info(scanner_nums, scanner_info):
    complete_scanner_count = get_complete_scanner_count(scanner_info)
    while complete_scanner_count < scanner_nums - 1:
        complete_scanner_count = get_complete_scanner_count(scanner_info)
        for i in range(scanner_nums):
            for j in range(scanner_nums):
                for k in range(scanner_nums):
                    if i == j or j == k or i == k:
                        continue
                    if (i, j) in scanner_info and (j, k) in scanner_info and not (i, k) in scanner_info:
                        first_pair = scanner_info[(i, j)]
                        second_pair = scanner_info[(j, k)]
                        scanner_info[(i, k)] = [*second_pair, *first_pair]
                    if (i, j) in scanner_info and (k, j) in scanner_info and not (i, k) in scanner_info:
                        first_pair = scanner_info[(i, j)]
                        inv_second_pair = scanner_info[(k, j)]
                        second_pair = []
                        for pair_info in reversed(inv_second_pair):
                            inv = get_inverse_matrix(pair_info["orientation"])
                            second_pair.append(
                                {
                                    "scanner_position": transform(
                                        [-value for value in pair_info["scanner_position"]], inv
                                    ),
                                    "orientation": inv
                                }
                            )
                        second_pair.extend(first_pair)
                        scanner_info[(i, k)] = [*second_pair]

    return scanner_info


def get_scanner_position_to_zero(scanners, scanner_info):
    scanner_position_to_zero = []
    for scanner_num in range(1, len(scanners)):
        position = None
        for scanner_info_pair in scanner_info[(0, scanner_num)]:
            if not position:
                position = scanner_info_pair["scanner_position"]
            else:
                position = add_points(scanner_info_pair["scanner_position"], transform(position, scanner_info_pair["orientation"]))
        scanner_position_to_zero.append(position)

    return scanner_position_to_zero


def solution(scanners):
    scanners_distance = get_scanner_distance(scanners)
    same_beacon_in_scanners = get_same_beacon_in_scanners(scanners, scanners_distance)
    orientations = get_orientations()
    scanner_info = {}
    for scanner_pair in same_beacon_in_scanners:
        for orientation in orientations:
            if check_if_orientation_match(same_beacon_in_scanners[scanner_pair], orientation):
                point1, point2 = list(same_beacon_in_scanners[scanner_pair])[-1][0], transform(list(same_beacon_in_scanners[scanner_pair])[-1][1], orientation)
                scanner_info[scanner_pair] = [{
                    "scanner_position": get_relative_position(point1, point2),
                    "orientation": orientation
                                            }]
                break

    scanner_info = modify_scanner_info(len(scanners), scanner_info)

    beacons = {tuple(point) for point in scanners[0]}
    for scanner_num in range(1, len(scanners)):
        for beacon in scanners[scanner_num]:
            for scanner_info_pair in scanner_info[(0, scanner_num)]:
                beacon = tuple(add_tuple_points(scanner_info_pair["scanner_position"], transform(beacon, scanner_info_pair["orientation"])))
            beacons.add(beacon)

    scanner_position_to_zero = get_scanner_position_to_zero(scanners, scanner_info)
    manhattan_distances = []
    for i in range(len(scanner_position_to_zero) - 1):
        for j in range(i + 1, len(scanner_position_to_zero)):
            manhattan_distances.append(
                get_manhattan_distance(scanner_position_to_zero[i], scanner_position_to_zero[j])
            )
    largest_manhattan_distance = max(manhattan_distances)

    return len(beacons), largest_manhattan_distance


def main():
    ans = solution(save_input())
    print(ans)


if __name__ == "__main__":
    main()
