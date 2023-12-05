from pprint import pprint

symbols = "*#+$"
engine_schematics = ("467..114.....*........35..633.......#...617*...........+.58...592...........755....$.*.....664"
                     ".598..")

chunks = len(engine_schematics)
chunk_size = len(engine_schematics) // 10

engine_matrix = [list(engine_schematics[i:i + chunk_size]) for i in range(0, chunks, chunk_size)]
pprint(engine_matrix)

numbers = []
valid_numbers = []

num_locations = []
sym_locations = []

for i in range(len(engine_matrix)):
    for j in range(len(engine_matrix[i])):
        current_char = engine_matrix[i][j]
        if current_char.isnumeric():
            num_locations.append((i, j))
        if current_char in symbols:
            sym_locations.append((i, j))


# print("num locs", num_locations)
# print("sym locs", sym_locations)

adjacent_digits = []
valid_numbers = []
current_num = ""
for i in range(len(engine_matrix)):

    for j in range(len(engine_matrix[i])):
        current_char = engine_matrix[i][j]
        if current_char in symbols:
            symbol_coordinates = (i, j)
            # print("sym coord", symbol_coordinates)
            # directions
            n = engine_matrix[i-1][j]
            ne = engine_matrix[i-1][j+1]
            e = engine_matrix[i][j+1]
            se = engine_matrix[i+1][j+1]
            s = engine_matrix[i+1][j]
            sw = engine_matrix[i+1][j-1]
            w = engine_matrix[i][j-1]
            nw = engine_matrix[i-1][j-1]

            if n.isdigit():
                print("n", n, "coord", (i-1, j))
                adjacent_digits.append((i-1, j))
                for elem in engine_matrix[i-1][j:len(engine_matrix[i-1])]:
                    if elem.isdigit():
                        current_num += elem
                valid_numbers.append(int(current_num))
                current_num = ""

            elif ne.isdigit():
                print("ne", ne, "coord", (i-1, j+1))
                adjacent_digits.append((i-1, j+1))
                for elem in engine_matrix[i-1][j+1:len(engine_matrix[i-1])]:
                    if elem.isdigit():
                        current_num += elem
                valid_numbers.append(int(current_num))
                current_num = ""

            elif e.isdigit():
                print("e", e, "coord", (i, j+1))
                adjacent_digits.append((i, j+1))
                for elem in engine_matrix[i][j+1:len(engine_matrix[i])]:
                    if elem.isdigit():
                        current_num += elem
                valid_numbers.append(int(current_num))
                current_num = ""

            elif se.isdigit():
                print("se", se, "coord", (i+1, j+1))
                adjacent_digits.append((i+1, j+1))
                for elem in engine_matrix[i+1][j+1:len(engine_matrix[i+1])]:
                    if elem.isdigit():
                        current_num += elem
                valid_numbers.append(int(current_num))
                current_num = ""

            elif s.isdigit():
                print("s", s, "coord", (i+1, j))
                adjacent_digits.append((i+1, j))
                for elem in engine_matrix[i+1][j:len(engine_matrix[i+1])]:
                    if elem.isdigit():
                        current_num += elem
                valid_numbers.append(int(current_num))
                current_num = ""

            # TODO: different direction so the slice is also different
            elif sw.isdigit():
                print("sw", sw, "coord", (i+1, j-1))
                adjacent_digits.append((i+1, j-1))
                # added +1 to range to include the found value
                for elem in engine_matrix[i+1][0:len(engine_matrix[i+1]) - j-1 + 1]:
                    if elem.isdigit():
                        current_num += elem
                valid_numbers.append(int(current_num))
                current_num = ""

            elif w.isdigit():
                print("w", w, "coord", (i, j-1))
                adjacent_digits.append((i, j-1))
                for elem in engine_matrix[i][0:len(engine_matrix[i+1]) - j-1]:
                    if elem.isdigit():
                        current_num += elem
                valid_numbers.append(int(current_num))
                current_num = ""

            elif nw.isdigit():
                print("nw", nw, "coord", (i-1, j-1))
                adjacent_digits.append((i-1, j-1))
                for elem in engine_matrix[i-1][0:len(engine_matrix[i+1]) - j-1]:
                    if elem.isdigit():
                        current_num += elem
                valid_numbers.append(int(current_num))
                current_num = ""


print("adj", adjacent_digits)
print("valid", valid_numbers)
