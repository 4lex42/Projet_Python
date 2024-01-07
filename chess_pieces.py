# chess_pieces.py
from constants import TILE_SIZE, MARGIN


class ChessPiece:
    def __init__(self, image, position, color):
        """
        PRE : image est une pygame.Surface, position est un tuple de deux entiers représentant (ligne, colonne), color est une chaîne de caractères.
        POST : Initialise un objet ChessPiece avec l'image, la position et la couleur fournies.
        """
        self.image = image
        self.position = position
        self.color = color  # Add a color attribute

    def click_inside_piece(self, x, y):
        """
        PRE : x et y sont des entiers représentant des coordonnées sur la fenêtre.
        POST : Retourne True si les coordonnées fournies sont à l'intérieur des limites de la pièce, sinon False.
        """
        x_piece = self.position[1] * TILE_SIZE + MARGIN - 50
        y_piece = self.position[0] * TILE_SIZE + MARGIN - 50
        return x_piece <= x <= x_piece + TILE_SIZE and y_piece <= y <= y_piece + TILE_SIZE

    def move(self, new_position, board):
        """
        PRE : new_position est un tuple de deux entiers représentant la position cible sur le plateau, board est un objet ChessBoard.
        POST : Déplace la pièce vers la nouvelle position si le mouvement est valide, met à jour le plateau en conséquence, et retourne True.
               Si le mouvement est invalide, retourne False.
        """
        target_piece = None

        for piece in board.get_all_pieces():
            if piece.position == new_position:
                target_piece = piece
                break

        if not target_piece:
            # The destination square is empty
            self.position = new_position
            return True
        elif target_piece.color == self.color:
            # The destination square is occupied by a piece of the same color
            print("Destination square is occupied by a piece of the same color.")
            return False
        else:
            # The destination square is occupied by an opponent's piece
            print(f"Removing opponent's piece: {target_piece.position}, {target_piece.color}")
            board.remove_piece(target_piece)
            self.position = new_position
            return True


class Pawn(ChessPiece):
    def __init__(self, image, position, color):
        """
        PRE : image est une pygame.Surface, position est un tuple de deux entiers représentant (ligne, colonne), color est une chaîne de caractères.
        POST : Initialise un objet Pawn avec l'image, la position, la couleur et un indicateur initial_double_move_allowed.
        """
        super().__init__(image, position, color)
        self.initial_double_move_allowed = True

    def move(self, new_position, board):
        """
        PRE: new_position est un tuple d'entiers (ligne, colonne) représentant la nouvelle position de la pièce.
             board est une instance de ChessBoard représentant l'échiquier.
        POST: La position de la pièce est mise à jour conformément aux règles de déplacement d'un pion.
              Si le premier double mouvement est effectué, initial_double_move_allowed est mis à False.
        """
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
            if super().move(new_position, board):
                self.initial_double_move_allowed = False  # Update the flag after the initial double move
                return True
            else:
                return False
        else:
            print("Invalid pawn move")
            return False


class Rook(ChessPiece):
    def __init__(self, image, position, color):
        """
        PRE : image est une pygame.Surface, position est un tuple de deux entiers représentant (ligne, colonne), color est une chaîne de caractères.
        POST : Initialise un objet Rook avec l'image, la position et la couleur fournies.
        """
        super().__init__(image, position, color)

    def move(self, new_position, board):
        """
        PRE: new_position est un tuple d'entiers (ligne, colonne) représentant la nouvelle position de la pièce.
             board est une instance de ChessBoard représentant l'échiquier.
        POST: La position de la pièce est mise à jour conformément aux règles de déplacement de chaque type de pièce.
        """
        start_row, start_col = self.position
        row, col = new_position

        # Check if the move is allowed for a rook (horizontal or vertical movement)
        if row == start_row or col == start_col:
            return super().move(new_position, board)
        else:
            print("Invalid rook move")
            return False


class Knight(ChessPiece):
    def __init__(self, image, position, color):
        """
        PRE : image est une pygame.Surface, position est un tuple de deux entiers représentant (ligne, colonne), color est une chaîne de caractères.
        POST : Initialise un objet Knight avec l'image, la position et la couleur fournies.
        """
        super().__init__(image, position, color)

    def move(self, new_position, board):
        """
        PRE: new_position est un tuple d'entiers (ligne, colonne) représentant la nouvelle position de la pièce.
             board est une instance de ChessBoard représentant l'échiquier.
        POST: La position de la pièce est mise à jour conformément aux règles de déplacement de chaque type de pièce.
        """
        start_row, start_col = self.position
        row, col = new_position

        # Check if the move is allowed for a knight (L-shaped movement)
        if ((abs(row - start_row) == 2 and abs(col - start_col) == 1) or
                (abs(row - start_row) == 1 and abs(col - start_col) == 2)):
            return super().move(new_position, board)
        else:
            print("Invalid knight move")
            return False


class Bishop(ChessPiece):
    def __init__(self, image, position, color):
        """
        PRE : image est une pygame.Surface, position est un tuple de deux entiers représentant (ligne, colonne), color est une chaîne de caractères.
        POST : Initialise un objet Bishop avec l'image, la position et la couleur fournies.
        """
        super().__init__(image, position, color)

    def move(self, new_position, board):
        """
        PRE: new_position est un tuple d'entiers (ligne, colonne) représentant la nouvelle position de la pièce.
             board est une instance de ChessBoard représentant l'échiquier.
        POST: La position de la pièce est mise à jour conformément aux règles de déplacement de chaque type de pièce.
        """
        start_row, start_col = self.position
        row, col = new_position

        # Check if the move is allowed for a bishop (diagonal movement)
        if abs(row - start_row) == abs(col - start_col):
            return super().move(new_position, board)
        else:
            print("Invalid bishop move")
            return False


class King(ChessPiece):
    def __init__(self, image, position, color):
        """
        PRE : image est une pygame.Surface, position est un tuple de deux entiers représentant (ligne, colonne), color est une chaîne de caractères.
        POST : Initialise un objet King avec l'image, la position et la couleur fournies.
        """
        super().__init__(image, position, color)

    def move(self, new_position, board):
        """
        PRE: new_position est un tuple d'entiers (ligne, colonne) représentant la nouvelle position de la pièce.
             board est une instance de ChessBoard représentant l'échiquier.
        POST: La position de la pièce est mise à jour conformément aux règles de déplacement de chaque type de pièce.
        """
        start_row, start_col = self.position
        row, col = new_position

        # Check if the move is allowed for a king (one square movement in any direction)
        if abs(row - start_row) <= 1 and abs(col - start_col) <= 1:
            return super().move(new_position, board)
        else:
            print("Invalid king move")
            return False


class Queen(ChessPiece):
    def __init__(self, image, position, color):
        """
        PRE : image est une pygame.Surface, position est un tuple de deux entiers représentant (ligne, colonne), color est une chaîne de caractères.
        POST : Initialise un objet Queen avec l'image, la position et la couleur fournies.
        """
        super().__init__(image, position, color)

    def move(self, new_position, board):
        """
        PRE: new_position est un tuple d'entiers (ligne, colonne) représentant la nouvelle position de la pièce.
             board est une instance de ChessBoard représentant l'échiquier.
        POST: La position de la pièce est mise à jour conformément aux règles de déplacement de chaque type de pièce.
        """
        start_row, start_col = self.position
        row, col = new_position

        # Check if the move is allowed for a queen (horizontal, vertical, or diagonal movement)
        if (row == start_row or col == start_col or
                abs(row - start_row) == abs(col - start_col)):
            return super().move(new_position, board)
        else:
            print("Invalid queen move")
            return False
