# chess_pieces.py
from constants import TILE_SIZE, MARGIN


class ChessPiece:
    def __init__(self, image, position):
        self.image = image
        self.position = position

    def click_inside_piece(self, x, y):
        x_piece = self.position[1] * TILE_SIZE + MARGIN - 50
        y_piece = self.position[0] * TILE_SIZE + MARGIN - 50
        return x_piece <= x <= x_piece + TILE_SIZE and y_piece <= y <= y_piece + TILE_SIZE

    def move(self, new_position):
        # Generic move logic
        self.position = new_position


class Pawn(ChessPiece):
    def __init__(self, image, position):
        super().__init__(image, position)

    def move(self, new_position):
        start_row, start_col = self.position
        row, col = new_position

        # Check if the move is allowed for a pawn
        if (row == start_row + 1) and (col == start_col):
            super().move(new_position)
        else:
            print("Invalid pawn move")


class Rook(ChessPiece):
    def __init__(self, image, position):
        super().__init__(image, position)

    def move(self, new_position):
        start_row, start_col = self.position
        row, col = new_position

        # Check if the move is allowed for a rook (horizontal or vertical movement)
        if (row == start_row or col == start_col):
            super().move(new_position)
        else:
            print("Invalid rook move")


class Knight(ChessPiece):
    def __init__(self, image, position):
        super().__init__(image, position)

    def move(self, new_position):
        start_row, start_col = self.position
        row, col = new_position

        # Check if the move is allowed for a knight (L-shaped movement)
        if ((abs(row - start_row) == 2 and abs(col - start_col) == 1) or
                (abs(row - start_row) == 1 and abs(col - start_col) == 2)):
            super().move(new_position)
        else:
            print("Invalid knight move")


class Bishop(ChessPiece):
    def __init__(self, image, position):
        super().__init__(image, position)

    def move(self, new_position):
        start_row, start_col = self.position
        row, col = new_position

        # Check if the move is allowed for a bishop (diagonal movement)
        if abs(row - start_row) == abs(col - start_col):
            super().move(new_position)
        else:
            print("Invalid bishop move")


class King(ChessPiece):
    def __init__(self, image, position):
        super().__init__(image, position)

    def move(self, new_position):
        start_row, start_col = self.position
        row, col = new_position

        # Check if the move is allowed for a king (one square movement in any direction)
        if abs(row - start_row) <= 1 and abs(col - start_col) <= 1:
            super().move(new_position)
        else:
            print("Invalid king move")


class Queen(ChessPiece):
    def __init__(self, image, position):
        super().__init__(image, position)

    def move(self, new_position):
        start_row, start_col = self.position
        row, col = new_position

        # Check if the move is allowed for a queen (horizontal, vertical, or diagonal movement)
        if (row == start_row or col == start_col or
                abs(row - start_row) == abs(col - start_col)):
            super().move(new_position)
        else:
            print("Invalid queen move")
