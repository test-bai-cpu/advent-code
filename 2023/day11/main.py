from pprint import pprint
import numpy as np

def save_input():
    with open("input") as f:
    # with open("sampleinput") as f:
        input_str = f.read()
    data = input_str.strip().splitlines()
    return data

def check_array(array):
    string_list = [''.join(row) for row in array]
    string_matrix = '\n'.join(string_list)

    print(string_matrix)

def part1(data):
    array = np.array([list(row) for row in data])
    rows, _ = array.shape
    
    i = 0
    while i < rows:
        if np.all(array[i] == "."):
            array = np.insert(array, i+1, array[i], axis=0)
            i += 1
        i += 1
            
    cols, _ = array.shape
    
    i = 0
    while i < cols:
        if np.all(array[:, i] == "."):
            array = np.insert(array, i+1, array[:, i], axis=1)
            i += 1
        i += 1
    
    # check_array(array)
    
    gal_locations = [(i, j) for i in range(len(array)) for j in range(len(array[i])) if array[i][j] == '#']
    
    dist = 0
    for i in range(len(gal_locations)):
        for j in range(i+1, len(gal_locations)):
            location1 = gal_locations[i]
            location2 = gal_locations[j]
            dist += abs(location1[0] - location2[0]) + abs(location1[1] - location2[1])

    return dist
    

def get_location(location, empty_rows, empty_cols, expan_times):
    row, col = location
    
    row += len([i for i in empty_rows if i < row]) * (expan_times - 1)
    col += len([i for i in empty_cols if i < col]) * (expan_times - 1)
    
    return (row, col)
    
            
def part2(data):
    array = np.array([list(row) for row in data])
    rows, cols = array.shape
    empty_rows = []
    for i in range(rows):
        if np.all(array[i] == "."):
            empty_rows.append(i)
            
    empty_cols = []
    for i in range(cols):
        if np.all(array[:, i] == "."):
            empty_cols.append(i)

    gal_locations = [(i, j) for i in range(len(array)) for j in range(len(array[i])) if array[i][j] == '#']

    dist = 0
    for i in range(len(gal_locations)):
        for j in range(i+1, len(gal_locations)):
            location1 = get_location(gal_locations[i], empty_rows, empty_cols, expan_times=1000000)
            location2 = get_location(gal_locations[j], empty_rows, empty_cols, expan_times=1000000)
            dist += abs(location1[0] - location2[0]) + abs(location1[1] - location2[1])

    return dist

input_data = save_input()
print("part1: ", part1(input_data))
print("part2: ", part2(input_data))