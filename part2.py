from typing import List
from pprint import pprint
from part1 import convert_data_to_matrix, get_direction, get_starting_pos

sample_input = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
..........."""

sample_input2 = """.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ..."""

# direction mappings

NORTH = (-1, 0)
SOUTH = (1, 0)
EAST = (0, 1)
WEST = (0, -1)

# NEIGHBORING_DIRECTIONS = {
#     "|": [NORTH, SOUTH],
#     "-": [EAST, WEST],
#     "L": [NORTH, EAST],
#     "J": [NORTH, WEST],
#     "7": [WEST, SOUTH],
#     "F": [SOUTH, EAST],
#     "S": [NORTH, SOUTH, EAST, WEST],
# }


Matrix = List[List[str]]


def main() -> None:
    matrix = convert_data_to_matrix(data=sample_input)
    curr_row, curr_col = get_starting_pos(matrix)

    if any([item < 0 for item in (curr_col, curr_row)]):
        raise Exception("aaa")

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

        if backwards_dir == NORTH and matrix[curr_row + WEST[0]][curr_col + WEST[1]] not in "S|-FJL":
            matrix[curr_row + WEST[0]][curr_col + WEST[1]] = "X"
        elif backwards_dir == SOUTH and matrix[curr_row + EAST[0]][curr_col + EAST[1]] not in "S|-FJL":
            matrix[curr_row + EAST[0]][curr_col + EAST[1]] = "X"
        elif backwards_dir == WEST and matrix[curr_row + SOUTH[0]][curr_col + SOUTH[1]] not in "S|-FJL":
            matrix[curr_row + SOUTH[0]][curr_col + SOUTH[1]] = "X"
        elif backwards_dir == EAST and matrix[curr_row + NORTH[0]][curr_col + NORTH[1]] not in "S|-FJL":
            matrix[curr_row + NORTH[0]][curr_col + NORTH[1]] = "X"

        curr_row += row_dir
        curr_col += col_dir

        if matrix[curr_row][curr_col] == "S":
            if backwards_dir == NORTH and matrix[curr_row + WEST[0]][curr_col + WEST[1]] not in "S|-FJL":
                matrix[curr_row + WEST[0]][curr_col + WEST[1]] = "X"
            elif backwards_dir == SOUTH and matrix[curr_row + EAST[0]][curr_col + EAST[1]] not in "S|-FJL":
                matrix[curr_row + EAST[0]][curr_col + EAST[1]] = "X"
            elif backwards_dir == WEST and matrix[curr_row + SOUTH[0]][curr_col + SOUTH[1]] not in "S|-FJL":
                matrix[curr_row + SOUTH[0]][curr_col + SOUTH[1]] = "X"
            elif backwards_dir == EAST and matrix[curr_row + NORTH[0]][curr_col + NORTH[1]] not in "S|-FJL":
                matrix[curr_row + NORTH[0]][curr_col + NORTH[1]] = "X"
            break

    pprint(matrix)


if __name__ == "__main__":
    main()
