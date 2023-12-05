from pprint import pprint

symbols = "*#+$"
engine_schematics = ("467..114.....*........35..633.......#...617*...........+.58...592...........755....$.*.....664"
                     ".598..")

chunks = len(engine_schematics)
chunk_size = len(engine_schematics) // 10

engine_matrix = [list(engine_schematics[i:i + chunk_size]) for i in range(0, chunks, chunk_size)]
pprint(engine_matrix)

numbers = []

# num_locations = []
# sym_locations = []

# for i in range(len(engine_matrix)):
#     for j in range(len(engine_matrix[i])):
#         current_char = engine_matrix[i][j]
#         if current_char.isnumeric():
#             num_locations.append((i, j))
#         if current_char in symbols:
#             sym_locations.append((i, j))


# print("num locs", num_locations)
# print("sym locs", sym_locations)

adjacent_digits = []
valid_numbers = []
current_num = ""
row_len = len(engine_matrix[0])
col_len = len(engine_matrix)

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
                if nw == ".":
                    for elem in engine_matrix[i-1][j:row_len]:
                        if elem.isdigit():
                            current_num += elem
                    valid_numbers.append(int(current_num))
                current_num = ""

            if ne.isdigit():
                for elem in engine_matrix[i-1][j:row_len]:
                    if elem.isdigit():
                        current_num += elem
                valid_numbers.append(int(current_num))
                current_num = ""

            if e.isdigit():
                for elem in engine_matrix[i][j+1:row_len]:
                    if elem.isdigit():
                        current_num += elem
                valid_numbers.append(int(current_num))
                current_num = ""

            if se.isdigit():
                for elem in engine_matrix[i+1][j+1:row_len]:
                    if elem.isdigit():
                        current_num += elem
                valid_numbers.append(int(current_num))
                current_num = ""

            # if s.isdigit():
            #
            #     for elem in engine_matrix[i+1][j:row_len]:
            #         if elem.isdigit():
            #             current_num += elem
            #     valid_numbers.append(int(current_num))
            #     current_num = ""

            if sw.isdigit():
                # added +1 to range to include the found value
                for elem in engine_matrix[i+1][0:j + 1]:
                    if elem.isdigit():
                        current_num += elem
                valid_numbers.append(int(current_num))
                current_num = ""

            if w.isdigit():
                for elem in engine_matrix[i][0:len(engine_matrix[i]) - j-1]:
                    if elem.isdigit():
                        current_num += elem
                valid_numbers.append(int(current_num))
                current_num = ""

            if nw.isdigit():
                for elem in engine_matrix[i-1][0:j-1 + 1]:
                    if elem.isdigit():
                        current_num += elem
                valid_numbers.append(int(current_num))
                current_num = ""


# print("adj", adjacent_digits)
print("valid", valid_numbers)
