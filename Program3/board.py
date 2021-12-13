# manages a board of chess pieces
# Drew Martin
# 10/22/2021

from chess_utils import BoardInfo
from chess_utils import PieceInfo
from chess_piece import ChessPiece


class Board():
    """Manages a board of chess pieces"""
    BOARD_SIZE = 8

    def __init__(self):
        self._board_info = [
            [None]*Board.BOARD_SIZE for i in range(Board.BOARD_SIZE)]

    def write_to_file(self, outfile):
        """writes the board to an already open output file"""
        for row in self._board_info:
            for piece in row:
                if piece == None:
                    outfile.write(PieceInfo.EMPTY.value)
                else:
                    outfile.write(piece.get_label().value)
            outfile.write('\n')

    def add_piece(self, row, col, piece):
        """adds the piece to the board"""
        self._board_info[row][col] = piece

    def get_square_info(self, row, col):
        """Returns information about the square 
            (off the board, empty, black or white)"""
        if not(Board.__is_on_board(row) and Board.__is_on_board(col)):
            return BoardInfo.OFF_THE_BOARD
        elif self._board_info[row][col] == None:
            return BoardInfo.EMPTY
        else:
            return self._board_info[row][col].get_color()

    def check_move(self, from_row, from_col, to_row, to_col):
        """determine whether the arguments represent a legal move"""
        is_legal = False  # assume false
        if Board.__is_on_board(from_row) and Board.__is_on_board(from_col) and Board.__is_on_board(to_row) and Board.__is_on_board(to_col) and self._board_info[from_row][from_col] != None:
            is_legal = self._board_info[from_row][from_col].is_legal_move(
                to_row, to_col, self)
        return is_legal

    def make_move(self, from_row, from_col, to_row, to_col):
        """make a move if it's legal--return false if not"""
        if self.check_move(from_row, from_col, to_row, to_col):
            self._board_info[from_row][from_col].move(to_row, to_col)
            self._board_info[to_row][to_col] = self._board_info[from_row][from_col]
            self._board_info[from_row][from_col] = None
            return True
        else:
            return False

    def display_possible_moves(self, row, col, outfile):
        """prints a board displaying possible moves from row,col"""
        # make an empty display board
        char_board = Board.__make_empty_char_board()

        # add valid moves (if any)
        if Board.__is_on_board(row) and Board.__is_on_board(col) and self._board_info[row][col] != None:
            char_board = self._board_info[row][col].generate_legal_moves(
                char_board, self)

        # display the result
        for row in char_board:
            for piece in row:
                outfile.write(piece)
            outfile.write('\n')

    def __make_empty_char_board():
        """make an empty board of characters"""
        return [[PieceInfo.EMPTY.value]*Board.BOARD_SIZE
                for i in range(Board.BOARD_SIZE)]

    def __is_on_board(index):
        """true if the index is on the board"""
        return index >= 0 and index < 8