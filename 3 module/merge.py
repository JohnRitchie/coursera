"""
Merge function for 2048 game.
"""


def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    # replace with your code

    # result = [0 for _ in range(len(line))]

    copy_line = line[:]
    tmp_list = [0 for _ in range(len(line))]

    index_list = 0
    for number in copy_line:
        if number > 0:
            tmp_list[index_list] = number
            index_list += 1

    for indx in range(len(line)):
        index_list = 0
        for number in tmp_list:
            if number > 0:
                tmp_list[index_list] = number
                index_list += 1

        if indx == (len(line) - 1):
            break

        number = tmp_list[indx]
        next_number_index = indx + 1
        next_number = tmp_list[next_number_index]

        print tmp_list

        if number == next_number:
            tmp_list[indx] = number + next_number
            tmp_list[next_number_index] = 0

        print tmp_list

    # index_list = 0
    # for number in tmp_list:
    #     if number > 0:
    #         result[index_list] = number
    #         index_list += 1

    return tmp_list


# l = [8, 16]
# 8, 8, 8, 2 => 8, 16, 2, 0
# 4, 4, 8, 8 => 8, 16, 0, 0
l = [4, 4, 8, 8]
print merge(l)
