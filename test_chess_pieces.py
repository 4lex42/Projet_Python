import unittest

import pygame

from chess_board import ChessBoard
from chess_pieces import ChessPiece


class TestChessPiece(unittest.TestCase):

    def setUp(self):
        pygame.init()

    def test_init_valid(self):
        image = pygame.Surface((50, 50))
        position = (1, 2)
        color = "A"
        piece = ChessPiece(image, position, color)
        self.assertEqual(piece.image, image)
        self.assertEqual(piece.position, position)
        self.assertEqual(piece.color, color)

    def test_init_invalid_image(self):
        with self.assertRaises(TypeError):
            ChessPiece("invalid_image", (1, 2), "A")

    def test_init_invalid_position(self):
        with self.assertRaises(TypeError):
            ChessPiece(pygame.Surface((50, 50)), (1, "invalid"), "A")

    def test_init_invalid_color(self):
        with self.assertRaises(TypeError):
            ChessPiece(pygame.Surface((50, 50)), (1, 2), 123)

    def test_click_inside_piece_valid(self):
        image = pygame.Surface((50, 50))
        position = (1, 2)
        color = "A"
        piece = ChessPiece(image, position, color)
        x = 60
        y = 70
        self.assertTrue(piece.click_inside_piece(x, y))

    def test_click_inside_piece_invalid_coordinates(self):
        image = pygame.Surface((50, 50))
        position = (1, 2)
        color = "A"
        piece = ChessPiece(image, position, color)
        x = "invalid"
        y = 70
        with self.assertRaises(TypeError):
            piece.click_inside_piece(x, y)

    def test_move_valid(self):
        image = pygame.Surface((50, 50))
        position = (1, 2)
        color = "A"
        piece = ChessPiece(image, position, color)
        new_position = (3, 2)
        board = ChessBoard(pygame.Surface((100, 100)))
        result = piece.move(new_position, board)
        self.assertTrue(result)
        self.assertEqual(piece.position, new_position)

    def test_move_invalid_position(self):
        image = pygame.Surface((50, 50))
        position = (1, 2)
        color = "A"
        piece = ChessPiece(image, position, color)
        new_position = (8, 2)
        board = ChessBoard(pygame.Surface((100, 100)))
        result = piece.move(new_position, board)
        self.assertFalse(result)
        self.assertEqual(piece.position, position)

    def test_move_invalid_position_same_color(self):
        image = pygame.Surface((50, 50))
        position = (1, 2)
        color = "A"
        piece = ChessPiece(image, position, color)
        new_position = (3, 2)
        board = ChessBoard(pygame.Surface((100, 100)))
        other_piece = ChessPiece(pygame.Surface((50, 50)), new_position, color)
        board.add_piece(other_piece)
        result = piece.move(new_position, board)
        self.assertFalse(result)
        self.assertEqual(piece.position, position)

    def test_move_invalid_position_opponent_piece(self):
        image = pygame.Surface((50, 50))
        position = (1, 2)
        color = "A"
        piece = ChessPiece(image, position, color)
        new_position = (3, 2)
        board = ChessBoard(pygame.Surface((100, 100)))
        opponent_piece = ChessPiece(pygame.Surface((50, 50)), new_position, "B")
        board.add_piece(opponent_piece)
        result = piece.move(new_position, board)
        self.assertTrue(result)
        self.assertEqual(piece.position, new_position)


if __name__ == '__main__':
    unittest.main()
