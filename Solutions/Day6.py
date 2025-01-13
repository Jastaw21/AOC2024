from Utility import commonfuncs as cf


input_data = cf.get_input_data_as_matrix(6)

guard_direction = {"<": (0, -1), ">": (0, 1), "v": (1, 0), "^": (-1, 0)}


def find_guard_start(map_data):
    for row_index, row_data in enumerate(input_data):
        for col_index,col_data in enumerate(row_data):
            if col_data in guard_direction.keys():
                return (row_index, col_index, guard_direction[col_data])


print(find_guard_start(input_data))
