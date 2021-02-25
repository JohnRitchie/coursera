"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 1  # Number of trials to run
SCORE_CURRENT = 2.0  # Score for squares played by the current player
SCORE_OTHER = 1.0  # Score for squares played by the other player
EMPTY = 1
PLAYER_X = 2
PLAYER_O = 3
DRAW = 4


def mc_trial(board, player):
    """
    This function takes a current board and the next player to move.
    The function should play a game starting with the given player by making random moves, alternating between players.
    The function should return when the game is over.
    The modified board will contain the state of the game, so the function does not return anything.
    In other words, the function should modify the board input.
    :param board:
    :param player:
    :return: None
    """
    while board.check_win() not in (PLAYER_X, PLAYER_O, DRAW):
        row, col = random.choice(board.get_empty_squares())
        board.move(row, col, player)
        player = provided.switch_player(player)


def mc_update_scores(scores, board, player):
    """
    This function takes a grid of scores (a list of lists) with the same dimensions as the Tic-Tac-Toe board,
    a board from a completed game, and which player the machine player is.
    The function should score the completed board and update the scores grid.
    As the function updates the scores grid directly, it does not return anything.
    :param scores:
    :param board:
    :param player:
    :return: None
    """
    pass


def get_best_move(board, scores):
    """
    This function takes a current board and a grid of scores.
    The function should find all of the empty squares with the maximum score and
    randomly return one of them as a (row, column) tuple.
    It is an error to call this function with a board that has no empty squares (there is no possible next move),
    so your function may do whatever it wants in that case. The case where the board is full will not be tested.
    :param board:
    :param scores:
    :return: (row, column) tuple
    """
    pass


def mc_move(board, player, trials):
    """
    This function takes a current board, which player the machine player is, and the number of trials to run.
    The function should use the Monte Carlo simulation to return a move for the machine player in
    the form of a (row, column) tuple.
    :param board:
    :param player:
    :param trials:
    :return: (row, column) tuple
    """
    mc_trial(board, player)
    print board
    print board.check_win()


def play():
    board = provided.TTTBoard(3)
    mc_move(board, PLAYER_X, NTRIALS)


if __name__ == '__main__':
    play()

# Test game with the console or the GUI.  Uncomment whichever
# you prefer.  Both should be commented out when you submit
# for testing to save time.

# provided.play_game(mc_move, NTRIALS, False)
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
