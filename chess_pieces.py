# chess_pieces.py
from constants import TILE_SIZE, MARGIN


class ChessPiece:
    def __init__(self, image, position, color):
        self.image = image
        self.position = position
        self.color = color  # Add a color attribute

    def click_inside_piece(self, x, y):
        x_piece = self.position[1] * TILE_SIZE + MARGIN - 50
        y_piece = self.position[0] * TILE_SIZE + MARGIN - 50
        return x_piece <= x <= x_piece + TILE_SIZE and y_piece <= y <= y_piece + TILE_SIZE

    def move(self, new_position):
        # Generic move logic
        self.position = new_position


class Pawn(ChessPiece):
    def __init__(self, image, position, color):
        super().__init__(image, position, color)
        self.initial_double_move_allowed = True

    def move(self, new_position, board):
        start_row, start_col = self.position
        row, col = new_position

        # Check if the move is allowed for a pawn
        if (
                (self.color == "A" and row == start_row + 1 and col == start_col) or
                (self.color == "B" and row == start_row - 1 and col == start_col) or
                (
                        self.color == "A" and start_row == 1 and row == start_row + 2 and col == start_col and self.initial_double_move_allowed
                ) or
                (
                        self.color == "B" and start_row == 6 and row == start_row - 2 and col == start_col and self.initial_double_move_allowed
                )
        ):
            # Check if the destination square is empty
            if not any(piece.position == new_position for piece in board.get_all_pieces() if
                       piece.color == self.color):
                super().move(new_position)
                self.initial_double_move_allowed = False  # Update the flag after the initial double move
            else:
                print("Destination square is occupied by a piece of the same color.")
        else:
            print("Invalid pawn move")


class Rook(ChessPiece):
    def __init__(self, image, position, color):
        super().__init__(image, position, color)

    def move(self, new_position, board):
        start_row, start_col = self.position
        row, col = new_position

        # Check if the move is allowed for a rook (horizontal or vertical movement)
        if (row == start_row or col == start_col):
            # Check if the destination square is empty
            if not any(piece.position == new_position for piece in board.get_all_pieces() if
                       piece.color == self.color):
                super().move(new_position)
            else:
                print("Destination square is occupied by a piece of the same color.")
        else:
            print("Invalid rook move")


class Knight(ChessPiece):
    def __init__(self, image, position, color):
        super().__init__(image, position, color)

    def move(self, new_position, board):
        start_row, start_col = self.position
        row, col = new_position

        # Check if the move is allowed for a knight (L-shaped movement)
        if ((abs(row - start_row) == 2 and abs(col - start_col) == 1) or
                (abs(row - start_row) == 1 and abs(col - start_col) == 2)):
            # Check if the destination square is empty
            if not any(piece.position == new_position for piece in board.get_all_pieces() if
                       piece.color == self.color):
                super().move(new_position)
            else:
                print("Destination square is occupied by a piece of the same color.")
        else:
            print("Invalid knight move")


class Bishop(ChessPiece):
    def __init__(self, image, position, color):
        super().__init__(image, position, color)

    def move(self, new_position, board):
        start_row, start_col = self.position
        row, col = new_position

        # Check if the move is allowed for a bishop (diagonal movement)
        if abs(row - start_row) == abs(col - start_col):
            # Check if the destination square is empty
            if not any(piece.position == new_position for piece in board.get_all_pieces() if
                       piece.color == self.color):
                super().move(new_position)
            else:
                print("Destination square is occupied by a piece of the same color.")
        else:
            print("Invalid bishop move")


class King(ChessPiece):
    def __init__(self, image, position, color):
        super().__init__(image, position, color)

    def move(self, new_position, board):
        start_row, start_col = self.position
        row, col = new_position

        # Check if the move is allowed for a king (one square movement in any direction)
        if abs(row - start_row) <= 1 and abs(col - start_col) <= 1:
            # Check if the destination square is empty
            if not any(piece.position == new_position for piece in board.get_all_pieces() if
                       piece.color == self.color):
                super().move(new_position)
            else:
                print("Destination square is occupied by a piece of the same color.")
        else:
            print("Invalid king move")


class Queen(ChessPiece):
    def __init__(self, image, position, color):
        super().__init__(image, position, color)

    def move(self, new_position, board):
        start_row, start_col = self.position
        row, col = new_position

        # Check if the move is allowed for a queen (horizontal, vertical, or diagonal movement)
        if (row == start_row or col == start_col or
                abs(row - start_row) == abs(col - start_col)):
            # Check if the destination square is empty
            if not any(piece.position == new_position for piece in board.get_all_pieces() if
                       piece.color == self.color):
                super().move(new_position)
            else:
                print("Destination square is occupied by a piece of the same color.")
        else:
            print("Invalid queen move")
