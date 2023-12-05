from pprint import pprint
import sys

def save_input():
    with open("input") as f:
    # with open("sampleinput") as f:
        input_str = f.read()
    data = input_str.strip().splitlines()
    return data

def check_match_and_convert(source, map):
    destination = None
    for row in map:
        if row[1] <= source and source < row[1] + row[2]:
            destination = row[0] + source - row[1]
            break
    if not destination:
        destination = source
        
    return destination

def part1(data):
    seeds = [int(s) for s in data[0].split(":")[1].strip().split(" ")]
    maps = {}
    current_map = None

    for line in data:
        if 'map:' in line:
            current_map = line[:-1]
            maps[current_map] = []
        elif line and current_map:
            numbers = [int(n) for n in line.split()]
            maps[current_map].append(numbers)
    
    order = ["seed-to-soil map", "soil-to-fertilizer map", "fertilizer-to-water map", "water-to-light map", "light-to-temperature map", "temperature-to-humidity map", "humidity-to-location map"]
    locations = []
    for seed in seeds:
        source = seed
        for key in order:
            destination = check_match_and_convert(source, maps[key])
            source = destination
            
        locations.append(destination)
        
    return min(locations)
    

def get_intersection(pair1, pair2):
    max_start = max(pair1[0], pair2[0])
    min_end = min(pair1[0] + pair1[1], pair2[0] + pair2[1])

    if max_start < min_end:
        intersection_pair = [max_start, min_end - max_start]

        remain_pairs = []
        if pair1[0] < max_start:
            remain_pairs.append([pair1[0], max_start - pair1[0]])
        if pair1[0] + pair1[1] > min_end:
            remain_pairs.append([min_end, pair1[0] + pair1[1] - min_end])
    else:
        intersection_pair = None
        remain_pairs = None

    return intersection_pair, remain_pairs


def part2(data):
    maps = {}
    current_map = None

    for line in data:
        if 'map:' in line:
            current_map = line[:-1]
            maps[current_map] = []
        elif line and current_map:
            numbers = [int(n) for n in line.split()]
            maps[current_map].append(numbers)
    
    order = ["seed-to-soil map", "soil-to-fertilizer map", "fertilizer-to-water map", "water-to-light map", "light-to-temperature map", "temperature-to-humidity map", "humidity-to-location map"]
    min_location = []
    
    seed_ranges = [int(s) for s in data[0].split(":")[1].strip().split(" ")]
    pairs = [seed_ranges[i:i+2] for i in range(0, len(seed_ranges), 2)]
    
    for origin_pair in pairs:
        source_pairs = [origin_pair]
        for key in order:
            destination_intersections = []
            
            for source_pair in source_pairs:
                remain_pairs = [source_pair]
                for row in maps[key]:
                    row_new_remain_pairs = []
                    for pair in remain_pairs:
                        intersection_pair, new_remain_pairs = get_intersection(pair, [row[1], row[2]])
                        if intersection_pair:
                            destination_intersec = [intersection_pair[0] + row[0] - row[1], intersection_pair[1]]
                            destination_intersections.append(destination_intersec)
                            row_new_remain_pairs += new_remain_pairs
                        else:
                            row_new_remain_pairs.append(pair)
            
                    remain_pairs = row_new_remain_pairs
                    if len(destination_intersections) > 0 and row_new_remain_pairs == []:
                        break
                    
                if remain_pairs:
                    destination_intersections += remain_pairs

            source_pairs = destination_intersections

        min_location.append(min(destination_intersections, key=lambda x: x[0]))
    
    min_min_location = min(min_location, key=lambda x: x[0])        
    return min_min_location[0]
            


input_data = save_input()
print("part1: ", part1(input_data))
print("part2: ", part2(input_data))