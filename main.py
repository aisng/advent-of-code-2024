engine_schematics = ("467..114.....*........35..633.......#...617*...........+.58...592...........755....$.*.....664"
                     ".598..")

symbols = "*#+$"

i = 0
valid_numbers = []
numbers = []
current_num = ""
number_indices = {}



while i < len(engine_schematics):

    if engine_schematics[i].isnumeric():
        current_num += engine_schematics[i]
    if engine_schematics[i] == "." and current_num != "":
        # numbers.append(current_num)
        current_num = ""
    print("nums loop", numbers, "curr idx", i)

    if engine_schematics[i] in symbols:
        symbol_idx = i
        print("symbol_idx", symbol_idx)
        if len(numbers) > 0:
            # engine_schematics.index()
            pass
    i += 1


print("nums", numbers)


# current_num = ""
# for i in range(len(engine_matrix)):
#     for j in range(len(engine_matrix[i])):
#         current_char = engine_matrix[i][j]
#         if current_char.isnumeric() and current_char != ".":
#             current_num += current_char
#
#             if engine_matrix[i-1][j] in symbols or engine_matrix[i+1][j+1] in symbols or engine_matrix[i][j+1] in symbols:
#                 valid_numbers.append(current_num)
#                 current_num = ""
#             elif 0 < i < len(engine_matrix):
#                 if j == 0:
#                     if engine_matrix[i-1][j] in symbols or engine_matrix[i+1][j] in symbols or engine_matrix[i-1][j+1] in symbols:
#                         valid_numbers.append(current_num)
#                         current_num = ""
