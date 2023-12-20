from typing import List, Optional, Tuple
from pprint import pprint
from task_input import full_input

sample_data = """.....
.S-7.
.|.|.
.L-J.
....."""

sample_data_2 = """..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""
sample_data_3 = """-L|F7
7S-7|
L|7||
-L-J|
L|-JF"""
sample_data_3_edit = """-L|F7
7F-7|
L|7||
-L-S|
L|-JF"""

sample_input = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
..........."""

# custom data types
Matrix = List[List[str]]

# movement mappings

NORTH = (-1, 0)
SOUTH = (1, 0)
EAST = (0, 1)
WEST = (0, -1)


ACCEPTED_DIRECTIONS = {
    "|": [NORTH, SOUTH],
    "-": [EAST, WEST],
    "L": [SOUTH, WEST],
    "J": [SOUTH, EAST],
    "7": [EAST, NORTH],
    "F": [NORTH, WEST],
    "S": [NORTH, SOUTH, EAST, WEST],
}

GUIDING_DIRECTIONS = {
    "|": [NORTH, SOUTH],
    "-": [EAST, WEST],
    "L": [NORTH, EAST],
    "J": [NORTH, WEST],
    "7": [WEST, SOUTH],
    "F": [SOUTH, EAST],
    "S": [NORTH, SOUTH, EAST, WEST],
}


def convert_data_to_matrix(data: str) -> Matrix:
    """Convert the input string to a matrix."""
    result = []
    for line in data.splitlines():
        result.append(list(line))
    return result


def get_starting_pos(matrix: Matrix) -> Tuple[int, int]:
    start_symbol = "S"
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == start_symbol:
                return row, col
    return -1, -1


def get_direction(curr_row: int,
                  curr_col: int,
                  matrix: Matrix,
                  backwards_dir: Optional[Tuple[int, int]],
                  ) -> Optional[Tuple[int, int]]:

    curr_symbol = matrix[curr_row][curr_col]
    for direction in (NORTH, SOUTH, EAST, WEST):
        step_row, step_col = direction
        next_row, next_col = curr_row + step_row, curr_col + step_col

        if next_row not in range(len(matrix)) or next_col not in range(len(matrix[0])):
            continue

        next_symbol = matrix[next_row][next_col]
        if next_symbol not in ACCEPTED_DIRECTIONS:
            continue

        next_symbol_dirs = ACCEPTED_DIRECTIONS[next_symbol]
        curr_symbol_dirs = GUIDING_DIRECTIONS[curr_symbol]
        if direction in next_symbol_dirs and direction in curr_symbol_dirs and direction != backwards_dir:
            return direction


def main() -> None:
    matrix = convert_data_to_matrix(data=full_input)
    curr_row, curr_col = get_starting_pos(matrix)

    if any([item < 0 for item in (curr_col, curr_row)]):
        raise Exception("aaa")

    distance = 0
    backwards_dir = None

    while True:

        next_dir = get_direction(
            curr_row=curr_row,
            curr_col=curr_col,
            matrix=matrix,
            backwards_dir=backwards_dir,
        )

        if not next_dir:
            raise Exception("aaa")

        row_dir, col_dir = next_dir

        backwards_dir = (-row_dir, -col_dir)
        curr_row += row_dir
        curr_col += col_dir

        distance += 1

        if matrix[curr_row][curr_col] == "S":
            break

    print(distance // 2)


if __name__ == "__main__":
    main()
