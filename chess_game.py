# chess_game.py
import random
import sys

import pygame

from Projet_Python import chess_board
from catastrophe import Transformation, Storm
from chess_board import ChessBoard
from constants import WHITE, WIDTH, HEIGHT, TILE_SIZE, MARGIN, SIDEBAR_WIDTH, GREEN


class ChessGame:
    def __init__(self):
        """
        PRE : Aucun
        POST : Initialise un objet ChessGame avec une fenêtre, un ChessBoard et définit le joueur actuel sur "A".
        RAISE : RuntimeError, Erreur lors de l'initialisation de Pygame.
        """
        try:
            pygame.init()
            self.window = pygame.display.set_mode((WIDTH + SIDEBAR_WIDTH, HEIGHT))
            self.board = ChessBoard(self.window)
            self.current_player = "A"
        except pygame.error as e:
            raise RuntimeError(f"Erreur lors de l'initialisation de Pygame : {e}")

    def draw_game(self):
        """
        PRE : Aucun
        POST : Dessine le jeu d'échecs sur la fenêtre, y compris le plateau, les pièces et la barre latérale.
        RAISE : RuntimeError, Erreur lors du dessin du jeu.
        """
        try:
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
        except pygame.error as e:
            raise RuntimeError(f"Erreur lors du dessin du jeu : {e}")

    def draw_sidebar(self):
        """
        PRE: Aucun
        POST : Dessine la barre latérale sur la fenêtre, affichant les noms des joueurs en fonction du tour actuel.
        RAISE : RuntimeError, Erreur lors du dessin de la barre latérale.
        """
        try:
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
        except pygame.error as e:
            raise RuntimeError(f"Erreur lors du dessin de la barre latérale : {e}")

    def switch_player_turn(self):
        # Switch the current player's turn
        self.current_player = "B" if self.current_player == "A" else "A"

    def display_winner(self, joueur):
        pygame.quit()
        pygame.init()

        # Create a new smaller window
        victory_screen = pygame.display.set_mode((400, 200))
        pygame.display.set_caption("Victoire!")

        font_winner = pygame.font.Font(None, 36)
        text_winner = font_winner.render(f"Le joueur {joueur[0]} a gagné!", True, (0, 0, 0))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            victory_screen.fill((255, 255, 255))
            victory_screen.blit(text_winner, (50, 80))
            pygame.display.flip()

    def run(self):
        """
        PRE : Aucun
        POST : Exécute la boucle du jeu d'échecs, permettant aux joueurs de faire des mouvements soit avec la souris, soit avec l'interface CLI.
        RAISE : RuntimeError, Erreur lors de l'exécution de la boucle du jeu d'échecs.
        """
        try:
            # Dessiner le jeu dès le lancement
            self.draw_game()

            en_cours = True
            pion_selectionne = None  # Stocker la pièce sélectionnée

            jouabilite = 0
            while jouabilite != "2" and jouabilite != "1":
                jouabilite = input("Choisissez votre mode de jouabilité, tapez le numéro 1 (Souris) ou 2 (Terminal) : ")

            if jouabilite == "1":  # Souris
                while en_cours:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            en_cours = False
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            x, y = pygame.mouse.get_pos()
                            for piece in self.board.pieces:
                                try:
                                    if piece.color == self.current_player and piece.click_inside_piece(x, y):
                                        # Autoriser uniquement les pièces du joueur actuel à être sélectionnées
                                        pion_selectionne = piece
                                        break
                                except Exception as e:
                                    raise RuntimeError(f"Erreur lors de la sélection de la pièce : {e}")

                        elif event.type == pygame.MOUSEBUTTONUP:
                            if pion_selectionne:
                                x, y = pygame.mouse.get_pos()
                                x -= MARGIN - 50
                                y -= MARGIN - 50
                                nouvelle_position = (y // TILE_SIZE, x // TILE_SIZE)

                                try:
                                    # Déplacer la pièce si le déplacement est valide
                                    if pion_selectionne.move(nouvelle_position, self.board):
                                        # Changer le tour du joueur après le déplacement
                                        self.switch_player_turn()

                                        # Vérifier s'il y a un événement de catastrophe
                                        if random.random() < 0.05:
                                            # Déclencher un événement de catastrophe aléatoire
                                            random_event = random.choice([Storm(), Transformation()])
                                            random_event.trigger(self.board)

                                    # Mettre à jour l'affichage après le déplacement de la pièce
                                    self.draw_game()

                                    pion_selectionne = None

                                    # Vérification de l'existence du roi dans la liste
                                    king_exists = [isinstance(objet, chess_board.King) for objet in
                                                   self.board.get_all_pieces()]
                                    nombre_de_rois = sum(king_exists)
                                    if nombre_de_rois < 2:
                                        colors_of_king = [objet.color for objet in self.board.get_all_pieces() if
                                                           isinstance(objet, chess_board.King)]
                                        self.display_winner(colors_of_king)

                                except Exception as e:
                                    raise RuntimeError(f"Erreur lors du déplacement de la pièce : {e}")

            elif jouabilite == "2":  # CLI
                while en_cours:
                    saisie_utilisateur = input("Entrez la position de la pièce à déplacer (ligne colonne) : ")

                    try:
                        coordonnees = saisie_utilisateur.split()  # Séparer la saisie en une liste de valeurs
                        ligne = int(coordonnees[0])  # Prendre la première valeur comme numéro de ligne
                        colonne = int(coordonnees[1])  # Prendre la deuxième valeur comme numéro de colonne
                        position = (ligne, colonne)  # Créer un tuple avec les coordonnées (ligne, colonne)
                    except (ValueError, IndexError):
                        print("Format de saisie incorrect. Utilisez le format 'ligne colonne'.")
                        continue

                    pion_selectionne = None
                    for piece in self.board.pieces:
                        try:
                            if piece.position == position:  # Vérifier si la position de la pièce correspond à la saisie de l'utilisateur
                                pion_selectionne = piece  # Si la pièce est trouvée, elle est assignée à pion_selectionne
                                break  # Arrêter la recherche dès qu'une pièce est trouvée
                        except Exception as e:
                            raise RuntimeError(f"Erreur lors de la recherche de la pièce : {e}")

                    if pion_selectionne:
                        nouvelle_position_input = input("Entrez la nouvelle position (ligne colonne) : ")

                        try:
                            nouvelles_coordonnees = nouvelle_position_input.split()  # Séparer la nouvelle saisie en une liste de valeurs
                            nouvelle_ligne = int(
                                nouvelles_coordonnees[0])  # Prendre la première valeur comme nouveau numéro de ligne
                            nouvelle_colonne = int(
                                nouvelles_coordonnees[1])  # Prendre la deuxième valeur comme nouveau numéro de colonne
                            nouvelle_position = (
                                nouvelle_ligne,
                                nouvelle_colonne)  # Créer un tuple avec les nouvelles coordonnées (ligne, colonne)
                        except (ValueError, IndexError):
                            print("Format de saisie incorrect. Utilisez le format 'ligne colonne'.")
                            continue

                        if pion_selectionne:
                            for piece in self.board.pieces:
                                try:
                                    if piece.position == nouvelle_position:
                                        self.board.pieces.remove(piece)
                                        break
                                except Exception as e:
                                    raise RuntimeError(f"Erreur lors de la suppression de la pièce : {e}")

                        try:
                            pion_selectionne.position = nouvelle_position
                        except Exception as e:
                            raise RuntimeError(f"Erreur lors de la mise à jour de la position de la pièce : {e}")

                    try:
                        self.window.fill(WHITE)
                        self.board.draw_board()
                        self.board.draw_pieces()  # Appel pour dessiner les pièces
                        pygame.display.flip()
                    except Exception as e:
                        raise RuntimeError(f"Erreur lors de l'effacement de l'écran et du rafraîchissement : {e}")

                pygame.quit()
                sys.exit()
        except Exception as e:
            raise RuntimeError(f"Erreur lors de l'exécution du jeu d'échecs : {e}")
