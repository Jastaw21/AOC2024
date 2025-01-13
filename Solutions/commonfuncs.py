from pathlib import Path


def get_input_data_as_list_of_lines(day_number: int) -> [str]:

    path_file_name_append = "Inputs/Day" + str(day_number) + ".txt"
    path_object = Path(__file__).parent.parent / path_file_name_append

    with open(path_object) as f:
        input_data = [line for line in f]
    return input_data


def get_input_data_as_matrix(day_number: int) -> [[]]:
    path_file_name_append = "Inputs/Day" + str(day_number) + ".txt"
    path_object = Path(__file__).parent.parent / path_file_name_append

    with open(path_object) as f:
        input_data = [line for line in f]

    matrix = []
    for row in input_data:
        columns = []
        for value in row:
            if value == "\n":
                pass
            else:
                columns.append(value)
        matrix.append(columns)
    return matrix
