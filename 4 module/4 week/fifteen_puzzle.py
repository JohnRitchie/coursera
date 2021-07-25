"""
Loyd's Fifteen puzzle - solver and visualizer
Note that solved configuration has the blank (zero) tile in upper left
Use the arrows key to swap this tile with its neighbors
"""

import random
import poc_fifteen_gui_ignore_ as poc_fifteen_gui


class Puzzle:
    """
    Class representation for the Fifteen puzzle
    """

    def __init__(self, puzzle_height, puzzle_width, initial_grid=None):
        """
        Initialize puzzle with default height and width
        Returns a Puzzle object
        """
        self._height = puzzle_height
        self._width = puzzle_width
        self._grid = [[col + puzzle_width * row
                       for col in range(self._width)]
                      for row in range(self._height)]

        if initial_grid is not None:
            for row in range(puzzle_height):
                for col in range(puzzle_width):
                    self._grid[row][col] = initial_grid[row][col]

    def __str__(self):
        """
        Generate string representaion for puzzle
        Returns a string
        """
        ans = ""
        for row in range(self._height):
            ans += str(self._grid[row])
            ans += "\n"
        return ans

    #####################################
    # GUI methods

    def get_height(self):
        """
        Getter for puzzle height
        Returns an integer
        """
        return self._height

    def get_width(self):
        """
        Getter for puzzle width
        Returns an integer
        """
        return self._width

    def get_number(self, row, col):
        """
        Getter for the number at tile position pos
        Returns an integer
        """
        return self._grid[row][col]

    def set_number(self, row, col, value):
        """
        Setter for the number at tile position pos
        """
        self._grid[row][col] = value

    def clone(self):
        """
        Make a copy of the puzzle to update during solving
        Returns a Puzzle object
        """
        new_puzzle = Puzzle(self._height, self._width, self._grid)
        return new_puzzle

    ########################################################
    # Core puzzle methods

    def current_position(self, solved_row, solved_col):
        """
        Locate the current position of the tile that will be at
        position (solved_row, solved_col) when the puzzle is solved
        Returns a tuple of two integers
        """
        solved_value = (solved_col + self._width * solved_row)

        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == solved_value:
                    return row, col
        assert False, "Value " + str(solved_value) + " not found"

    def update_puzzle(self, move_string):
        """
        Updates the puzzle state based on the provided move string
        """
        zero_row, zero_col = self.current_position(0, 0)
        for direction in move_string:
            if direction == "l":
                assert zero_col > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col - 1]
                self._grid[zero_row][zero_col - 1] = 0
                zero_col -= 1
            elif direction == "r":
                assert zero_col < self._width - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col + 1]
                self._grid[zero_row][zero_col + 1] = 0
                zero_col += 1
            elif direction == "u":
                assert zero_row > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row - 1][zero_col]
                self._grid[zero_row - 1][zero_col] = 0
                zero_row -= 1
            elif direction == "d":
                assert zero_row < self._height - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row + 1][zero_col]
                self._grid[zero_row + 1][zero_col] = 0
                zero_row += 1
            else:
                assert False, "invalid direction: " + direction

    ##################################################################
    # Phase one methods

    def lower_row_invariant(self, target_row, target_col):
        """
        Check whether the puzzle satisfies the specified invariant
        at the given position in the bottom rows of the puzzle (target_row > 1)
        Returns a boolean
        """
        if not self.get_number(target_row, target_col) == 0:
            print 'Not zero!'
            return False

        flat_grid = [self.get_number(row, col)
                     for row in range(self._height)
                     for col in range(self._width)]
        standard_grid = Puzzle(self._height, self._width)
        flat_standard_grid = [standard_grid.get_number(row, col)
                              for row in range(self._height)
                              for col in range(self._width)]

        target_index = target_col + self._width * target_row
        while target_index + 1 < len(flat_grid):
            target_index += 1
            if flat_grid[target_index] != flat_standard_grid[target_index]:
                print 'Not match!'
                return False

        return True

    def position_tile(self, target_pos, target_tile):
        """
        Helper function
        """
        move_string = ''
        target_row, target_col = target_pos
        current_row, current_col = target_tile

        if target_row == current_row:
            move_string += 'l' * (target_col - current_col)
        elif target_row > current_row and target_col == current_col:
            move_string += 'u' * (target_row - current_row)
        elif target_row > current_row and target_col > current_col:
            move_string += 'l' * (target_col - current_col)
            move_string += 'u' * (target_row - current_row)
            # move_string += 'lddruld'
        elif target_row > current_row and target_col < current_col:
            move_string += 'u'
            move_string += 'r' * (current_col - target_col)
            move_string += 'u' * (target_row - current_row - 1)

        return move_string

    def solve_interior_tile(self, target_row, target_col):
        """
        Place correct tile at target position
        Updates puzzle and returns a move string
        """
        # assert self.lower_row_invariant(target_row, target_col)
        # assert target_row > 1, "target row <= 1 !"
        # assert target_col > 0, "target col <= 0 !"

        current_row, current_col = self.current_position(target_row, target_col)
        # assert current_row <= target_row, "current row > target row !"
        # assert current_col < target_col, "current col >= target col !"

        target_pos = (target_row, target_col)
        target_tile = (current_row, current_col)
        move_string = self.position_tile(target_pos, target_tile)

        self.update_puzzle(move_string)
        # assert self.lower_row_invariant(target_row, target_col - 1)
        return move_string

    def solve_col0_tile(self, target_row):
        """
        Solve tile in column zero on specified row (> 1)
        Updates puzzle and returns a move string
        """
        # replace with your code
        return ""

    #############################################################
    # Phase two methods

    def row0_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row zero invariant
        at the given column (col > 1)
        Returns a boolean
        """
        if not self.get_number(0, target_col) == 0:
            print 'Not zero!'
            return False

        standard_grid = Puzzle(self._height, self._width)
        standard_row0 = standard_grid._grid[0]
        row0 = self._grid[0]

        target_index = target_col
        while target_index + 1 < len(row0):
            target_index += 1
            if row0[target_index] != standard_row0[target_index]:
                print 'Not match row0!'
                return False

        flat_grid = [self.get_number(row, col)
                     for row in range(self._height)
                     for col in range(self._width)]
        flat_standard_grid = [standard_grid.get_number(row, col)
                              for row in range(self._height)
                              for col in range(self._width)]

        remainder_index = target_col + self._width
        while remainder_index < len(flat_grid):
            if flat_grid[remainder_index] != flat_standard_grid[remainder_index]:
                print 'Not match rest!'
                return False
            remainder_index += 1

        return True

    def row1_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row one invariant
        at the given column (col > 1)
        Returns a boolean
        """
        if not self.get_number(1, target_col) == 0:
            print 'Not zero!'
            return False

        standard_grid = Puzzle(self._height, self._width)
        flat_grid = [self.get_number(row, col)
                     for row in range(self._height)
                     for col in range(self._width)]
        flat_standard_grid = [standard_grid.get_number(row, col)
                              for row in range(self._height)
                              for col in range(self._width)]

        target_index = target_col + self._width
        while target_index + 1 < len(flat_grid):
            target_index += 1
            if flat_grid[target_index] != flat_standard_grid[target_index]:
                print 'Not match!'
                return False

        return True

    def solve_row0_tile(self, target_col):
        """
        Solve the tile in row zero at the specified column
        Updates puzzle and returns a move string
        """
        # replace with your code
        return ""

    def solve_row1_tile(self, target_col):
        """
        Solve the tile in row one at the specified column
        Updates puzzle and returns a move string
        """
        # replace with your code
        return ""

    ###########################################################
    # Phase 3 methods

    def solve_2x2(self):
        """
        Solve the upper left 2x2 part of the puzzle
        Updates the puzzle and returns a move string
        """
        # replace with your code
        return ""

    def solve_puzzle(self):
        """
        Generate a solution string for a puzzle
        Updates the puzzle and returns a move string
        """
        # replace with your code
        zero_row, zero_col = self.current_position(0, 0)

        return self.solve_interior_tile(zero_row, zero_col)


def make_grid():
    grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    height = len(grid)
    width = len(grid)
    flat_grid = []

    for tile in range(16):
        flat_grid.append(tile)

    flat_grid = random.sample(flat_grid, len(flat_grid))

    flat_grid_index = 0
    for row in range(height):
        for col in range(width):
            grid[row][col] = flat_grid[flat_grid_index]
            flat_grid_index += 1

    return grid


grid_3 = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
# grid_4 = [[1, 7, 9, 8], [4, 5, 6, 3], [2, 10, 0, 11], [12, 13, 14, 15]]
# grid_4 = [[1, 10, 9, 8], [4, 5, 6, 3], [2, 7, 0, 11], [12, 13, 14, 15]]
# grid_4 = [[1, 7, 10, 8], [4, 5, 6, 3], [2, 9, 0, 11], [12, 13, 14, 15]]
grid_4 = [[1, 7, 9, 10], [4, 5, 6, 3], [2, 8, 0, 11], [12, 13, 14, 15]]
grid_5 = [[11, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 0, 12, 13, 14],
          [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]]
# grid = make_grid()

# Start interactive simulation
poc_fifteen_gui.FifteenGUI(Puzzle(4, 4, initial_grid=grid_4))
# puzzle = Puzzle(5, 5, grid_5)
# puzzle.solve_interior_tile(2, 1)
