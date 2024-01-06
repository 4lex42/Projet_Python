# main.py
import pygame

from chess_game import ChessGame

if __name__ == "__main__":
    pygame.init()
    icon = pygame.image.load("./assets/icon.png")
    pygame.display.set_caption("Jeu Loufoque")
    pygame.display.set_icon(icon)

    game = ChessGame()
    game.run()
