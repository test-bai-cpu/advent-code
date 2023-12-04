import math
import numpy as np
from pprint import pprint


def image_get(matrix, index_row, index_col, default):
    try:
        return matrix[index_row][index_col]
    except IndexError:
        return default


def save_input():
    with open("input", "r") as f:
        input_string = f.read()
    inputs = input_string.split('\n\n')
    image_enhancement_algorithm = list(inputs[0])
    input_image = []
    for line in inputs[1].splitlines():
        input_image.append(list(line))
    return image_enhancement_algorithm, input_image


def get_bin_value(pixel):
    if pixel == ".":
        return "0"
    else:
        return "1"


def count_light_pixel(input_image):
    count = 0
    for i in range(len(input_image)):
        for j in range(len(input_image[0])):
            if input_image[i][j] == "#":
                count += 1

    return count


def print_image(input_image):
    output_image = ""
    for i in range(len(input_image)):
        output_image += "".join(input_image[i]) + "\n"
    print(output_image)

def part1(image_enhancement_algorithm, input_image):
    for k in range(50):
        if k % 2 == 0:
            default_pixel = "."
            new_image = [["."] * len(input_image[0]) for _ in range(len(input_image))]
        else:
            default_pixel = "#"
            new_image = [["#"] * len(input_image[0]) for _ in range(len(input_image))]
        for i in range(len(input_image)):
            for j in range(len(input_image[0])):
                nine_pixels = [
                    image_get(input_image, i - 1, j - 1, default_pixel),
                    image_get(input_image, i - 1, j, default_pixel),
                    image_get(input_image, i - 1, j + 1, default_pixel),
                    image_get(input_image, i, j - 1, default_pixel),
                    image_get(input_image, i, j, default_pixel),
                    image_get(input_image, i, j + 1, default_pixel),
                    image_get(input_image, i + 1, j - 1, default_pixel),
                    image_get(input_image, i + 1, j, default_pixel),
                    image_get(input_image, i + 1, j + 1, default_pixel),
                ]
                nine_bins = "".join([get_bin_value(pixel_around) for pixel_around in nine_pixels])
                decimal_number = int(nine_bins, 2)
                algo_pixel = image_enhancement_algorithm[decimal_number]
                new_image[i][j] = algo_pixel
        input_image = new_image

    return input_image


def main():
    image_enhancement_algorithm, input_image = save_input()
    ans = part1(image_enhancement_algorithm, input_image)
    # print_image(ans)
    print(count_light_pixel(ans))


if __name__ == "__main__":
    main()
