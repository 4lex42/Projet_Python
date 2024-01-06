# chess_board.py
import pygame

from chess_pieces import ChessPiece
from constants import WHITE, PINK, TILE_SIZE, MARGIN


class ChessBoard:
    def __init__(self, window):
        self.window = window
        self.pieces = []
        self.creer_pieces()

    def creer_pieces(self):
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

        # creer des listes des positions et des listes des images pour les joueurs A et B
        pieces_positions_A = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)]
        pieces_images_A = [tour_image, cavalier_image, fou_image, reine_image, roi_image, fou_image, cavalier_image,
                           tour_image]
        pieces_positions_B = [(7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7)]
        pieces_images_B = [tour_image, cavalier_image, fou_image, reine_image, roi_image, fou_image, cavalier_image,
                           tour_image]

        # Placer les 8 pieces des joueurs A et B
        for i in range(8):
            piece_A = ChessPiece(pieces_images_A[i], pieces_positions_A[i])
            self.ajouter_pion(piece_A)
            piece_B = ChessPiece(pieces_images_B[i], pieces_positions_B[i])
            self.ajouter_pion(piece_B)
        # Placer les pions des joueurs A et B
        for i in range(8):
            pion_A = ChessPiece(pion_image, (1, i))
            self.ajouter_pion(pion_A)
            pion_B = ChessPiece(pion_image, (6, i))
            self.ajouter_pion(pion_B)

    def ajouter_pion(self, piece):
        self.pieces.append(piece)

    def dessiner_plateau(self):
        for i in range(8):
            for j in range(8):
                couleur = WHITE if (i + j) % 2 == 0 else PINK
                pygame.draw.rect(self.window, couleur, (j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    def dessiner_pions(self):
        for piece in self.pieces:
            x = piece.position[1] * TILE_SIZE + MARGIN - 50 + (TILE_SIZE - piece.image.get_width()) // 2
            y = piece.position[0] * TILE_SIZE + MARGIN - 50 + (TILE_SIZE - piece.image.get_height()) // 2
            self.window.blit(piece.image, (x, y))
