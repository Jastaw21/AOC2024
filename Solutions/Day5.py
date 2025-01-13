import commonfuncs as cF


input_data = cF.get_input_data_as_list_of_lines(5)


# to find where the seperator from the order rules, to the lists of pages is
def find_rule_split(data: [str]) -> int:

    split_found = False

    for index, value in enumerate(data):
        if value == "\n":
            return index


# just get the order rules from the above
def get_mapping(data, rule_split):
    return data[:rule_split]


# intermediate to turn this into a tuple (pair really) of lists of ints
def mapping_to_columns(raw_mapping_data) -> ([int]):
    # get indexes 0,1 of the string and turn to int
    left_column = [int(i[:2]) for i in raw_mapping_data]

    # get 3,4 and intify
    right_column = [int(i[3:5]) for i in raw_mapping_data]

    # stick it in a pair for convenient return
    return left_column, right_column


# returns a dict of {x:[y,z,i,j]} where x is a number that must precede the list of other numbers [y,z,i,z]
def get_rule_orders(mapping_columns: ([int], [int])) -> {int: [int]}:

    mapping_rules = {}

    # use an enumerate to give easy access to the corresponding index in the second list
    for index, value in enumerate(mapping_columns[0]):

        # so 'value' is the number, and now must_be_before is the matching index from the right hand column
        must_be_before = mapping_columns[1][index]

        # check if key exists
        if value in mapping_rules.keys():

            # if it does, can get the value and append this new number to it
            mapping_rules[value].append(must_be_before)
        else:
            # if not, need to allocate it
            mapping_rules[value] = [must_be_before]

    return mapping_rules


# just gets the section of the input below the seperator
def get_pages(data, rule_split) -> str:
    return data[rule_split + 1 :]


def process_pages(pages_data_in: str) -> [[int]]:

    return [[int(i) for i in j.split(",")] for j in pages_data_in]


def test_mapping():

    map_data = get_mapping(input_data, find_rule_split(input_data))
    mapping_columns = mapping_to_columns(map_data)

    print(get_rule_orders(mapping_columns))


def is_ordered(page_order: [int], rules: {int: [int]}) -> bool:
    for index, page_number in enumerate(page_order):

        if page_number in rules.keys():
            numbers_must_be_before = rules[page_number]

            for number in numbers_must_be_before:
                if number in page_order[:index]:
                    return False
                else:
                    pass

        else:
            pass
    return True


def get_middle_number(page_order):
    middle_index = int((len(page_order) - 1) / 2)
    return page_order[middle_index]


def part_one():

    # where is the input file split between rules/pages
    rule_split = find_rule_split(input_data)

    # get the pages, i.e the list of pages that must be printed
    processed_pages_data = process_pages(get_pages(input_data, rule_split))

    # turn the rules into a usable format
    mapping_columns = mapping_to_columns(get_mapping(input_data, rule_split))

    # use this to build the rules
    rule_orders = get_rule_orders(mapping_columns)

    # iterate through all of the given manuals, and increment the count if they're valid
    running_sum = 0
    for i in processed_pages_data:

        if is_ordered(i, rule_orders):
            running_sum += get_middle_number(i)

    print(running_sum)


def fix_order(pages, rules):

    new_pages = [i for i in pages]

    # while loop to allow continuous checking
    while not is_ordered(new_pages, rules):
        # walk through all the pages (enum to give indexing)
        for index, page_number in enumerate(new_pages):

            # sanitise the page we're looking at, don't want a key error
            if page_number in rules.keys():

                # this gives all the numbers our current page_number must be before
                numbers_that_must_follow = rules[page_number]

                # slice to see the numbers that actually precede our numbers
                for sub_index, num in enumerate(new_pages[:index]):

                    # if one of them is a number that must follow our number, swap them over
                    if num in numbers_that_must_follow:
                        new_pages[sub_index], new_pages[index] = (
                            new_pages[index],
                            new_pages[sub_index],
                        )
    return new_pages


def part_two():

    # where is the input file split between rules/pages
    rule_split = find_rule_split(input_data)

    # get the pages, i.e the list of pages that must be printed
    processed_pages_data = process_pages(get_pages(input_data, rule_split))

    # turn the rules into a usable format
    mapping_columns = mapping_to_columns(get_mapping(input_data, rule_split))

    # use this to build the rules
    rule_orders = get_rule_orders(mapping_columns)

    running_sum = 0
    for page_order in processed_pages_data:

        # if it is an invalid number
        if not is_ordered(page_order, rule_orders):

            fixed_order = fix_order(page_order, rule_orders)
            running_sum += get_middle_number(fixed_order)

    print(running_sum)


part_one()
part_two()
