from pathlib import Path
import re
import commonFuncs as CF


input_data = CF.get_input_data_as_list_of_lines(3)

# change the seperate line format of the input into one string
joined_input = "".join(input_data)


# just runs the regex match on the data, and returns it as a list of strings
def get_raw_matches(input_string: str) -> [str]:
    regex_str = r"mul\([0-9]{1,3},[0-9]{1,3}\)"
    return re.findall(regex_str, input_string)


# turns a sub string that has been matched, ie mul(123,9) to it's integer product result
def mul_str_to_answer(input_mul_str: str) -> int:
    # strip out the individual numbers, saves using text before and after etc to find the comma
    individual_number_regex = r"[0-9]{1,3}"

    # don't need to worry about cases where there's not 2 matches, we'll only pass in cases where there are
    results = re.findall(individual_number_regex, input_mul_str)
    return int(results[0]) * int(results[1])


def get_valid_ranges():
    dont_regex = r"don't\(\)"
    do_regex = r"do\(\)"

    # find all the dos and donts
    do_matches = re.finditer(do_regex, joined_input)
    dont_matches = re.finditer(dont_regex, joined_input)

    # build lists of where they start, including assuming the first thing is a do
    do_starts = [0]
    for match in do_matches:
        do_starts.append(match.start())

    dont_starts = []
    for match in dont_matches:
        dont_starts.append(match.start())

    # to populate with ranges
    valid_ranges = []

    # to track when we find a new don't
    last_new_dont = 0
    # to track how many times we see a given don't value, basically to only take the first one
    repeated_dont_value_count = 0

    # now walk through the lists, to build acceptable ranges
    for do in do_starts:

        # intention is to get the next don't that's bigger than the current do
        # step one, probably inefficient, get the list of don'ts greater than this one
        donts_greater_than_last_do = list(filter(lambda x: x > do, dont_starts))

        # check there is any, to avoid an index out of range situation
        if len(donts_greater_than_last_do) > 0:
            # the smallest don't fitting the criteria will be in list index 0
            next_dont = donts_greater_than_last_do[0]
        else:
            # other wise, there isn't any, so we can just use the end of file
            next_dont = len(joined_input)

        # have we seen a new don't?
        if next_dont == last_new_dont:
            # if so, build the counter
            repeated_dont_value_count += 1

        # if it's new, set the tracker to track the new one, and reset count
        else:
            repeated_dont_value_count = 0
            last_new_dont = next_dont

        if repeated_dont_value_count < 1:
            do_range = (do, next_dont)
            valid_ranges.append(do_range)
    return valid_ranges


def part_one():
    matches = get_raw_matches(joined_input)
    running_sum = 0
    for match in matches:
        running_sum += mul_str_to_answer(match)
    print(running_sum)


def part_two():
    running_sum = 0
    for i in get_valid_ranges():
        # get the sliced string to test
        string_to_test = joined_input[i[0] : i[1] + len("don't()")]

        matches = get_raw_matches(string_to_test)
        for match in matches:
            running_sum += mul_str_to_answer(match)
    print(running_sum)


part_one()
part_two()
