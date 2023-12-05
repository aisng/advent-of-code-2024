engine_schematics = ("467..114.....*........35..633.......#...617*...........+.58...592...........755....$.*.....664"
                     ".598..")

symbols = "*#+$"

i = 0
valid_numbers = []
numbers = []
current_num = ""
# number_indices = {}



# while i < len(engine_schematics):
#
#     if engine_schematics[i].isnumeric():
#         current_num += engine_schematics[i]
#     if engine_schematics[i] == "." and current_num != "":
#         # numbers.append(current_num)
#         current_num = ""
#     print("nums loop", numbers, "curr idx", i)
#
#     if engine_schematics[i] in symbols:
#         symbol_idx = i
#         print("symbol_idx", symbol_idx)
#         if len(numbers) > 0:
#             # engine_schematics.index()
#             pass
#     i += 1
#
#
# print("nums", numbers)


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

# if current_char in symbols:
#     symbol_coordinates = (i, j)
#     # print("sym coord", symbol_coordinates)
#     # directions
#     n = engine_matrix[i - 1][j]
#     ne = engine_matrix[i - 1][j + 1]
#     e = engine_matrix[i][j + 1]
#     se = engine_matrix[i + 1][j + 1]
#     s = engine_matrix[i + 1][j]
#     sw = engine_matrix[i + 1][j - 1]
#     w = engine_matrix[i][j - 1]
#     nw = engine_matrix[i - 1][j - 1]
#
#     if n.isdigit():
#         if nw == ".":
#             for elem in engine_matrix[i - 1][j:row_len]:
#                 if elem.isdigit():
#                     current_num += elem
#             valid_numbers.append(int(current_num))
#         current_num = ""
#
#     if ne.isdigit():
#         for elem in engine_matrix[i - 1][j:row_len]:
#             if elem.isdigit():
#                 current_num += elem
#         valid_numbers.append(int(current_num))
#         current_num = ""
#
#     if e.isdigit():
#         for elem in engine_matrix[i][j + 1:row_len]:
#             if elem.isdigit():
#                 current_num += elem
#         valid_numbers.append(int(current_num))
#         current_num = ""
#
#     if se.isdigit():
#         for elem in engine_matrix[i + 1][j + 1:row_len]:
#             if elem.isdigit():
#                 current_num += elem
#         valid_numbers.append(int(current_num))
#         current_num = ""
#
#     if s.isdigit():
#         if not se.isdigit():
#             # sw logic
#             for elem in engine_matrix[i + 1][0:j + 1]:
#                 if elem.isdigit():
#                     current_num += elem
#             valid_numbers.append(int(current_num))
#         if not sw.isdigit():
#             pass
#         current_num = ""
#
#     if sw.isdigit():
#         # added +1 to range to include the found value
#         for elem in engine_matrix[i + 1][0:j + 1]:
#             if elem.isdigit():
#                 current_num += elem
#         valid_numbers.append(int(current_num))
#         current_num = ""
#
#     if w.isdigit():
#         for elem in engine_matrix[i][0:j]:
#             if elem.isdigit():
#                 current_num += elem
#         valid_numbers.append(int(current_num))
#         current_num = ""
#
#     if nw.isdigit():
#         for elem in engine_matrix[i - 1][0:j - 1 + 1]:
#             if elem.isdigit():
#                 current_num += elem
#         valid_numbers.append(int(current_num))
#         current_num = ""
a = [(4, 0), (8, 1), (0, 2), (0, 5), (0, 6)]

for j, k in a:
    print(j,k)