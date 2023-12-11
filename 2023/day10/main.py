from pprint import pprint
import numpy as np

def save_input():
    with open("input") as f:
    # with open("sampleinput") as f:
        input_str = f.read()
    data = input_str.strip().splitlines()
    return data

def part1(data):
    maze = [list(row) for row in data]
    
    for row in maze:
        row.insert(0, ".")
        row.append(".")
    
    maze.insert(0, ["." for i in range(len(maze[0]))])
    maze.append(["." for i in range(len(maze[0]))])

    step_maze = [[-1 for i in range(len(maze[0]))] for j in range(len(maze))]
    
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "S":
                step_maze[i][j] = 0
            if maze[i][j] == ".":
                step_maze[i][j] = -2
    same_ite_cnt = 0
    last_num = None
    while True:
        for i in range(1, len(maze)-1):
            for j in range(1, len(maze[i])-1):
                new_steps_positive = []
                if maze[i][j] == "|":
                    new_steps = [step_maze[i-1][j], step_maze[i+1][j]]
                    new_steps_positive = [step for step in new_steps if step >= 0]

                if maze[i][j] == "-":
                    new_steps = [step_maze[i][j-1], step_maze[i][j+1]]
                    new_steps_positive = [step for step in new_steps if step >= 0]

                if maze[i][j] == "L":
                    new_steps = [step_maze[i][j+1], step_maze[i-1][j]]
                    new_steps_positive = [step for step in new_steps if step >= 0]

                if maze[i][j] == "J":
                    new_steps = [step_maze[i][j-1], step_maze[i-1][j]]
                    new_steps_positive = [step for step in new_steps if step >= 0]

                if maze[i][j] == "7":
                    new_steps = [step_maze[i][j-1], step_maze[i+1][j]]
                    new_steps_positive = [step for step in new_steps if step >= 0]

                if maze[i][j] == "F":
                    new_steps = [step_maze[i][j+1], step_maze[i+1][j]]
                    new_steps_positive = [step for step in new_steps if step >= 0]

                if new_steps_positive:
                    new_step = min(new_steps_positive)
                    step_maze[i][j] = new_step + 1
        
        count_neg_ones = sum(sublist.count(-1) for sublist in step_maze)
        print(count_neg_ones)
        if count_neg_ones == last_num:
            same_ite_cnt += 1
        last_num = count_neg_ones
        
        if same_ite_cnt == 2:
            break
        
        if all(number != -1 for row in step_maze for number in row):
            break
    
    largest_number = max(number for row in step_maze for number in row)    

    with open('output.txt', 'w') as file:
        for row in step_maze:
            line = ' '.join(map(str, row))
            file.write(line + '\n')
    
    return largest_number

def write_to_file(step_maze, file_name):
    with open(file_name, 'w') as file:
        for row in step_maze:
            line = ' '.join(map(str, row))
            file.write(line + '\n')
            
def part2(data):
    maze = [list(row) for row in data]
    
    for row in maze:
        row.insert(0, ".")
        row.append(".")
    
    maze.insert(0, ["." for i in range(len(maze[0]))])
    maze.append(["." for i in range(len(maze[0]))])

    step_maze = [[-1 for i in range(len(maze[0]))] for j in range(len(maze))]
    
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == "S":
                start_pos = (i, j)
    
    four_dirs = [(-1,0), (1,0), (0,-1), (0,1)]
    four_letters = ["|7F", "|JL", "-LF", "-J7"]
    
    let_dir = {
        "|": [0, 1],
        "-": [2, 3],
        "L": [3, 0],
        "J": [2, 0],
        "7": [2, 1],
        "F": [3, 1],
    }
    
    ends = []
    for dir_ind in range(4):
        direction = four_dirs[dir_ind]
        current_pos = (start_pos[0] + direction[0], start_pos[1] + direction[1])
        current_letter = maze[current_pos[0]][current_pos[1]]
        if current_letter in four_letters[dir_ind]:
            ends.append((current_pos, current_letter, dir_ind))
    
    start_pos, start_letter, input_dir = ends[0]
    end_pos, end_letter,output_dir = ends[1]
    
    cnt = 0
    while True:
        step_maze[start_pos[0]][start_pos[1]] = 0
        current_letter = maze[start_pos[0]][start_pos[1]]
        if input_dir == 0: input_dir = 1
        elif input_dir == 1: input_dir = 0
        elif input_dir == 2: input_dir = 3
        elif input_dir == 3: input_dir = 2
        indices = let_dir[current_letter].copy()

        indices.remove(input_dir)

        dir_ind = indices[0]
        direction = four_dirs[dir_ind]
        current_pos = (start_pos[0] + direction[0], start_pos[1] + direction[1])

        start_pos = current_pos
        input_dir = dir_ind
        cnt += 1
        if current_pos == end_pos:
            break
    
    write_to_file(step_maze, "output.txt")
    
    with open("output.txt") as f:
        input_str = f.read()
    data = input_str.strip().splitlines()
    step_maze = [[int(number) for number in row.split()] for row in data]
            
            
    cnt = 0
    step_maze = np.array(step_maze)
    rows, cols = step_maze.shape
    for i in range(1, rows-1):
        cross = 0
        for j in range(1, cols-1):
            if step_maze[i, j] == 0:
                if maze[i][j] in "|F7" or maze[i][j] == "S":
                    cross += 1
            else:
                if cross % 2 == 1:
                    cnt += 1
    return cnt


input_data = save_input()
# print("part1: ", part1(input_data))
print("part2: ", part2(input_data))