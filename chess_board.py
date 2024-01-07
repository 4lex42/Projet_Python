# chess_board.py
import random

import pygame

from chess_pieces import Rook, Knight, Bishop, Queen, King, Pawn
from constants import WHITE, PINK, TILE_SIZE, MARGIN


class ChessBoard:
    def __init__(self, window):
        self.window = window
        self.pieces = []
        self.create_pieces()

    def create_pieces(self):
        # Load images
        pion_image = pygame.image.load("assets/pion.png")
        pion_image = pygame.transform.scale(pion_image, (80, 80))

        roi_image = pygame.image.load("assets/roi.png")
        roi_image = pygame.transform.scale(roi_image, (80, 80))

        reine_image = pygame.image.load("assets/reine.png")
        reine_image = pygame.transform.scale(reine_image, (80, 80))

        tour_image = pygame.image.load("assets/tour.png")
        tour_image = pygame.transform.scale(tour_image, (80, 80))

        fou_image = pygame.image.load("assets/fou.png")
        fou_image = pygame.transform.scale(fou_image, (80, 80))

        cavalier_image = pygame.image.load("assets/cavalier.png")
        cavalier_image = pygame.transform.scale(cavalier_image, (80, 80))

        pieces_images = ["pion", "roi", "reine", "tour", "fou", "cavalier"]

        # creer des listes des positions et des listes des images pour les joueurs A et B
        pieces_positions_a = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)]
        pieces_positions_b = [(7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7)]

        def get_special_pieces_list(positions, color, rotate=False):
            def get_image(image):
                if rotate:
                    image = pygame.transform.rotate(image, 180)
                return image

            return [Rook(get_image(tour_image), positions[0], color),
                    Knight(get_image(cavalier_image), positions[1], color),
                    Bishop(get_image(fou_image), positions[2], color),
                    Queen(get_image(reine_image), positions[3], color),
                    King(get_image(roi_image), positions[4], color),
                    Bishop(get_image(fou_image), positions[5], color),
                    Knight(get_image(cavalier_image), positions[6], color),
                    Rook(get_image(tour_image), positions[7], color)]

        pieces_a = get_special_pieces_list(pieces_positions_a, "A", True)
        pieces_b = get_special_pieces_list(pieces_positions_b, "B")

        # Placer les 8 pieces des joueurs A et B
        for piece_a in pieces_a:
            self.add_piece(piece_a)

        for piece_b in pieces_b:
            self.add_piece(piece_b)

        # Placer les pions des joueurs A et B
        for i in range(8):
            pion_a = Pawn(pygame.transform.rotate(pion_image, 180), (1, i), "A")
            self.add_piece(pion_a)

            pion_b = Pawn(pion_image, (6, i), "B")
            self.add_piece(pion_b)

    def add_piece(self, piece):
        self.pieces.append(piece)

    def remove_piece(self, piece):
        self.pieces.remove(piece)

    def draw_board(self):
        for i in range(8):
            for j in range(8):
                color = WHITE if (i + j) % 2 == 0 else PINK
                pygame.draw.rect(self.window, color, (j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    def draw_pieces(self):
        for piece in self.pieces:
            x = piece.position[1] * TILE_SIZE + MARGIN - 50 + (TILE_SIZE - piece.image.get_width()) // 2
            y = piece.position[0] * TILE_SIZE + MARGIN - 50 + (TILE_SIZE - piece.image.get_height()) // 2
            self.window.blit(piece.image, (x, y))

    def get_all_pieces(self):
        return self.pieces

    def shuffle_pieces(self):
        # Shuffle the positions of each piece on the board
        positions = [(i, j) for i in range(8) for j in range(8)]
        random.shuffle(positions)

        for piece, new_position in zip(self.pieces, positions):
            piece.position = new_position

        print("SUFFLE THE PIECES")
