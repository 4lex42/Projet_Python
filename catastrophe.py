class Catastrophe:
    def __init__(self, name):
        self.name = name

    def trigger(self, board):
        print(f"{self.name} event has been triggered!")


class Storm(Catastrophe):
    def __init__(self):
        super().__init__("Storm")

    def trigger(self, board):
        super().trigger(board)
        board.shuffle_pieces()


class Transformation(Catastrophe):
    def __init__(self):
        super().__init__("Transformation")

    def trigger(self, board):
        super().trigger(board)
        board.transform_random_piece_in_queen()
