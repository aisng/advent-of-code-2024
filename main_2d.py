from typing import List, Iterator, Tuple, Callable

with open("data_full.txt", "r", encoding="utf-8") as f:
    data_full = [line.strip() for line in f.readlines()]

Matrix = List[List[str]]


def convert_data_to_matrix(data: str) -> Matrix:
    """Convert the data to two dimensional matrix"""
    data_in_2d = []

    for line in data:
        data_in_2d.append(list(line))

    return data_in_2d


# def
def find_adjacent_values_and_coordinates(data: Matrix, x_coord: int, y_coord: int) -> Iterator[
        Tuple[str, Tuple[int, int]]]:
    """Get all values and their coordinates within a matrix adjacent to coordinates specified"""

    for x in (x_coord - 1, x_coord, x_coord + 1):
        for y in (y_coord - 1, y_coord, y_coord + 1):

            if y not in range(len(data[0])) or x not in range(len(data)):
                continue

            if x == x_coord and y == y_coord:
                continue

            yield data[x][y], (x, y)


def is_symbol(item):
    return not item.isdigit() and item != "."


def is_digit(item):
    return item.isdigit()


def check_adjacent(data: Matrix, x_coord: int, y_coord: int, analyzer: Callable) -> bool:
    """Check if any symbol is adjacent to the current coordinate"""
    for value, _ in find_adjacent_values_and_coordinates(data, x_coord, y_coord):
        if analyzer(value):
            return True
    return False


def get_adjacent_digit_coordinates(data: Matrix, x_coord: int, y_coord: int) -> List[Tuple[int, int]]:
    """Get the coordinates of all adjacent digits"""
    result = []
    for value, coordinates in find_adjacent_values_and_coordinates(data, x_coord, y_coord):
        if value.isdigit():
            result.append(coordinates)
    return result


def numbers_and_coordinates(data: Matrix) -> Iterator[Tuple[int, List]]:
    """Find all the numbers and their coordinates within a matrix"""
    current_num = ""
    digit_coordinates = []
    for x_coord in range(len(data)):
        for y_coord in range(len(data[x_coord])):
            current_char = data[x_coord][y_coord]

            # if digit -> collect data
            if current_char.isdigit():
                current_num += current_char
                digit_coordinates.append((x_coord, y_coord))
                continue

            # not digit -> check if digit was before -> if so return collected data
            if current_num:
                yield int(current_num), digit_coordinates
                digit_coordinates = []
                current_num = ""


def get_gear_coordinates(data: Matrix) -> Iterator[Tuple]:
    """Return coordinates of all the gear symbols within a matrix"""
    gear_symbol = "*"
    for x in range(len(data)):
        for y in range(len(data[x])):
            current_char = data[x][y]
            if current_char == gear_symbol:
                yield x, y


def calculate_part_numbers_sum(data: Matrix) -> int:
    """AOC day 3, part 1. Find numbers that are adjacent to symbols and calculate their sum"""
    result = 0
    for number, coordinates in numbers_and_coordinates(data):
        for x, y in coordinates:
            if check_adjacent(data, x_coord=x, y_coord=y, analyzer=is_symbol):
                result += number
                break
    return result


def calculate_gear_ratios_sum(matrix: Matrix) -> int:
    """AOC day 3, part 2. Find the product of two numbers adjacent to asterisk (*) symbol and
    calculate their sum """

    result = 0
    gear_coordinates = get_gear_coordinates(matrix)

    for x, y in gear_coordinates:
        current_adjacent_numbers = []
        current_gear_ratio = 1

        if not check_adjacent(matrix, x, y, is_digit):
            continue

        adjacent_digits = get_adjacent_digit_coordinates(matrix, x, y)

        for number, num_coordinates in numbers_and_coordinates(matrix):
            for digit_coordinates in adjacent_digits:
                if digit_coordinates in num_coordinates:
                    current_adjacent_numbers.append(number)
                    break

            if len(current_adjacent_numbers) != 2:
                continue

            for num in current_adjacent_numbers:
                current_gear_ratio *= num
            result += current_gear_ratio
            break

    return result


def main():
    matrix = convert_data_to_matrix(data_full)
    print("p1", calculate_part_numbers_sum(matrix))
    print("p2", calculate_gear_ratios_sum(matrix))
    # print("part1", 540212)
    # print("part2", 87605697)


if __name__ == "__main__":
    main()
