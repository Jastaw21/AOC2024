import string

import commonFuncs as CF


input_data = CF.get_input_data_as_matrix(4)
g_max_rows = len(input_data) - 1
g_max_columns = len(input_data[0]) - 1

xmas_list = ["X", "M", "A", "S"]
list_following_x = xmas_list[1:]


def get_locations_by_letter_index(data, letter_index: int) -> [(int, int)]:
    letter_locations = []

    for row, row_data in enumerate(data):
        for column, value in enumerate(row_data):
            if value == xmas_list[letter_index]:
                letter_locations.append((row, column))

    return letter_locations


def build_valid_paths(x_start: (int, int)) -> [[int]]:

    paths = []

    row = x_start[0]
    col = x_start[1]

    # left
    if col >= 3:
        left_path = [(row, i) for i in range(col - 3, col + 1, 1)]
        left_path.reverse()
        paths.append(left_path)

    # right
    if col <= g_max_columns - 3:
        right_path = [(row, i) for i in range(col, col + 4, 1)]
        paths.append(right_path)

    # up
    if row >= 3:
        up_path = [(i, col) for i in range(row - 3, row + 1, 1)]
        up_path.reverse()
        paths.append(up_path)

    # down
    if row <= g_max_rows - 3:
        down_path = [(i, col) for i in range(row, row + 4, 1)]
        paths.append(down_path)

    # diag down right
    if row <= g_max_rows - 3 and col <= g_max_columns - 3:
        diag_right_path = []
        for i in range(0, 4, 1):
            diag_right_path.append((row + i, col + i))
        paths.append(diag_right_path)

    # diag down left
    if row <= g_max_rows - 3 and col >= 3:
        diag_left_path = []
        for i in range(0, 4, 1):
            diag_left_path.append((row + i, col - i))
        paths.append(diag_left_path)

    # diag up right
    if row >= 3 and col <= g_max_columns - 3:
        diag_up_right_path = []
        for i in range(0, 4, 1):
            diag_up_right_path.append((row - i, col + i))
        paths.append(diag_up_right_path)

    # diag up left
    if row >= 3 and col >= 3:
        diag_up_left_path = []
        for i in range(0, 4, 1):
            diag_up_left_path.append((row - i, col - i))
        paths.append(diag_up_left_path)

    return paths


def path_to_characters(data, path: [(int, int)]) -> str:
    base_string = []
    for coord in path:
        x = coord[0]
        y = coord[1]
        letter = data[x][y]
        base_string.append(letter)
    return_string = "".join(base_string)
    return return_string


def part_one():
    running_sum = 0
    for x in get_locations_by_letter_index(input_data, 0):
        if x == (2,4):
            pass
        paths = build_valid_paths(x)
        for path in paths:
            string_generated = path_to_characters(input_data, path)
            if string_generated == 'XMAS':
                running_sum += 1

    print(running_sum)

part_one()