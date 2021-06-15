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


def mm_move(board, player):
    """
    Make a move on the board.

    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """

    copy_board = board.clone()

    for square in copy_board.get_empty_squares():
        copy_board.move(square[0], square[1], player)
        score, _ = mm_move(copy_board, provided.switch_player(player))

        if player == provided.PLAYERX and score == 1:
            return score, square
        elif player == provided.PLAYERO and score == -1:
            return score, square
        # elif score == 0:
            # what we need to do is to pickup the move with highest score.
            # Consider the case that playerX has seven empty squares.
            # We need to check the score of each move. If the score is 1, that move is one
            # of the best and you can return (score, square).
            # But, if score=0, you cannot treat this as the best because there are other candidate moves.
            # What you need to do here is set this move as temporary best move and check next empty square.
            # return score, square


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
print board
playerx = provided.PLAYERO
print mm_move(board, playerx)
