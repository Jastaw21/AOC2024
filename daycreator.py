import sys
from pathlib import Path


def make_day(day_number: int):

    path_suffix_py = f"2024/Solutions/Day{day_number}.py"
    path_suffix_txt = f"2024/Inputs/Day{day_number}.txt"

    py_file_path = Path(__file__).parent.parent / path_suffix_py
    text_file_path = Path(__file__).parent.parent / path_suffix_txt

    print(py_file_path)
    py_file_obj = open(py_file_path, "x")
    py_file_obj.write("from Utility import commonfuncs as cf\n")

    text_file_obj = open(text_file_path, "x")


if __name__ == "__main__":
    make_day(sys.argv[1])
