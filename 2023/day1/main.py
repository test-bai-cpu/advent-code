import re

def save_input():
    with open("input") as f:
        input_str = f.read()
    data = input_str.strip().splitlines()
    return data


def part1(data):
    sum = 0
    for row in data:
        digits = [char for char in row if char.isdigit()]
        sum += int(digits[0] + digits[-1])
    return sum


def get_first_digit(row, words_to_digits):
    pattern = re.compile('|'.join(words_to_digits.keys()) + r'|\d')
    nums = pattern.findall(row)
    digits = [words_to_digits.get(word, word) for word in nums]
    
    return digits[0]
        
def part2(data):
    words_to_digits = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4',
        'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }
    reversed_words_to_digits = {key[::-1]: value for key, value in words_to_digits.items()}

    sum = 0
    for row in data:
        first_digit = get_first_digit(row, words_to_digits)
        last_digit = get_first_digit(row[::-1], reversed_words_to_digits)
        sum += int(first_digit + last_digit)
        
    return sum

input_data = save_input()
print("part1: ", part1(input_data))
print("part2: ", part2(input_data))