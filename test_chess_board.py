import unittest
from unittest.mock import Mock

import pygame

from chess_board import ChessBoard


class TestChessBoard(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.window = pygame.display.set_mode((800, 800))
        self.chess_board = ChessBoard(self.window)

    def tearDown(self):
        pygame.quit()

    def test_chess_board_initialization(self):
        self.assertEqual(self.chess_board.window, self.window)
        self.assertEqual(len(self.chess_board.pieces), 32)

    def test_add_piece(self):
        piece = Mock()
        self.chess_board.add_piece(piece)
        self.assertIn(piece, self.chess_board.pieces)

    def test_remove_piece(self):
        piece = Mock()
        self.chess_board.add_piece(piece)
        self.chess_board.remove_piece(piece)
        self.assertNotIn(piece, self.chess_board.pieces)

    def test_draw_board(self):
        # This test assumes that the draw_board method doesn't raise any exceptions
        self.chess_board.draw_board()

    def test_draw_pieces(self):
        # This test assumes that the draw_pieces method doesn't raise any exceptions
        self.chess_board.draw_pieces()

    def test_get_all_pieces(self):
        pieces = self.chess_board.get_all_pieces()
        self.assertEqual(len(pieces), 32)

    def test_shuffle_pieces(self):
        original_positions = [piece.position for piece in self.chess_board.get_all_pieces()]
        self.chess_board.shuffle_pieces()
        new_positions = [piece.position for piece in self.chess_board.get_all_pieces()]

        # Verify that the positions are shuffled
        self.assertNotEqual(original_positions, new_positions)

    def test_transform_random_piece_in_queen(self):
        # This test assumes that the transform_random_piece_in_queen method doesn't raise any exceptions
        self.chess_board.transform_random_piece_in_queen()

    # Add more test cases to cover different scenarios and behaviors


if __name__ == '__main__':
    unittest.main()
