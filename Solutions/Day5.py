import commonFuncs as CF


input_data = CF.get_input_data_as_list_of_lines(5)


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


def page_order_is_valid(page_order: [int], rules: {int: [int]}) -> bool:
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



processed_pages_data = process_pages(get_pages(input_data, find_rule_split(input_data)))


mapping_columns = mapping_to_columns(get_mapping(input_data, find_rule_split(input_data)))
rule_orders = get_rule_orders(mapping_columns)

running_sum = 0
for i in processed_pages_data:

    if page_order_is_valid(i, rule_orders):
        running_sum += get_middle_number(i)

print(running_sum)
