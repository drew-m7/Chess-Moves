# constants and utilities for the chess move checker
# Drew Martin
# 10/21/2021

from enum import Enum


class BoardInfo(Enum):
    EMPTY = 0
    BLACK = 1
    WHITE = 2
    OFF_THE_BOARD = 3


class PieceInfo(Enum):
    EMPTY = '_'
    BLACK = 'b'
    WHITE_PAWN = 'P'
    WHITE_ROOK = 'R'
    WHITE_KNIGHT = 'N'
    WHITE_QUEEN = 'Q'
    WHITE_KING = 'K'
    WHITE_BISHOP = 'B'