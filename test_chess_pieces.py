import unittest

from unittest.mock import Mock  # Utiliser Mock pour simuler les dépendances externes comme pygame

from chess_pieces import ChessPiece, Pawn


class TestChessPiece(unittest.TestCase):
    def setUp(self):
        # Initialisation des objets communs pour les tests
        self.mock_image = Mock()
        self.mock_board = Mock()
        self.mock_board.get_all_pieces.return_value = []

    def test_chess_piece_initialization(self):
        piece = ChessPiece(self.mock_image, (0, 0), "A")
        self.assertEqual(piece.image, self.mock_image)
        self.assertEqual(piece.position, (0, 0))
        self.assertEqual(piece.color, "A")

    def test_chess_piece_click_inside_piece(self):
        piece = ChessPiece(self.mock_image, (1, 1), "B")
        # On suppose TILE_SIZE = 50, MARGIN = 10 pour simplifier
        self.assertTrue(piece.click_inside_piece(35, 35))  # Inside the piece
        self.assertFalse(piece.click_inside_piece(10, 10))  # Outside the piece

    def test_chess_piece_move_valid(self):
        piece = ChessPiece(self.mock_image, (2, 2), "A")
        self.assertTrue(piece.move((3, 2), self.mock_board))
        self.assertEqual(piece.position, (3, 2))

    def test_chess_piece_move_invalid_same_color(self):
        piece1 = ChessPiece(self.mock_image, (2, 2), "A")
        piece2 = ChessPiece(self.mock_image, (3, 2), "A")
        self.mock_board.get_all_pieces.return_value = [piece2]
        self.assertFalse(piece1.move((3, 2), self.mock_board))
        self.assertEqual(piece1.position, (2, 2))

    def test_chess_piece_move_remove_opponent_piece(self):
        piece1 = ChessPiece(self.mock_image, (2, 2), "A")
        piece2 = ChessPiece(self.mock_image, (3, 2), "B")
        self.mock_board.get_all_pieces.return_value = [piece2]
        self.assertTrue(piece1.move((3, 2), self.mock_board))
        self.assertEqual(piece1.position, (3, 2))
        self.assertNotIn(piece2, self.mock_board.pieces)


class TestPawn(unittest.TestCase):
    def setUp(self):
        self.mock_image = Mock()
        self.mock_board = Mock()
        self.mock_board.get_all_pieces.return_value = []

    def test_pawn_initialization(self):
        pawn = Pawn(self.mock_image, (0, 0), "A")
        self.assertEqual(pawn.image, self.mock_image)
        self.assertEqual(pawn.position, (0, 0))
        self.assertEqual(pawn.color, "A")
        self.assertTrue(pawn.initial_double_move_allowed)

    def test_pawn_move_valid(self):
        pawn = Pawn(self.mock_image, (1, 1), "A")
        self.assertTrue(pawn.move((2, 1), self.mock_board))
        self.assertEqual(pawn.position, (2, 1))
        self.assertFalse(pawn.initial_double_move_allowed)


if __name__ == '__main__':
    unittest.main()
