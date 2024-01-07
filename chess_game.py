# chess_game.py
import sys

import pygame

from chess_board import ChessBoard
from constants import WHITE, WIDTH, HEIGHT, TILE_SIZE, MARGIN, SIDEBAR_WIDTH, GREEN


class ChessGame:
    def __init__(self):
        self.window = pygame.display.set_mode((WIDTH + SIDEBAR_WIDTH, HEIGHT))
        self.board = ChessBoard(self.window)
        self.current_player = "A"

    def draw_game(self):
        # Clear the window
        self.window.fill(WHITE)

        # Draw the board
        self.board.draw_board()

        # Draw the pieces
        self.board.draw_pieces()

        # Draw the sidebar
        self.draw_sidebar()

        # Update the display
        pygame.display.flip()

    def draw_sidebar(self):
        # Draw the sidebar
        pygame.draw.rect(self.window, (100, 100, 100), (WIDTH, 0, SIDEBAR_WIDTH, HEIGHT))

        # Display player A's name with color based on turn
        player_a_color = GREEN if self.current_player == "A" else WHITE
        font_a = pygame.font.Font(None, 36)
        text_a = font_a.render("Player A", True, player_a_color)
        self.window.blit(text_a, ((WIDTH + 10), 90))

        # Display player B's name with color based on turn
        player_b_color = GREEN if self.current_player == "B" else WHITE
        font_b = pygame.font.Font(None, 36)
        text_b = font_b.render("Player B", True, player_b_color)
        self.window.blit(text_b, ((WIDTH + 10), 690))

    def switch_player_turn(self):
        # Switch the current player's turn
        self.current_player = "B" if self.current_player == "A" else "A"

    def run(self):
        # Dessiner le jeu des le lancement
        self.draw_game()

        en_cours = True
        pion_selectionne = None  # stocker la piece selectionnee

        jouabilite = 0
        while jouabilite != "2" and jouabilite != "1":
            jouabilite = input("Choisissez votre mode de jouabilité, tapez le numéro 1 (Souris) ou 2 (Terminal) :")

        if jouabilite == "1":  # souris
            while en_cours:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        en_cours = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        x, y = pygame.mouse.get_pos()
                        for piece in self.board.pieces:
                            if piece.color == self.current_player and piece.click_inside_piece(x, y):
                                # Only allow pieces of the current player to be selected
                                pion_selectionne = piece
                                break
                    elif event.type == pygame.MOUSEBUTTONUP:
                        if pion_selectionne:
                            x, y = pygame.mouse.get_pos()
                            x -= MARGIN - 50
                            y -= MARGIN - 50
                            nouvelle_position = (y // TILE_SIZE, x // TILE_SIZE)

                            # Move the piece if the move is valid
                            if pion_selectionne.move(nouvelle_position, self.board):
                                # Switch the player turn after the move
                                self.switch_player_turn()

                            # Update the display after moving the piece
                            self.draw_game()

                            pion_selectionne = None

        elif jouabilite == "2":  # CLI
            while en_cours:
                # Demande à l'utilisateur de fournir la position de la pièce à déplacer
                user_input = input("Entrez la position de la pièce à déplacer (ligne colonne) : ")

                # Convertit la saisie de l'utilisateur en une paire de coordonnées (ligne, colonne)
                coordonnees = user_input.split()  # Sépare la saisie en une liste de valeurs
                ligne = int(coordonnees[0])  # Prend la première valeur comme numéro de ligne
                colonne = int(coordonnees[1])  # Prend la deuxième valeur comme numéro de colonne
                position = (ligne, colonne)  # Crée un tuple avec les coordonnées (ligne, colonne)

                # Recherche de la pièce à la position spécifiée dans la liste des pièces sur l'échiquier
                selected_piece = None
                for piece in self.board.pieces:
                    if piece.position == position:  # Vérifie si la position de la pièce correspond à la saisie de l'utilisateur
                        selected_piece = piece  # Si la pièce est trouvée, elle est assignée à selected_piece
                        break  # Arrête la recherche dès qu'une pièce est trouvée

                if selected_piece:  # Vérifie si une pièce a été trouvée à la position spécifiée
                    # Demande à l'utilisateur de fournir la nouvelle position pour déplacer la pièce
                    new_position_input = input("Entrez la nouvelle position (ligne colonne) : ")

                    # Converti la nouvelle saisie de l'utilisateur en une paire de coordonnées (ligne, colonne)
                    new_coordonnees = new_position_input.split()  # Sépare la nouvelle saisie en une liste de valeurs
                    new_ligne = int(new_coordonnees[0])  # Prend la première valeur comme nouveau numéro de ligne
                    new_colonne = int(new_coordonnees[1])  # Prend la deuxième valeur comme nouveau numéro de colonne
                    new_position = (
                        new_ligne, new_colonne)  # Crée un tuple avec les nouvelles coordonnées (ligne, colonne)

                    if selected_piece:
                        for piece in self.board.pieces:
                            if piece.position == new_position:
                                self.board.pieces.remove(piece)
                                break

                    # Met à jour la position de la pièce sélectionnée avec la nouvelle position fournie par l'utilisateur
                    selected_piece.position = new_position

                # Effacer l'écran et rafraichissement
                self.window.fill(WHITE)
                self.board.draw_board()
                self.board.draw_pieces()  # Appel pour dessiner les pièces
                pygame.display.flip()

            """command = input("Entrez la position de la pièce à déplacer (ligne colonne) : ")
            position = tuple(map(int, command.split()))  # Convertit la saisie en coordonnées (ligne, colonne)

            # Recherche de la pièce à la position spécifiée
            selected_piece = None
            for piece in self.board.pieces:
                if piece.position == position:
                    selected_piece = piece
                    break

            if selected_piece:
                new_position = input("Entrez la nouvelle position (ligne colonne) : ")
                new_position = tuple(map(int, new_position.split()))  # Nouvelle position de la pièce
                selected_piece.position = new_position  # Met à jour la position de la pièce"""

        pygame.quit()
        sys.exit()
