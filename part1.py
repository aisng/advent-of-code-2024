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

sample_input3 = """..........
.S------7.
.|F----7|.
.||....||.
.||....||.
.|L-7F-J|.
.|..||..|.
.L--JL--J.
.........."""

sample_input4 = """.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ..."""

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


def flood(row: int, col: int, matrix: Matrix) -> None:
    bound_chars = "|-LJ7FS"

    if row not in range(len(matrix)) or col not in range(len(matrix[0])):
        return

    if matrix[row][col] in bound_chars:
        return

    if matrix[row][col] == "X":
        return

    matrix[row][col] = "X"

    flood(row + 1, col, matrix)
    flood(row - 1, col, matrix)
    flood(row, col + 1, matrix)
    flood(row, col - 1, matrix)


bound_chars = "|-LJ7FS"


def main() -> None:
    matrix = convert_data_to_matrix(data=sample_input4)
    curr_row, curr_col = get_starting_pos(matrix)

    # flood(0, 0, matrix)
    if any([item < 0 for item in (curr_col, curr_row)]):
        raise Exception("aaa")

    distance = 0
    backwards_dir = None

    # p2
    loop_coords = {(curr_row, curr_col)}
    counter = 0
    cross_count = 0

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

        loop_coords.add((curr_row, curr_col))

        distance += 1

        if matrix[curr_row][curr_col] == "S":
            break

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == ".":

                row_to_check = matrix[row][col:]
                for row_item in range(col, len(matrix[row])):

                    if matrix[row][row_item] == ".":
                        continue

                    curr_char = matrix[row][row_item]

                    if curr_char in bound_chars and (row, row_item) in loop_coords:
                        cross_count += 1

            if cross_count % 2 != 0:
                counter += 1
                cross_count = 0

    print(distance)
    print(len(loop_coords))
    print(counter)
    # pprint(matrix)


if __name__ == "__main__":
    main()
