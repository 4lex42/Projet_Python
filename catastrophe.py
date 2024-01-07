# catastrophe.py
class Catastrophe:
    def __init__(self, name):
        """
        PRE : name est une chaîne de caractères représentant le nom de la catastrophe.
        """
        self.name = name

    def trigger(self, board):
        """
        PRE : board est une instance de ChessBoard représentant l'échiquier.
        POST : Affiche un message indiquant que l'événement de catastrophe a été déclenché.
        """
        print(f"{self.name} event has been triggered!")


class Storm(Catastrophe):
    def __init__(self):
        super().__init__("Storm")

    def trigger(self, board):
        """
        PRE : board est une instance de ChessBoard représentant l'échiquier.
        POST : Affiche un message indiquant que l'événement de tempête a été déclenché.
               Mélange les positions de toutes les pièces sur l'échiquier.
        """
        super().trigger(board)
        board.shuffle_pieces()


class Transformation(Catastrophe):
    def __init__(self):
        super().__init__("Transformation")

    def trigger(self, board):
        """
        PRE : board est une instance de ChessBoard représentant l'échiquier.
        POST : Affiche un message indiquant que l'événement de transformation a été déclenché.
               Transforme une pièce aléatoire en une reine.
        """
        super().trigger(board)
        board.transform_random_piece_in_queen()
