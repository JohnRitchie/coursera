"""
Clone of 2048 game.
"""
import random
import poc_2048_gui


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
    Helper function that slide numbers in line to the left and zeros to the right.
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
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._cells = None

        self._dir_dict = {UP: [],
                          DOWN: [],
                          LEFT: [],
                          RIGHT: []}

        for col in range(self._grid_width):
            self._dir_dict[UP].append((0, col))
            self._dir_dict[DOWN].append((self._grid_height - 1, col))
        for row in range(self._grid_height):
            self._dir_dict[LEFT].append((row, 0))
            self._dir_dict[RIGHT].append((row, self._grid_width - 1))

        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        self._cells = [[0 for dummy_col in range(self._grid_width)]
                       for dummy_row in range(self._grid_height)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        return 'TwentyFortyEight Grid is: {}'.format(self._cells)

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._grid_height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._grid_width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        if direction == UP or direction == DOWN:
            _num_steps = self._grid_height
        elif direction == LEFT or direction == RIGHT:
            _num_steps = self._grid_width

        moved = False
        _tmp_list = []

        for tile in self._dir_dict[direction]:
            for step in range(_num_steps):
                row = tile[0] + step * OFFSETS[direction][0]
                col = tile[1] + step * OFFSETS[direction][1]
                _tmp_list.append(self._cells[row][col])
            _tmp_list_copy = _tmp_list[:]
            _tmp_list = merge(_tmp_list)

            if _tmp_list_copy != _tmp_list:
                moved = True

            idx = 0
            for step in range(_num_steps):
                row = tile[0] + step * OFFSETS[direction][0]
                col = tile[1] + step * OFFSETS[direction][1]
                self._cells[row][col] = _tmp_list[idx]
                idx += 1

            _tmp_list = []

        if moved:
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        _null_coordinates_list = []
        for row in range(len(self._cells)):
            for col in range(len(self._cells[row])):
                if self._cells[row][col] == 0:
                    _null_coordinates_list.append((row, col))

        _row = _null_coordinates_list[random.randrange(len(_null_coordinates_list))][0]
        _col = _null_coordinates_list[random.randrange(len(_null_coordinates_list))][1]

        _percentage_of_2 = int(float(len(_null_coordinates_list)) * 9 / 10)
        _percentage_of_4 = len(_null_coordinates_list) - _percentage_of_2

        _rand_nums_list = [2 for _ in range(_percentage_of_2)]
        for _ in range(_percentage_of_4):
            _rand_nums_list.append(4)

        self._cells[_row][_col] = random.choice(_rand_nums_list)

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._cells[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._cells[row][col]


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
