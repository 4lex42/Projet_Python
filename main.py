import pygame
import sys

# Initialisation de Pygame
pygame.init()
icon = pygame.image.load("./assets/icon.png")
pygame.display.set_caption("Jeu Loufoque")
pygame.display.set_icon(icon)

# Définir les dimensions de la fenêtre
largeur, hauteur = 800, 800
fenetre = pygame.display.set_mode((largeur, hauteur))

# Définir les couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROSE = (255, 105, 180)

# Définir la taille de la case et la marge
TAILLE_CASE = 100
MARGE = 50

# Charger les images des pions
pion_rond = pygame.image.load("img/pion_rond.png")
pion_triangle = pygame.image.load("img/pion_triangle.png")

# Créer une liste pour les positions et types de pions
pions = [
    {"image": pion_rond, "position": (0, i)} for i in range(8)  # Première ligne pour les pions ronds
] + [
    {"image": pion_rond, "position": (1, i)} for i in range(8)  # Deuxième ligne pour les pions ronds
] + [
    {"image": pion_triangle, "position": (6, i)} for i in range(8)  # Avant-dernière ligne pour les pions triangulaires
] + [
    {"image": pion_triangle, "position": (7, i)} for i in range(8)  # Dernière ligne pour les pions triangulaires
]


# Fonction pour dessiner le plateau
def dessiner_plateau():
    for i in range(8):
        for j in range(8):
            couleur = BLANC if (i + j) % 2 == 0 else NOIR
            pygame.draw.rect(fenetre, couleur, (j * TAILLE_CASE, i * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE))


# Fonction pour dessiner les pions
def dessiner_pions():
    for pion in pions:
        x = pion["position"][1] * TAILLE_CASE + MARGE - 50 + (TAILLE_CASE - pion["image"].get_width()) // 2
        y = pion["position"][0] * TAILLE_CASE + MARGE - 50 + (TAILLE_CASE - pion["image"].get_height()) // 2
        fenetre.blit(pion["image"], (x, y))


# Boucle principale du jeu
en_cours = True
pion_selectionne = None

while en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            for pion in pions:
                rect = pion["image"].get_rect(topleft=(pion["position"][1] * TAILLE_CASE + MARGE - 50,
                                                       pion["position"][0] * TAILLE_CASE + MARGE - 50))
                expanded_rect = rect.inflate(100, 100)  # Augmente la zone de détection du clic
                if expanded_rect.collidepoint(x, y):
                    pion_selectionne = pion
                    break
        elif event.type == pygame.MOUSEBUTTONUP:
            if pion_selectionne:
                x, y = pygame.mouse.get_pos()
                x -= MARGE - 50
                y -= MARGE - 50
                pion_selectionne["position"] = (y // TAILLE_CASE, x // TAILLE_CASE)  # Inverse les coordonnées
            pion_selectionne = None

    # Effacer l'écran
    fenetre.fill(BLANC)

    # Dessiner le plateau et les pions
    dessiner_plateau()
    dessiner_pions()

    # Mettre à jour l'affichage
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
sys.exit()
