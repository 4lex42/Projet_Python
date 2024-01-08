import unittest
from unittest.mock import patch
from io import StringIO

import pygame

from chess_board import ChessBoard
from chess_game import ChessGame


class TestChessGame(unittest.TestCase):
    @patch('builtins.input', return_value='1')  # Mocking user input for testing
    def test_game_initialization(self, mock_input):
        game = ChessGame()

        self.assertIsInstance(game.window, pygame.Surface)
        self.assertIsInstance(game.board, ChessBoard)
        self.assertEqual(game.current_player, "A")

    @patch('builtins.input', return_value='1')  # Mocking user input for testing
    @patch('sys.stdout', new_callable=StringIO)  # Redirecting stdout for testing
    def test_draw_game(self, mock_stdout, mock_input):
        game = ChessGame()
        game.draw_game()

        # Check if any errors were printed to stdout during drawing
        self.assertEqual(mock_stdout.getvalue(), "")

    @patch('builtins.input', return_value='1')  # Mocking user input for testing
    @patch('sys.stdout', new_callable=StringIO)  # Redirecting stdout for testing
    def test_draw_sidebar(self, mock_stdout, mock_input):
        game = ChessGame()
        game.draw_sidebar()

        # Check if any errors were printed to stdout during drawing the sidebar
        self.assertEqual(mock_stdout.getvalue(), "")

    @patch('builtins.input', return_value='1')  # Mocking user input for testing
    def test_switch_player_turn(self, mock_input):
        game = ChessGame()
        initial_player = game.current_player

        game.switch_player_turn()
        new_player = game.current_player

        # Check if the player turn has switched
        self.assertNotEqual(initial_player, new_player)

    @patch('builtins.input', side_effect=['1'])  # Mocking input to simulate user input
    @patch('sys.stdout', new_callable=StringIO)  # Redirecting stdout for testing
    def test_run_with_mouse_input(self, mock_stdout, mock_input):
        game = ChessGame()
        game.run()

        self.assertEqual(mock_stdout.getvalue(), "")