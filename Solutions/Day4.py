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


def get_x_masses():
    # generates a list of possible X-MAS, in form of the five relevant characters
    # this grid:
    #   S ? S
    #   ? A ?
    #   M ? M
    #
    # becomes a list with the indexes as:
    #   0 ? 1
    #   ? 2 ?
    #   4 ? 5
    # so it'd look like this: [S,S,A,M,M]

    # used to generate all combos of S?S, S?M etc
    top = ["S", "M"]
    bottom = top

    possible_xmases = []
    for i in top:
        for j in bottom:


            # oppose the bottom right to the top left
            if i == "M":
                m = "S"
            else:
                m = "M"

            # same for the rights
            if j == "M":
                k = "S"
            else:
                k = "M"

            # generate a list, of a list of chars for each line
            mas_combo = [i, j, "A", k, m]

            # add this combo to the master list
            possible_xmases.append(mas_combo)

    return possible_xmases


def index_to_grid_list(data, index: (int, int)) -> [str]:
    # returns the relevant grid from a starting point
    # this grid:
    #   S ? S
    #   ? A ?
    #   M ? M
    #
    # becomes a list with the indexes as:
    #   0 ? 1
    #   ? 2 ?
    #   4 ? 5
    # so it'd look like this: [S,S,A,M,M]

    # map of where to offset to in the grid, for each character in the output string.
    #   0,0  -  0,2
    #    -  1,1  -
    #   2,0  -  2,2

    start_row = index[0]
    start_col = index[1]

    offsets = [(0, 0), (0, 2), (1, 1), (2, 0), (2, 2)]
    grid_list = []
    if index[0] <= g_max_columns - 2 and index[1] <= g_max_rows - 2:
        for offset in offsets:
            new_row = start_row + offset[0]
            new_col = start_col + offset[1]

            grid_list.append(data[new_row][new_col])
    return grid_list


def part_one():
    running_sum = 0
    for x in get_locations_by_letter_index(input_data, 0):
        if x == (2, 4):
            pass
        paths = build_valid_paths(x)
        for path in paths:
            string_generated = path_to_characters(input_data, path)
            if string_generated == "XMAS":
                running_sum += 1

    print(running_sum)


def part_two():
    running_sum = 0
    for row, row_data in enumerate(input_data):
        for col, value in enumerate(row_data):
            grid = index_to_grid_list(input_data, (row, col))
            if grid in get_x_masses():
                running_sum += 1
                print(grid, (row, col), "Found")
    print(running_sum)


part_two()
