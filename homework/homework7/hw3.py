from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    """Analyzes the completed Tic Tac toe board"""
    for symbol in ("x", "o"):
        for i in range(len(board)):
            if board[i][0] == board[i][1] == board[i][2] == symbol:
                return f"{symbol} wins!"
            if board[0][i] == board[1][i] == board[2][i] == symbol:
                return f"{symbol} wins!"
            if board[0][0] == board[1][1] == board[2][2] == symbol:
                return f"{symbol} wins!"
            if board[0][2] == board[1][1] == board[2][0] == symbol:
                return f"{symbol} wins!"
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == "-":
                return "unfinished"
    return "draw!"
