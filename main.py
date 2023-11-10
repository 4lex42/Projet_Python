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

# Définir la taille de la case et la marge
TAILLE_CASE = 100
MARGE = 50

# Charger les images des pions
tour = pygame.image.load("assets/tour.png")
tour = pygame.transform.scale(tour, (80, 80))

pion = pygame.image.load("assets/pion.png")
pion = pygame.transform.scale(pion, (80, 80))

roi = pygame.image.load("assets/roi.png")
roi = pygame.transform.scale(roi, (80, 80))

reine = pygame.image.load("assets/reine.png")
reine = pygame.transform.scale(reine, (80, 80))

fou = pygame.image.load("assets/fou.png")
fou = pygame.transform.scale(fou, (80, 80))

cavalier = pygame.image.load("assets/cavalier.png")
cavalier = pygame.transform.scale(cavalier, (80, 80))

# Créer une liste pour les positions et types de pions
pions = [
    {"image": roi, "position": (0, 4), "joueur": 1},
    {"image": reine, "position": (0, 3), "joueur": 1},
    {"image": fou, "position": (0, 2), "joueur": 1},
    {"image": fou, "position": (0, 5), "joueur": 1},
    {"image": cavalier, "position": (0, 1), "joueur": 1},
    {"image": cavalier, "position": (0, 6), "joueur": 1},
    {"image": tour, "position": (0, 0), "joueur": 1},
    {"image": tour, "position": (0, 7), "joueur": 1}
] + [
    {"image": pion, "position": (1, i), "joueur": 1} for i in range(8)
] + [
    {"image": tour, "position": (7, 0), "joueur": 2},
    {"image": cavalier, "position": (7, 1), "joueur": 2},
    {"image": fou, "position": (7, 2), "joueur": 2},
    {"image": reine, "position": (7, 3), "joueur": 2},
    {"image": roi, "position": (7, 4), "joueur": 2},
    {"image": fou, "position": (7, 5), "joueur": 2},
    {"image": cavalier, "position": (7, 6), "joueur": 2},
    {"image": tour, "position": (7, 7), "joueur": 2}
] + [
    {"image": pion, "position": (6, i), "joueur": 2} for i in range(8)
]

# Position dans le plateau
def is_outside(pos):
    return all(0 <= coord < 8 for coord in pos)

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

# Fonction pour gérer le déplacement d'une pièce
def deplacer_piece():
    global pion_selectionne, joueur_actuel
    x, y = pygame.mouse.get_pos()
    x -= MARGE - 50
    y -= MARGE - 50
    nouvelle_position = (y // TAILLE_CASE, x // TAILLE_CASE)

    if is_outside(nouvelle_position):
        piece_existante = next((p for p in pions if p["position"] == nouvelle_position), None)
        if piece_existante and piece_existante != pion_selectionne:
            pions.remove(piece_existante)

        pion_selectionne["position"] = nouvelle_position  # Update the position

        return True  # Indique un déplacement réussi

    return False  # Indique un déplacement échoué



# Boucle principale du jeu
en_cours = True
joueur_actuel = 1  # Initialisez à 1 pour le premier joueur
pion_selectionne = None

clock = pygame.time.Clock()  # Ajoutez une horloge pour contrôler le taux de rafraîchissement

while en_cours:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Vérifiez que le clic gauche est utilisé
                for pion in pions:
                    # Ajoutez une vérification pour s'assurer que le joueur sélectionne sa propre pièce
                    if pion["joueur"] == joueur_actuel:
                        center_x = pion["position"][1] * TAILLE_CASE + MARGE - 50 + TAILLE_CASE / 2
                        center_y = pion["position"][0] * TAILLE_CASE + MARGE - 50 + TAILLE_CASE / 2

                        distance = ((event.pos[0] - center_x) ** 2 + (event.pos[1] - center_y) ** 2) ** 0.5

                        if distance <= TAILLE_CASE / 2:
                            pion_selectionne = pion
                            break
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and pion_selectionne:  # Vérifiez le bouton de la souris
                deplacement_reussi = deplacer_piece()

                if deplacement_reussi:
                    # Si le déplacement a réussi, changez de joueur
                    joueur_actuel = 3 - joueur_actuel  # Alterner entre les joueurs 1 et 2
                pion_selectionne = None  # Réinitialisez la pièce sélectionnée après le déplacement

    # Effacer l'écran
    fenetre.fill(BLANC)

    # Dessiner le plateau et les pions
    dessiner_plateau()
    dessiner_pions()

    # Mettre à jour l'affichage
    pygame.display.flip()

    # Contrôler le taux de rafraîchissement
    clock.tick(30)  # 30 images par seconde (ajustez selon vos besoins)

# Quitter Pygame
pygame.quit()
sys.exit()
