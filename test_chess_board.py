import unittest

import pygame

from chess_board import ChessBoard
from chess_pieces import Rook, Queen


class TestChessBoard(unittest.TestCase):
    def setUp(self):
        # Initialize a pygame window for testing
        self.window = pygame.Surface((800, 800))
        self.board = ChessBoard(self.window)

    def test_add_piece(self):
        # Test adding a piece to the board
        piece = Rook(pygame.Surface((80, 80)), (0, 0), "A")
        self.board.add_piece(piece)
        self.assertIn(piece, self.board.get_all_pieces())

    def test_remove_piece(self):
        # Test removing a piece from the board
        piece = Rook(pygame.Surface((80, 80)), (0, 0), "A")
        self.board.add_piece(piece)
        self.board.remove_piece(piece)
        self.assertNotIn(piece, self.board.get_all_pieces())

    def test_shuffle_pieces(self):
        # Test shuffling the positions of pieces on the board
        initial_positions = [piece.position for piece in self.board.get_all_pieces()]
        self.board.shuffle_pieces()
        shuffled_positions = [piece.position for piece in self.board.get_all_pieces()]
        self.assertNotEqual(initial_positions, shuffled_positions)

    def test_transform_random_piece_in_queen(self):
        # Test transforming a random piece into a queen
        initial_pieces = self.board.get_all_pieces()
        self.board.transform_random_piece_in_queen()
        new_pieces = self.board.get_all_pieces()

        # Ensure that the number of pieces remains the same
        self.assertEqual(len(initial_pieces), len(new_pieces))

        # Ensure that at least one piece is different after transformation
        self.assertNotEqual(initial_pieces, new_pieces)

        # Ensure that the transformed piece is a Queen
        for piece in new_pieces:
            if piece not in initial_pieces:
                self.assertIsInstance(piece, Queen)


if __name__ == '__main__':
    unittest.main()
