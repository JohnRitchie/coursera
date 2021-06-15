"""
Mini-max Tic-Tac-Toe Player
"""

import SimpleGUICS2Pygame.codeskulptor as codeskulptor
import poc_ttt_gui_ignore_ as poc_ttt_gui
import poc_ttt_provided_ignore_ as provided
import random

# Set timeout, as mini-max can take a long time
codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}


def children(board, player):
    copy_board = board.clone()
    children_boards = []

    for square in copy_board.get_empty_squares():
        tmp_board = board.clone()
        tmp_board.move(square[0], square[1], player)
        children_boards.append(tmp_board)

    return children_boards


my_board = [[3, 2, 3], [2, 2, 3], [2, 1, 1]]  # two free
board = provided.TTTBoard(3, board=my_board)
playerx = provided.PLAYERX
boards = children(board, playerx)
for board in boards:
    print board


def mm_move(board, player):
    """
    Make a move on the board.

    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    # opponent_player = provided.switch_player(player)
    # empty_squares_list = board.get_empty_squares()

    print copy_board
    expected_score = 1 if player == provided.PLAYERX else -1

    if not copy_board.get_empty_squares():  # base case
        return SCORES[board.check_win()], 'there is not empty squares'

    # while board.check_win() not in (provided.PLAYERX, provided.PLAYERO, provided.DRAW):
    #     row, col = random.choice(board.get_empty_squares())
    #     board.move(row, col, player)
    #     player = provided.switch_player(player)


    return SCORES[board.check_win()], board.check_win()
    # return 0, (-1, -1)


def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]


# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.
# provided.play_game(move_wrapper, 1, False)
# poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)

# my_board = [[1, 2, 1], [1, 1, 1], [1, 1, 1]]  # one full cell
# my_board = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]  # full
my_board = [[3, 2, 3], [2, 2, 3], [2, 1, 1]]  # two free
board = provided.TTTBoard(3, board=my_board)
playerx = provided.PLAYERX
# print mm_move(board, playerx)
