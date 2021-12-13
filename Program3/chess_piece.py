# class chess piece
# Drew Martin
# 10/22/2021

from chess_utils import BoardInfo
from chess_utils import PieceInfo

class ChessPiece:
    _row = None
    _col = None
    _color = None

    def __init__(self, row_num, col_num, color):
        self._row = row_num
        self._col = col_num
        self._color = color

    def move(self, new_row, new_col):
        self._row = new_row
        self._col = new_col

    def get_color(self):
        return self._color

    def get_label():
        return PieceInfo.EMPTY

    def is_legal_move(dest_row, dest_col, board):
        return False

    def generate_legal_moves(board_data, board):
        return [0][0]

    # Added an extra method similar to checking a square from the given king class
    def square_available(self, square):
        is_available = (square != self._color and square != BoardInfo.OFF_THE_BOARD)
        return is_available
