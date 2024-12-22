from pathlib import Path

path = Path(__file__).parent.parent / "Inputs/Day2.txt"


# returns the sign of a number -> >0 = 1, 0 = 0, <0 = -1
def sign(number: int) -> int:
    int_sign = -1 if number < 0 else 1
    int_sign = 0 if number == 0 else int_sign
    return int_sign


# turn the raw text input into a list of integers
def intify_level(raw_level: [str]) -> [int]:
    return [int(x) for x in raw_level.split(" ")]


# checks if a raw level follows the rules
def level_is_safe(level_data: [int]) -> bool:
    direction_flag = 0
    last_number = 0
    still_valid = True

    for index, number in enumerate(level_data):

        if index == 0:
            last_number = number

        elif still_valid:
            direction_valid = index == 1 or sign(number - last_number) == direction_flag
            if not direction_valid:
                return False
            direction_flag = sign(number - last_number)
            valid_numbers = []
            lower_numbers = [i for i in range(last_number, last_number - 4, -1)]
            higher_numbers = [i for i in range(last_number, last_number + 4, 1)]

            if abs(number - last_number) <= 3 and direction_valid:
                pass
            else:
                return False
            last_number = number

        else:
            return False
    return True


# works through a level, popping one value at a time, and reevaluting to see if it passes
def level_can_be_made_safe(level_data: [int]) -> bool:
    raw_level_data = intify_level(level_data)
    for index, value in enumerate(raw_level_data):

        temp_list = raw_level_data.pop(index)
        if level_is_safe(temp_list):
            return True
    return False


with open(path) as f:
    input_data = [line for line in f]

# test inputs as given in problem
test_1 = [7, 6, 4, 2, 1]
test_2 = [1, 2, 7, 8, 9]
test_3 = [9, 7, 6, 2, 1]
test_4 = [1, 3, 2, 4, 5]
test_5 = [8, 6, 4, 4, 1]
test_6 = [1, 3, 6, 7, 9]
test_7 = [1, 2, 3, 4, 5, 6, 1, 8, 9]


def part_one():
    # RUN TESTS

    # expected test output
    part_1_test_string = "True False False False False True"

    # actual part 1 output
    part_1_output_string = (
        str(level_is_safe(test_1))
        + " "
        + str(level_is_safe(test_2))
        + " "
        + str(level_is_safe(test_3))
        + " "
        + str(level_is_safe(test_4))
        + " "
        + str(level_is_safe(test_5))
        + " "
        + str(level_is_safe(test_6))
    )

    # part 1 test checker
    print("Part 1 test result: " + str(part_1_test_string == part_1_output_string))

    safe_count = 0

    for level in input_data:
        if level_is_safe(intify_level(level)):
            safe_count += 1

    print(safe_count)


def part_two():
    # run tests
    part_2_test_string = "True False False True True True True"
    part_2_output_string = (
        str(level_can_be_made_safe(test_1))
        + " "
        + str(level_can_be_made_safe(test_2))
        + " "
        + str(level_can_be_made_safe(test_3))
        + " "
        + str(level_can_be_made_safe(test_4))
        + " "
        + str(level_can_be_made_safe(test_5))
        + " "
        + str(level_can_be_made_safe(test_6))
        + " "
        + str(level_can_be_made_safe(test_7))
    )
    print("Part 2 test result: " + str(part_2_test_string == part_2_output_string))

    # run part two

    safe_count = 0
    for level in input_data:
        level_is_safe_already = level_can_be_made_safe(intify_level(level))
        level_can_become_safe = level_can_be_made_safe(intify_level(level))

        if level_can_become_safe or level_is_safe_already:
            safe_count += 1

    print(safe_count)


part_one()
part_two()
