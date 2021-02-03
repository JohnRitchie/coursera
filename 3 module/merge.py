"""
Merge function for 2048 game.
"""


def slide_to_left(line):
    """
    Function that slide numbers in line to the left and zeros to the right.
    """

    result_line = [0 for _ in range(len(line))]

    index_list = 0
    for number in line:
        if number > 0:
            result_line[index_list] = number
            index_list += 1

    return result_line


def merge(line):
    """
    Function that merges a single row or column in 2048.
    """

    copy_line = line[:]
    
    for indx in range(len(line)):

        slided_list = slide_to_left(copy_line)

        number = slided_list[indx]
        next_number_index = indx + 1
        if next_number_index == (len(line)):
            break
        next_number = slided_list[next_number_index]

        if number == next_number:
            slided_list[indx] = number + next_number
            slided_list[next_number_index] = 0

        copy_line = slided_list

    return slided_list
