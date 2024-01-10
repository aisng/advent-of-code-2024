from typing import List, Optional, Tuple
from task_input import full_input


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


def get_start_pipe(coords: Tuple[int, int],
                   matrix: Matrix
                   ) -> str:

    row, col = coords
    curr_symbol = matrix[row][col]
    directions = []
    result = ""

    for direction in (NORTH, SOUTH, EAST, WEST):
        step_row, step_col = direction
        next_row, next_col = row + step_row, col + step_col

        if next_row not in range(len(matrix)) or next_col not in range(len(matrix[0])):
            continue

        next_symbol = matrix[next_row][next_col]
        if next_symbol not in ACCEPTED_DIRECTIONS:
            continue

        next_symbol_dirs = ACCEPTED_DIRECTIONS[next_symbol]
        curr_symbol_dirs = GUIDING_DIRECTIONS[curr_symbol]
        if direction in next_symbol_dirs and direction in curr_symbol_dirs and direction:
            directions.append(direction)

    for symbol, guiding_dir in GUIDING_DIRECTIONS.items():
        if directions == guiding_dir:
            result = symbol
    return result


bound_chars = "|-LJ7FS"
loop_south_chars = "7F|"


def main() -> None:
    matrix = convert_data_to_matrix(data=full_input)
    start_pos = get_starting_pos(matrix)
    start_pipe = get_start_pipe(coords=start_pos, matrix=matrix)

    curr_row, curr_col = start_pos

    if any([item < 0 for item in (curr_col, curr_row)]):
        raise Exception("out of matrix bounds")

    distance = 0
    backwards_dir = None

    loop_coords = {(curr_row, curr_col)}

    # pt1
    while True:

        next_dir = get_direction(
            curr_row=curr_row,
            curr_col=curr_col,
            matrix=matrix,
            backwards_dir=backwards_dir,
        )

        if not next_dir:
            raise Exception("next dir not found")

        row_dir, col_dir = next_dir

        backwards_dir = (-row_dir, -col_dir)
        curr_row += row_dir
        curr_col += col_dir

        loop_coords.add((curr_row, curr_col))

        distance += 1

        if matrix[curr_row][curr_col] == "S":
            break

    # pt2
    tiles_within_counter = 0

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):

            if (row, col) not in loop_coords:
                cross_counter = 0

                for row_item_idx in range(col, len(matrix[row])):
                    current_char = matrix[row][row_item_idx]

                    if current_char in bound_chars and (row, row_item_idx) in loop_coords:
                        if current_char == "S":
                            current_char = start_pipe

                        if current_char in loop_south_chars:
                            cross_counter += 1

                if cross_counter % 2 != 0:
                    tiles_within_counter += 1

    print("pt1", distance // 2)
    print("pt2", tiles_within_counter)


if __name__ == "__main__":
    # pt1 6856
    # pt2 501
    main()
