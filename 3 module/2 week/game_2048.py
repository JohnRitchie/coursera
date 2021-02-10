"""
Clone of 2048 game.
"""
import sys
sys.path.append('C:\\Users\\vlazarenko\\Desktop\\coursera\\3 module\\ext')

try:
    import poc_2048_gui
except ImportError:
    import ext.poc_2048_gui as poc_2048_gui
try:
    import poc_simpletest
except ImportError:
    import ext.poc_simpletest as poc_simpletest

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}


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
    Helper function that merges a single row or column in 2048
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


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        pass

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # replace with your code
        pass

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        return ""

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return 0

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return 0

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        pass

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        pass

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        pass

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return 0


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
