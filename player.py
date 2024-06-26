"""
Programme python de la classe Player
Auteurs : Thomas BOTTALICO, Rayane BOUSSOURA, Alexandre BRENSKI, Arthur HACQUES, Tess POIRAT, Adrien RIVET
Version : 1.1
"""


"""IMPORT DES LIBRAIRIES ET DES FONCTIONS EXTERNES"""

import pygame # import de la librairie pygame pour gérer le jeu
from missile import Missile # import de la classe Missile depuis missile.py


"""CORPS DU PROGRAMME"""

# classe qui gère le joueur
class Player(pygame.sprite.Sprite) :

    def __init__(self, game) :
        super().__init__()
        self.game = game
        self.health = 100   # définir les points de vie du joueur
        self.max_health = 100 # définir les points de vie max du joueur
        self.all_missiles = pygame.sprite.Group()   # définir le groupe de missiles
        self.image = pygame.transform.scale(pygame.image.load("assets/boat.png"), (200, 200))   # redimensionner l'image en 200x200 et affecter l'image

    # fonction des dégats
    def damage(self):
        if self.health - 10 > 10 :   # si la vie du jeu est > 10 pdv
            self.health -= 10   # enlever 10 pdv au joueur
        else:
            self.game.game_over()   # passer en mode game over

    # fonction de la barre de pdv
    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (60, 63, 60), [250, 400, self.max_health, 5])   # dessiner la barre de vie initiale
        pygame.draw.rect(surface, (111, 210, 46), [250, 400, self.health, 5])   # dessiner la barre de vie

    # fonction du lancement des missiles
    def launch_missile(self) :
        self.all_missiles.add(Missile(self))   # créer une nouvelle instance de la classe Missile