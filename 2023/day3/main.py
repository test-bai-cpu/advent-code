from pprint import pprint
import re

def save_input():
    with open("input") as f:
        input_str = f.read()
    data = input_str.strip().splitlines()
    return data

def analyze_row(row):
    # print("---- for row: ", row)
    numbers = re.finditer(r'\d+', row)
    number_locations = [(int(num.group()), [num.start(), num.end() - 1]) for num in numbers]
    # print("number: ", number_locations)
    symbols = re.finditer(r'[^0-9\.]', row)
    symbol_locations = [(sym.group(), sym.start()) for sym in symbols]
    # print("symbol: ", symbol_locations)    
    
    return number_locations, symbol_locations

def check_if_adjenct(number_locations, current_symbol, last_symbol=None, next_symbol=None):
    symbol_locations = current_symbol
    if last_symbol:
        symbol_locations = symbol_locations + last_symbol
    if next_symbol:
        symbol_locations = symbol_locations + next_symbol

    sum = 0
    for num_pair in number_locations:
        number = num_pair[0]
        number_location = num_pair[1]
        for sym_pair in symbol_locations:
            symbol_location = sym_pair[1]
            if symbol_location >= number_location[0]-1 and symbol_location <= number_location[1]+1:
                # print(number)
                sum += number
                break
                
    return sum
    

def part1(data):
    sum = 0
    for i, row in enumerate(data):
        if i == 0:
            number_locations, symbol_locations = analyze_row(row)
            next_row_number_locations, next_row_symbol_locations = analyze_row(data[i+1])
            sum += check_if_adjenct(number_locations, symbol_locations, next_symbol=next_row_symbol_locations)
        elif i == len(data) - 1:
            sum += check_if_adjenct(number_locations, symbol_locations, last_symbol=last_row_symbol_locations)
        else:
            next_row_number_locations, next_row_symbol_locations = analyze_row(data[i+1])
            sum += check_if_adjenct(number_locations, symbol_locations, last_symbol=last_row_symbol_locations, next_symbol=next_row_symbol_locations)
        
        last_row_symbol_locations = symbol_locations
        number_locations = next_row_number_locations
        symbol_locations = next_row_symbol_locations

    return sum


def check_if_gear(symbol_locations, current_number, last_number=None, next_number=None):
    number_locations = current_number
    if last_number:
        number_locations = number_locations + last_number
    if next_number:
        number_locations = number_locations + next_number

    sum = 0
    for sym_pair in symbol_locations:
        symbol = sym_pair[0]
        if symbol != "*":
            continue
        symbol_location = sym_pair[1]
        adj_nums = []
        for num_pair in number_locations:
            number = num_pair[0]
            number_location = num_pair[1]
            if symbol_location >= number_location[0]-1 and symbol_location <= number_location[1]+1:
                adj_nums.append(number)
        if len(adj_nums) == 2:
            sum += adj_nums[0] * adj_nums[1]
                
    return sum
    
    
def part2(data):
    sum = 0
    for i, row in enumerate(data):
        if i == 0:
            number_locations, symbol_locations = analyze_row(row)
            next_row_number_locations, next_row_symbol_locations = analyze_row(data[i+1])
            sum += check_if_gear(symbol_locations, number_locations, next_number=next_row_number_locations)
        elif i == len(data) - 1:
            sum += check_if_gear(symbol_locations,number_locations, last_number=last_row_number_locations)
        else:
            next_row_number_locations, next_row_symbol_locations = analyze_row(data[i+1])
            sum += check_if_gear(symbol_locations, number_locations, last_number=last_row_number_locations, next_number=next_row_number_locations)
        
        last_row_number_locations = number_locations
        number_locations = next_row_number_locations
        symbol_locations = next_row_symbol_locations

    return sum
    
    
    
    
    
input_data = save_input()
print("part1: ", part1(input_data))
print("part2: ", part2(input_data))