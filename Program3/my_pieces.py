# The file has the blackPiece and the king in it
# Drew Martin
# 10/22/2021

from chess_piece import ChessPiece
from board import Board
from chess_utils import BoardInfo
from chess_utils import PieceInfo


class BlackPiece(ChessPiece):
    """A black piece that never does anything -- we're always playing white"""

    def __init__(self, row_num, col_num):
        ChessPiece.__init__(self, row_num, col_num, BoardInfo.BLACK)
        self.label = PieceInfo.BLACK

    def get_label(self):
        return self.label

    def generate_legal_moves(self, board_data, board):
        """Adds representation for the legal moves to the provided 
        board representation and returns the result"""
        board_data[self._row][self._col] = self.label.value
        return board_data


class King(ChessPiece):
    def __init__(self, row_num, col_num, color, label):
        ChessPiece.__init__(self, row_num, col_num, color)
        self.label = label

    def get_label(self):
        return self.label

    def is_legal_move(self, dest_row, dest_col, board):
        """Returns true if this piece can legally move to the specified
        location on the provide board"""
        row_diff = abs(self._row-dest_row)
        col_diff = abs(self._col-dest_col)
        square_type = board.get_square_info(dest_row, dest_col)

        is_legal = (row_diff == 1 and col_diff < 2 or row_diff < 2 and col_diff ==
                    1) and square_type != self._color and square_type != BoardInfo.OFF_THE_BOARD
        return is_legal

    def generate_legal_moves(self, board_data, board):
        """Adds representation for the legal moves to the provided 
        board representation and returns the result"""
        char_label = self.label.value
        board_data[self._row][self._col] = char_label
        for row in range(self._row-1, self._row+2):
            for col in range(self._col-1, self._col+2):
                square_type = board.get_square_info(row, col)
                if square_type != self._color and square_type != BoardInfo.OFF_THE_BOARD:
                    board_data[row][col] = char_label
        return board_data

class Knight(ChessPiece):
    def __init__(self, row_num, col_num, color, label):
        ChessPiece.__init__(self, row_num, col_num, color)
        self.label = label

    def get_label(self):
        return self.label

    def is_legal_move(self, dest_row, dest_col, board):
        """Returns true if this piece can legally move to the specified
        location on the provide board"""
        row_diff = abs(self._row-dest_row)
        col_diff = abs(self._col-dest_col)
        square_type = board.get_square_info(dest_row, dest_col)

        is_legal = (row_diff == 1 and col_diff == 2 or row_diff == 2 and col_diff ==
                    1) and square_type != self._color and square_type != BoardInfo.OFF_THE_BOARD
        return is_legal

    def generate_legal_moves(self, board_data, board):
        """Adds representation for the legal moves to the provided 
        board representation and returns the result"""
        char_label = self.label.value
        board_data[self._row][self._col] = char_label
        row = self._row
        col = self._col
        # knight can go in an L movement, 1 move 1 way, then 2 the other way or vice versa
        # list for legal knight moves
        list_legal = [(self._row-2, self._col+1),
        (self._row+2,self._col+1),
        (self._row+2,self._col-1),
        (self._row-2,self._col-1),
        (self._row-1,self._col+2),
        (self._row+1,self._col+2),
        (self._row+1,self._col-2),
        (self._row-1,self._col-2)]
        for (row,col) in list_legal:
            square_type = board.get_square_info(row, col)
            if square_type != self._color and square_type != BoardInfo.OFF_THE_BOARD:
                board_data[row][col] = char_label
        return board_data

class Rook(ChessPiece):
    def __init__(self, row_num, col_num, color, label):
        ChessPiece.__init__(self, row_num, col_num, color)
        self.label = label

    def get_label(self):
        return self.label

    def is_legal_move(self, dest_row, dest_col, board):
        """Returns true if this piece can legally move to the specified
        location on the provide board"""
        row_diff = abs(self._row-dest_row)
        col_diff = abs(self._col-dest_col)
        square_type = board.get_square_info(dest_row, dest_col)

        # trying to find intervening pieces in way
        row = self._row
        col = self._col
        # starting = [row][col]
        # ending = [dest_row][dest_col]
        def col_blocked(self, starting, ending, board):
            for x in range(starting, ending):
                if not self.square_available(self._row, col):
                    return True
                elif board.get_square_info(self._row, col) ==BoardInfo.BLACK and col < ending:
                    return True
        def row_blocked(self, starting, ending, board):
            for x in range(starting, ending):
                if not self.square_available(row, self._col):
                    return True
                elif board.get_square_info(row, self._col) ==BoardInfo.BLACK and row < ending:
                    return True
        # enemy_in_way = False
        # col = self._col + 1
        # while (self.square_available(board.get_square_info(self._row, col)) and not enemy_in_way):
        #     col += 1
        #     if (board.get_square_info(self._row, col - 1) == BoardInfo.BLACK):
        #         enemy_in_way = True
        # enemy_in_way = False
        # col = self._col - 1
        # while (self.square_available(board.get_square_info(self._row, col)) and not enemy_in_way):
        #     col -= 1
        #     if (board.get_square_info(self._row, col + 1) == BoardInfo.BLACK):
        #         enemy_in_way = True
        # enemy_in_way = False
        # row = self._row + 1
        # while (self.square_available(board.get_square_info(row, self._col)) and not enemy_in_way):
        #     row += 1
        #     if (board.get_square_info(row - 1, self._col) == BoardInfo.BLACK):
        #         enemy_in_way = True
        # enemy_in_way = False
        # row = self._row - 1
        # while (self.square_available(board.get_square_info(row, self._col)) and not enemy_in_way):
        #     row -= 1
        #     if (board.get_square_info(row + 1, self._col) == BoardInfo.BLACK):
        #         enemy_in_way = True
        
        is_legal = (row_diff == 0 and col_diff < 9 or row_diff < 9 and col_diff ==
                    0) and square_type != self._color and square_type != BoardInfo.OFF_THE_BOARD 
                    # and row_blocked == False and col_blocked == False)
        return is_legal

    # had to use seperate loops for each possible direction up down side to side
    def generate_legal_moves(self, board_data, board):
        """Adds representation for the legal moves to the provided 
        board representation and returns the result"""
        char_label = self.label.value
        board_data[self._row][self._col] = char_label

        # check for enemies
        enemy_in_way = False
        # column straight up
        col = self._col + 1
        while (self.square_available(board.get_square_info(self._row, col)) and not enemy_in_way):
            board_data[self._row][col] = char_label
            col += 1
            if (board.get_square_info(self._row, col - 1) == BoardInfo.BLACK):
                enemy_in_way = True

        enemy_in_way = False
        # column straight down
        col = self._col - 1
        while (self.square_available(board.get_square_info(self._row, col)) and not enemy_in_way):
            board_data[self._row][col] = char_label
            col -= 1
            if (board.get_square_info(self._row, col + 1) == BoardInfo.BLACK):
                enemy_in_way = True
        
        enemy_in_way = False
        # row to right
        row = self._row + 1
        while (self.square_available(board.get_square_info(row, self._col)) and not enemy_in_way):
            board_data[row][self._col] = char_label
            row += 1
            if (board.get_square_info(row - 1, self._col) == BoardInfo.BLACK):
                enemy_in_way = True

        enemy_in_way = False
        # row to left
        row = self._row - 1
        while (self.square_available(board.get_square_info(row, self._col)) and not enemy_in_way):
            board_data[row][self._col] = char_label
            row -= 1
            if (board.get_square_info(row + 1, self._col) == BoardInfo.BLACK):
                enemy_in_way = True

        return board_data

# because pawns move in only one direction, the different colors behave differently, unlike other pieces
class WhitePawn(ChessPiece):
    def __init__(self, row_num, col_num, color, label):
        ChessPiece.__init__(self, row_num, col_num, color)
        self.label = label

    def get_label(self):
        return self.label

    def is_legal_move(self, dest_row, dest_col, board):
        """Returns true if this piece can legally move to the specified
        location on the provide board"""
        row_diff = abs(self._row-dest_row)
        col_diff = abs(self._col-dest_col)
        square_type = board.get_square_info(dest_row, dest_col)
        # check pawn moves for legality in its different situations
        if row_diff == 2 and col_diff == 0 and self._row == 1:
            return square_type == BoardInfo.EMPTY
        if row_diff == 1:
            if col_diff == 0:
                return square_type == BoardInfo.EMPTY
            if col_diff == 1:
                return square_type == BoardInfo.BLACK
        return False

    # pawn can more forward one place or two after first move and capture diagonally
    def generate_legal_moves(self, board_data, board):
        """Adds representation for the legal moves to the provided 
        board representation and returns the result"""
        char_label = self.label.value
        board_data[self._row][self._col] = char_label
        square_type = board.get_square_info(self._row + 1, self._col)
        # for first move one place or next moves two places
        if square_type == BoardInfo.EMPTY:
            board_data[self._row + 1][self._col] = char_label
            square_type = board.get_square_info(self._row + 2, self._col)
            if self._row == 1 and square_type == BoardInfo.EMPTY:
                board_data [self._row + 2][self._col] = char_label
        # for pawn capturing to the right or left diagonal
        square_type = board.get_square_info(self._row + 1, self._col + 1)
        if square_type == BoardInfo.BLACK:
            board_data[self._row + 1][self._col + 1] = char_label
        square_type = board.get_square_info(self._row - 1, self._col - 1)
        if square_type == BoardInfo.BLACK:
            board_data[self._row - 1][self._col - 1] = char_label
        return board_data

class Bishop(ChessPiece):
    def __init__(self, row_num, col_num, color, label):
        ChessPiece.__init__(self, row_num, col_num, color)
        self.label = label

    def get_label(self):
        return self.label

    def is_legal_move(self, dest_row, dest_col, board):
        """Returns true if this piece can legally move to the specified
        location on the provide board"""
        row_diff = abs(self._row-dest_row)
        col_diff = abs(self._col-dest_col)
        square_type = board.get_square_info(dest_row, dest_col)
        # return true or false for is legal move for all 4 cases
        # row diff to equal col diff for bishop moves
        block = False
        if row_diff == col_diff:
            if row_diff > 0:
                for x in range(1,row_diff):
                    square_type = board.get_square_info(self._row + x, self._col + x)
                    if not self.square_available(square_type):
                        block = True
                    if square_type == BoardInfo.BLACK and x <= row_diff + 1:
                        block = True
                
            if row_diff < 0:
                for x in range(1,row_diff):
                    square_type = board.get_square_info(self._row - x, self._col - x)
                    if not self.square_available(square_type):
                        block = True
                    if square_type == BoardInfo.BLACK and x <= row_diff + 1:
                        block = True
                
        if row_diff > col_diff:
            for x in range(1,row_diff):
                    square_type = board.get_square_info(self._row + x, self._col - x)
                    if not self.square_available(square_type):
                        block = True
                    if square_type == BoardInfo.BLACK and x <= row_diff + 1:
                        block = True
            
        elif row_diff < col_diff:
            for x in range(1,row_diff):
                    square_type = board.get_square_info(self._row - x, self._col + x)
                    if not self.square_available(square_type):
                        block = True
                    if square_type == BoardInfo.BLACK and x <= row_diff + 1:
                        block = True
            
        is_legal = (row_diff == col_diff) and square_type != self._color and square_type != BoardInfo.OFF_THE_BOARD 
                    # and block != True)
        return is_legal

    def generate_legal_moves(self, board_data, board):
        """Adds representation for the legal moves to the provided 
        board representation and returns the result"""
        char_label = self.label.value
        board_data[self._row][self._col] = char_label
        # check for enemies
        enemy_in_way = False
        # right diagonal up
        col = self._col + 1
        row = self._row - 1
        while (self.square_available(board.get_square_info(row, col)) and not enemy_in_way):
            board_data[row][col] = char_label
            col += 1
            row -= 1
            if (board.get_square_info(row + 1, col - 1) == BoardInfo.BLACK):
                enemy_in_way = True

        enemy_in_way = False
        # left diagonal down
        col = self._col - 1
        row = self._row + 1
        while (self.square_available(board.get_square_info(row, col)) and not enemy_in_way):
            board_data[row][col] = char_label
            col -= 1
            row += 1
            if (board.get_square_info(row - 1, col + 1) == BoardInfo.BLACK):
                enemy_in_way = True
        
        enemy_in_way = False
        # left diagonal up
        row = self._row - 1
        col = self._col - 1
        while (self.square_available(board.get_square_info(row, col)) and not enemy_in_way):
            board_data[row][col] = char_label
            row -= 1
            col -= 1
            if (board.get_square_info(row + 1, col + 1) == BoardInfo.BLACK):
                enemy_in_way = True

        enemy_in_way = False
        # right diagonal down
        row = self._row + 1
        col = self._col + 1
        while (self.square_available(board.get_square_info(row, col)) and not enemy_in_way):
            board_data[row][col] = char_label
            row += 1
            col += 1
            if (board.get_square_info(row - 1, col - 1) == BoardInfo.BLACK):
                enemy_in_way = True

        return board_data

# Queen moves like a rook and a bishop combined
class Queen(ChessPiece):
    def __init__(self, row_num, col_num, color, label):
        ChessPiece.__init__(self, row_num, col_num, color)
        self.label = label

    def get_label(self):
        return self.label

    def is_legal_move(self, dest_row, dest_col, board):
        """Returns true if this piece can legally move to the specified
        location on the provide board"""
        row_diff = abs(self._row-dest_row)
        col_diff = abs(self._col-dest_col)
        square_type = board.get_square_info(dest_row, dest_col)

        is_legal = (row_diff == col_diff or row_diff == 0 and col_diff < 9 or row_diff < 9 and col_diff ==
                    0) and square_type != self._color and square_type != BoardInfo.OFF_THE_BOARD
        return is_legal

    # Queen is essentially the same as the bishop and rook moves combined, why not just reuse them 
    def generate_legal_moves(self, board_data, board):
        """Adds representation for the legal moves to the provided 
        board representation and returns the result"""
        char_label = self.label.value
        board_data[self._row][self._col] = char_label
        board_data = (Bishop.generate_legal_moves(self, board_data, board) 
                      and Rook.generate_legal_moves(self, board_data, board))
        return board_data
