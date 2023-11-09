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
tour = pygame.image.load("img/tour.png")
tour = pygame.transform.scale(tour, (80, 80))

pion = pygame.image.load("img/pion.png")
pion = pygame.transform.scale(pion, (80, 80))

roi = pygame.image.load("img/roi.png")
roi = pygame.transform.scale(roi, (80, 80))

reine = pygame.image.load("img/reine.png")
reine = pygame.transform.scale(reine, (80, 80))

fou = pygame.image.load("img/fou.png")
fou = pygame.transform.scale(fou, (80, 80))

cavalier = pygame.image.load("img/cavalier.png")
cavalier = pygame.transform.scale(cavalier, (80, 80))

# Créer une liste pour les positions et types de pions
pions = pions = [
    {"image": roi, "position": (0, 4)},
    {"image": reine, "position": (0, 3)},
    {"image": fou, "position": (0, 2)},
    {"image": fou, "position": (0, 5)},
    {"image": cavalier, "position": (0, 1)},
    {"image": cavalier, "position": (0, 6)},
    {"image": tour, "position": (0, 0)},
    {"image": tour, "position": (0, 7)}
    ] + [
    {"image": pion, "position": (1, i)} for i in range(8)
] + [
    {"image": tour, "position": (7, 0)},
    {"image": cavalier, "position": (7, 1)},
    {"image": fou, "position": (7, 2)},
    {"image": reine, "position": (7, 3)},
    {"image": roi, "position": (7, 4)},
    {"image": fou, "position": (7, 5)},
    {"image": cavalier, "position": (7, 6)},
    {"image": tour, "position": (7, 7)}
] + [
    {"image": pion, "position": (6, i)} for i in range(8)
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
                center_x = pion["position"][1] * TAILLE_CASE + MARGE - 50 + TAILLE_CASE / 2
                center_y = pion["position"][0] * TAILLE_CASE + MARGE - 50 + TAILLE_CASE / 2

                distance = ((x - center_x) ** 2 + (y - center_y) ** 2) ** 0.5

                if distance <= TAILLE_CASE / 2:
                    pion_selectionne = pion
                    break
        elif event.type == pygame.MOUSEBUTTONUP:
            if pion_selectionne:
                 x, y = pygame.mouse.get_pos()
                 x -= MARGE - 50
                 y -= MARGE - 50
                 nouvelle_position = (y // TAILLE_CASE, x // TAILLE_CASE)

                 # Check if there's already a piece at the target position
                 piece_existante = next((p for p in pions if p["position"] == nouvelle_position), None)

                 if piece_existante:
                      # Remove the existing piece
                      pions.remove(piece_existante)

                 pion_selectionne["position"] = nouvelle_position  # Update the position
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
