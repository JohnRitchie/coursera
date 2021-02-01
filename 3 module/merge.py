"""
Merge function for 2048 game.
"""


def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    # replace with your code

    tmp_list = [0 for _ in range(len(line))]

    result = [0 for _ in range(len(line))]

    index_list = 0
    for number in line:
        if number > 0:
            tmp_list[index_list] = number
            index_list += 1

    print tmp_list

    for indx in range(len(tmp_list)):
        number_index = -1 - indx
        if number_index + len(tmp_list) == 0:
            break
        number = tmp_list[number_index]

        next_number_index = number_index - 1
        next_number = tmp_list[next_number_index]

        if number == next_number:
            tmp_list[number_index] = number + next_number
            tmp_list[next_number_index] = 0

        print tmp_list

    tmp_list.reverse()
    print tmp_list

    index_list = 0
    for number in tmp_list:
        if number > 0:
            result[index_list] = number
            index_list += 1

    return result


# l = [8, 16]
l = [8, 16]
print merge(l)
