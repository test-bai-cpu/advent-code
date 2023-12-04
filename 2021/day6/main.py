

def save_input2():
    with open("input") as f:
        input_string = f.read()
    numbers = list(map(int, input_string.split(",")))
    fish = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for num in numbers:
        fish[num] += 1
    return fish




def part1():
    input_data = [1]
    for day in range(1,81):
        add_eight_count = 0
        for i in range(len(input_data)):
            internal_timer = input_data[i]
            if internal_timer == 0:
                add_eight_count += 1
                input_data[i] = 6
            else:
                input_data[i] -= 1
        input_data.extend([8]*add_eight_count)
        print(day, len(input_data))

    return len(input_data)


def update_fish(fish):
    fish_0 = fish[0]
    for i in range(8):
        fish[i] = fish[i+1]
    fish[6] += fish_0
    fish[8] = fish_0
    return fish
def main():
    days = 256
    with open("input2") as f:
        input_string = f.read()
    numbers = list(map(int, input_string.split(",")))
    fish = [0] * 9
    for num in numbers:
        fish[num] += 1
    for i in range(days):
        fish = update_fish(fish)

    return sum(fish)


print(main())

def prepare_timer_list():
    timer_list = {}
    for i in range(1, 6):
        num = i
        input_data = [i]
        for day in range(1, 81):
            add_eight_count = 0
            for i in range(len(input_data)):
                internal_timer = input_data[i]
                if internal_timer == 0:
                    add_eight_count += 1
                    input_data[i] = 6
                else:
                    input_data[i] -= 1
            input_data.extend([8] * add_eight_count)

        timer_list[num] =  len(input_data)
    return timer_list


def prepare_timer_list_2():
    pass


def part2(timer, input_data):
    count = 0
    for num in input_data:
        count += timer[num]

    return count


#res1 = count_eight(1,8,0)
#print(res1)

#timer = prepare_timer_list()
#res = part2(timer, save_input2())
#print(res)