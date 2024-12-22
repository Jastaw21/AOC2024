from pathlib import Path


def get_input_data(day_number: int) -> [str]:

    path_file_name_append = "Inputs/Day" + str(day_number) + ".txt"
    path_object = Path(__file__).parent.parent / path_file_name_append

    with open(path_object) as f:
        input_data = [line for line in f]
    return input_data
