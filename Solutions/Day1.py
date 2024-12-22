from collections import Counter
import commonFuncs as CF

input_data = CF.get_input_data(1)

l_column = []
r_column = []

for line in input_data:
    column_tracker = 1
    columns = line.split("   ")
    for col in columns:
        col = col.rstrip("\n")
        if column_tracker == 1:
            l_column.append(int(col))
        else:
            r_column.append(int(col))
        column_tracker += 1

l_column.sort()
r_column.sort()

# part 1
running_sum = 0

# part 2
r_column_counted = Counter(r_column)
similarity_score = 0

for index, value in enumerate(l_column):
    running_sum += abs(value - r_column[index])

    num_occurences = r_column_counted[value]
    similarity_score += num_occurences * value


print(running_sum)
print(similarity_score)
