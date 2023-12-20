from typing import List
from pprint import pprint
from part1 import convert_data_to_matrix, get_direction, get_starting_pos
from task_input import full_input
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

sample_input3 = """..........
.S------7.
.|F----7|.
.||....||.
.||....||.
.|L-7F-J|.
.|..||..|.
.L--JL--J.
.........."""

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

bound_chars = "|-LJ7FS"
Matrix = List[List[str]]
matrix = convert_data_to_matrix(data=sample_input3)


def flood(row: int, col: int) -> None:
    if row not in range(len(matrix)) or col not in range(len(matrix[0])):
        return

    if matrix[row][col] in bound_chars:
        return

    if matrix[row][col] == "X":
        return

    matrix[row][col] = "X"

    flood(row + 1, col)
    flood(row - 1, col)
    flood(row, col + 1)
    flood(row, col - 1)


def main() -> None:

    pprint(matrix, width=200)
    flood(0, 0)
    pprint(matrix, width=200)

    counter = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == ".":
                counter += 1

    print(counter)

    with open("output.py", "w") as f:
        f.write(f'"""{"".join(y for x in matrix for y in x)}"""')


if __name__ == "__main__":
    main()
