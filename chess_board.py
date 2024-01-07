# chess_board.py
import random

import pygame

from chess_pieces import Rook, Knight, Bishop, Queen, King, Pawn
from constants import WHITE, PINK, TILE_SIZE, MARGIN


class ChessBoard:
    def __init__(self, window):
        """
        PRE : window est une fenêtre pygame.
        POST : Initialise un objet ChessBoard avec une liste vide de pièces et la fenêtre fournie.
        RAISES :
            ValueError: Erreur si la fenêtre n'est pas une instance de pygame.Surface.
            RuntimeError: Erreur lors de l'initialisation du plateau d'échecs.
        """
        try:
            if not isinstance(window, pygame.Surface):
                raise ValueError("La fenêtre doit être une instance de pygame.Surface.")

            self.window = window
            self.pieces = []
            self.create_pieces()
        except Exception as e:
            raise RuntimeError(f"Erreur lors de l'initialisation du plateau d'échecs : {e}")

    def create_pieces(self):
        """
        PRE : Aucun
        POST : Crée et place les pièces d'échecs sur le plateau, y compris les pions, les tours, les cavaliers, les fous, les rois et les reines.
        RAISE :
            RuntimeError: Erreur lors de la création et du placement des pièces d'échecs.
        """
        try:
            # Load images with error handling
            try:
                pion_image = pygame.image.load("assets/pion.png")
                pion_image = pygame.transform.scale(pion_image, (80, 80))
            except pygame.error as e:
                raise RuntimeError(f"Erreur lors du chargement de l'image du pion : {e}")

            try:
                roi_image = pygame.image.load("assets/roi.png")
                roi_image = pygame.transform.scale(roi_image, (80, 80))
            except pygame.error as e:
                raise RuntimeError(f"Erreur lors du chargement de l'image du roi : {e}")

            try:
                reine_image = pygame.image.load("assets/reine.png")
                reine_image = pygame.transform.scale(reine_image, (80, 80))
            except pygame.error as e:
                raise RuntimeError(f"Erreur lors du chargement de l'image de la reine : {e}")

            try:
                tour_image = pygame.image.load("assets/tour.png")
                tour_image = pygame.transform.scale(tour_image, (80, 80))
            except pygame.error as e:
                raise RuntimeError(f"Erreur lors du chargement de l'image de la tour : {e}")

            try:
                fou_image = pygame.image.load("assets/fou.png")
                fou_image = pygame.transform.scale(fou_image, (80, 80))
            except pygame.error as e:
                raise RuntimeError(f"Erreur lors du chargement de l'image du fou : {e}")

            try:
                cavalier_image = pygame.image.load("assets/cavalier.png")
                cavalier_image = pygame.transform.scale(cavalier_image, (80, 80))
            except pygame.error as e:
                raise RuntimeError(f"Erreur lors du chargement de l'image du cavalier : {e}")

            # Create and place pieces
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

            for piece_a in pieces_a:
                self.add_piece(piece_a)

            for piece_b in pieces_b:
                self.add_piece(piece_b)

            for i in range(8):
                pion_a = Pawn(pygame.transform.rotate(pion_image, 180), (1, i), "A")
                self.add_piece(pion_a)

                pion_b = Pawn(pion_image, (6, i), "B")
                self.add_piece(pion_b)

        except Exception as e:
            raise RuntimeError(f"Erreur lors de la création et du placement des pièces d'échecs : {e}")

    def add_piece(self, piece):
        self.pieces.append(piece)

    def remove_piece(self, piece):
        self.pieces.remove(piece)

    def draw_board(self):
        """
        PRE : Aucun
        POST : Dessine le plateau d'échecs sur la fenêtre avec des cases de couleurs alternées.
        RAISE :
            RuntimeError: Erreur lors du dessin du plateau d'échecs.
        """
        try:
            for i in range(8):
                for j in range(8):
                    color = WHITE if (i + j) % 2 == 0 else PINK
                    pygame.draw.rect(self.window, color, (j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        except Exception as e:
            raise RuntimeError(f"Erreur lors du dessin du plateau d'échecs : {e}")

    def draw_pieces(self):
        """
        PRE : Aucun
        POST : Dessine toutes les pièces d'échecs à leurs positions respectives sur la fenêtre.
        RAISE :
            RuntimeError: Erreur lors du dessin des pièces d'échecs.
        """
        try:
            for piece in self.pieces:
                x = piece.position[1] * TILE_SIZE + MARGIN - 50 + (TILE_SIZE - piece.image.get_width()) // 2
                y = piece.position[0] * TILE_SIZE + MARGIN - 50 + (TILE_SIZE - piece.image.get_height()) // 2
                self.window.blit(piece.image, (x, y))
        except Exception as e:
            raise RuntimeError(f"Erreur lors du dessin des pièces d'échecs : {e}")

    def get_all_pieces(self):
        return self.pieces

    def shuffle_pieces(self):
        """
        PRE : Aucun
        POST : Mélange les positions de chaque pièce sur le plateau de manière aléatoire.
        RAISE :
            RuntimeError: Erreur lors du mélange des pièces sur le plateau.
        """
        try:
            positions = [(i, j) for i in range(8) for j in range(8)]
            random.shuffle(positions)

            for piece, new_position in zip(self.pieces, positions):
                piece.position = new_position
        except Exception as e:
            raise RuntimeError(f"Erreur lors du mélange des pièces sur le plateau : {e}")

    def transform_random_piece_in_queen(self):
        """
        PRE : Aucun
        POST : Transforme une pièce sélectionnée au hasard sur le plateau en une Reine.
        RAISE :
            RuntimeError: Erreur lors de la transformation d'une pièce en Reine.
        """
        try:
            pieces = self.get_all_pieces()
            if pieces:
                random_piece = random.choice(pieces)
                index = self.pieces.index(random_piece)

                reine_image = pygame.image.load("assets/reine.png")
                reine_image = pygame.transform.scale(reine_image, (80, 80))

                if random_piece.color == "A":
                    new_queen = Queen(pygame.transform.rotate(reine_image, 180), random_piece.position, random_piece.color)
                else:
                    new_queen = Queen(reine_image, random_piece.position, random_piece.color)

                self.pieces[index] = new_queen
        except Exception as e:
            raise RuntimeError(f"Erreur lors de la transformation d'une pièce en Reine : {e}")
