from pprint import pprint

lines = [[[tuple(int(v) for v in l.split(','))] for l in l[1:]] for l in
         [l.strip().split('\n') for l in open("input2").read().split('\n\n')]]


def distance(p1, p2):
    return sum([(p1[i] - p2[i]) ** 2 for i in range(3)]) ** (1 / 2)


for scanner in lines:
    for beacon1 in scanner:
        beacon1.append({distance(beacon1[0], beacon2[0]) for beacon2 in scanner})


def inverse(m):
    det = determinant(m[0], m[1], m[2])
    return (
        (
            ((m[1][1] * m[2][2]) - (m[1][2] * m[2][1])) // det,
            (-((m[0][1] * m[2][2]) - (m[0][2] * m[2][1]))) // det,
            ((m[0][1] * m[1][2]) - (m[0][2] * m[1][1])) // det,
        ),
        (
            (-((m[1][0] * m[2][2]) - (m[1][2] * m[2][0]))) // det,
            ((m[0][0] * m[2][2]) - (m[0][2] * m[2][0])) // det,
            (-((m[0][0] * m[1][2]) - (m[0][2] * m[1][0]))) // det,
        ),
        (
            ((m[1][0] * m[2][1]) - (m[1][1] * m[2][0])) // det,
            (-((m[0][0] * m[2][1]) - (m[0][1] * m[2][0]))) // det,
            ((m[0][0] * m[1][1]) - (m[0][1] * m[1][0])) // det,
        )
    )


def add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def minus(a):
    return (-a[0], -a[1], -a[2])


def determinant(x, y, z):
    det = 0
    det1 = x[0] * (y[1] * z[2] - y[2] * z[1])
    det2 = x[1] * (y[2] * z[0] - y[0] * z[2])
    det3 = x[2] * (y[0] * z[1] - y[1] * z[0])
    for i in range(3):
        det += x[i] * (y[(i + 1) % 3] * z[(i + 2) % 3] - y[(i + 2) % 3] * z[(i + 1) % 3])
    return det


# rotations = ((1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1))
# orientations = []
# for x in rotations:
#     for y in rotations:
#         for z in rotations:
#             if determinant(x,y,z) == 1:
#                 orientations.append((x,y,z))
# pprint(orientations)


orientations = [
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


def apply_orientation(point, orientation):
    return (
        point[0] * orientation[0][0] + point[1] * orientation[0][1] + point[2] * orientation[0][2],
        point[0] * orientation[1][0] + point[1] * orientation[1][1] + point[2] * orientation[1][2],
        point[0] * orientation[2][0] + point[1] * orientation[2][1] + point[2] * orientation[2][2])


beaconmap = {}
for i in range(len(lines)):
    for j in range(i + 1, len(lines)):
        for beacon1 in lines[i]:
            for beacon2 in lines[j]:
                if len(beacon1[1] & beacon2[1]) >= 12:
                    beaconmap.setdefault((i, j), set()).add((beacon1[0], beacon2[0]))

transforms = {}
for scanner_pair, paired_points in beaconmap.items():
    for orientation in orientations:
        distance_set = set()
        for paired_point in paired_points:
            distance_set.add(
                distance(paired_point[0], apply_orientation(paired_point[1], orientation)))
        if len(distance_set) == 1:
            A, B = list(paired_points)[-1][0], apply_orientation(list(paired_points)[-1][1],
                                                                 orientation)
            transforms[scanner_pair] = [(add(A, minus(B)), orientation)]
            break


def get_complete_scanner_count(scanner_info):
    count = 0
    for pair in scanner_info:
        if pair[0] == 0:
            count += 1
    return count


complete_scanner_count = get_complete_scanner_count(transforms)
while complete_scanner_count < len(lines) - 1:
    complete_scanner_count = get_complete_scanner_count(transforms)
    for m in range(len(lines)):
        for i in range(len(lines)):
            for j in range(len(lines)):
                if m == i or i == j or m == j:
                    continue
                if (m, i) in transforms and (i, j) in transforms and not (m, j) in transforms:
                    first_pair = transforms[(m, i)]
                    second_pair = transforms[(i, j)]
                    transforms[(m, j)] = [*second_pair, *first_pair]
                if (m, i) in transforms and (j, i) in transforms and not (m, j) in transforms:
                    first_pair = transforms[(m, i)]
                    inv_second_pair = transforms[(j, i)]
                    second_pair = []
                    for pair_info in reversed(inv_second_pair):
                        inv = inverse(pair_info[1])
                        second_pair.append((apply_orientation(minus(pair_info[0]), inv), inv))
                    second_pair.extend(first_pair)
                    transforms[(m, j)] = [*second_pair]


points, positions = {p[0] for p in lines[0]}, []
pprint(lines[0])
# print(points)
for i in range(1, len(lines)):
    for p in lines[i]:
        testpoint = (0, 0, 0)
        point = p[0]
        for trans in transforms[(0, i)]:
            testpoint = add(trans[0], apply_orientation(testpoint, trans[1]))
            point = add(trans[0], apply_orientation(point, trans[1]))
        points.add(point)
    positions.append(testpoint)

# pprint(points)
# pprint(positions)

print(len(points), max([sum(map(abs, add(i, minus(j)))) for i in positions for j in positions]))
