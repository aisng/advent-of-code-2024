from typing import List, Iterable

with open("data.txt", "r", encoding="utf-8") as f:
    data_full = [line.strip() for line in f.readlines()]


def get_all_numbers_from_line(line: str) -> Iterable[List[str]]:
    """Collect all digits, including the ones spelled with letters, from a single line of data for part 2"""
    digit_map = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8",
                 "nine": "9"}
    line_digits = []

    for i, _ in enumerate(line):

        for number_name, number_value in digit_map.items():
            line_slice = line[i:i + len(number_name)]
            if line_slice == number_name:
                line_digits.append(number_value)
                break

        if line[i].isdigit():
            line_digits.append(line[i])

    if line_digits:
        yield line_digits


def get_digits_from_line(data: str) -> Iterable[List[str]]:
    """Collect all digits from a single line of data for part 1"""
    for line in data:
        line_digits = []

        for char in line:
            if not char.isdigit():
                continue
            line_digits.append(char)

        if line_digits:
            yield line_digits


def get_calibration_value(data: str) -> int:
    """AOC, day 1, part 1. Calculate the calibration value"""
    result = 0
    for digits_list in get_digits_from_line(data):
        number = digits_list[0] + digits_list[-1]
        result += int(number)
    return result


def get_calibration_value_p2(data: str) -> int:
    """AOC, day 1, part 2. Calculate the calibration value w/ spelled digits"""
    result = 0
    for line in data:
        for digits_list in get_all_numbers_from_line(line):
            number = digits_list[0] + digits_list[-1]
            result += int(number)
    return result


def main() -> None:
    print(get_calibration_value(data_full))
    print(get_calibration_value_p2(data_full))


if __name__ == "__main__":
    # part 1 answer 54605
    # part 2 answer 55429
    main()
