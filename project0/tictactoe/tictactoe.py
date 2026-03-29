"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0
    for x in board:
        for y in x:
            if y == X:
                x_count += 1
            elif y == O:
                o_count += 1
    if x_count > o_count:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for row,x in enumerate(board):
        for col,y in enumerate(x):
            if y == EMPTY:
                actions.add((row,col))
    return actions



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i,j = action
    if i<0 or i>2 or j<0 or j>2:
        raise Exception("Out fo bounds move")
    if board[action[0]][action[1]] != EMPTY:
        raise Exception("Invalid Input")
    new_board = copy.deepcopy(board)
    new_board[action[0]][action[1]] = X if player(board) == X else O
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None) or (board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None):
            return True
    if (board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None) or (board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None):
        return True
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    temp = winner(board)
    if temp == X:
        return 1
    elif temp == O:
        return -1
    else:
        return 0

def min_value(state):
    if terminal(state):
        return utility(state)
    v = math.inf
    for action in actions(state):
        v = min(v,max_value(result(state,action)))
    return v
def max_value(state):
    if terminal(state):
        return utility(state)
    v = -math.inf
    for action in actions(state):
        v = max(v,min_value(result(state,action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if(terminal(board)):
        return None
    toplay = player(board)
    bestAction = None
    if toplay == X:
        best_val = -math.inf
    else:
        best_val = math.inf
    for action in actions(board):
        if toplay == X:
            temp = min_value(result(board,action))
            if best_val < temp:
                best_val = temp
                bestAction = action
            if best_val == 1:
                return action
        else:
            temp = max_value(result(board,action))
            if best_val > temp:
                best_val = temp
                bestAction = action
            if best_val == -1:
                return action
    return bestAction
