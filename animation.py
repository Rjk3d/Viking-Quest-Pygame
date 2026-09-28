
import pygame


class AnimateSprite(pygame.sprite.Sprite):
    def __init__(self,skin="visual/perso_mec/mec3.png",taille=1):
        assert taille==2.5 or taille==1 or taille==0.625 or taille==0.75 or taille==0.8125 or taille==0.90625#multiplicateurs de 32 pour rester en nombre entier
        super().__init__()
        self.sprite_sheet = pygame.image.load(skin)
        self.sprite_sheet = pygame.transform.scale(self.sprite_sheet,(self.sprite_sheet.get_size()[0]*taille,self.sprite_sheet.get_size()[1]*taille))
        self.animation_index = 0
        self.images = {
            'down': self.get_images(0,taille),
            'left': self.get_images(32*taille,taille),
            'right': self.get_images(64*taille,taille),
            'up': self.get_images(96*taille,taille)
        }

    def get_image(self, x, y,taille):
        """
Description :
    La fonction get_image est conçue pour extraire une image spécifique à partir d'une feuille de sprites. Elle prend en compte les coordonnées (x, y) de l'image souhaitée et une taille pour permettre le redimensionnement.

Paramètres :
    x : La coordonnée en x de l'image à extraire depuis la feuille de sprites.
    y : La coordonnée en y de l'image à extraire depuis la feuille de sprites.
    taille : La taille pour redimensionner l'image extraite.
Retour :
    Retourne l'image extraite sous forme de surface Pygame.
Préconditions :
    La feuille de sprites (sprite_sheet) doit être correctement définie avant d'appeler cette fonction.
    Les coordonnées (x, y) doivent pointer vers une position valide sur la feuille de sprites.
Postconditions :
    Une surface Pygame représentant l'image extraite est renvoyée.
    L'image conservée peut être redimensionnée selon la valeur de taille.
        """
        image=pygame.Surface([32*taille,32*taille])
        image.blit(self.sprite_sheet,(0, 0), (x, y, 32*taille, 32*taille))#dans sprite_sheet chaque partie qui représente un personnage fait initialement 32 pixels
        return image

    def change_animation(self, name):
        """
Description :
    La fonction change_animation est utilisée pour gérer l'animation de mouvement en alternant entre les trois images d'une même rangée dans la feuille de sprites.

Paramètres :
    name : Le nom de l'animation à changer, correspondant à une clé dans le dictionnaire self.images.
Préconditions :
    La feuille de sprites (sprite_sheet) doit être correctement chargée et les images doivent être préalablement découpées et organisées en dictionnaire (self.images).
    L'animation spécifiée par name doit exister dans le dictionnaire self.images.
    L'attribut animation_index doit être initialisé à 0 avant d'appeler cette fonction.
Effets :
    Modifie l'attribut self.image pour changer l'image affichée à celle de la rangée spécifiée par name et de l'index actuel de l'animation.
    Incrémente l'attribut animation_index.
    Si l'indice dépasse le nombre d'images dans l'animation spécifiée, réinitialise l'indice à 0 pour boucler l'animation.
Postconditions :
    L'image de l'objet est mise à jour pour afficher la prochaine image dans la séquence d'animation spécifiée.
        """
        self.image=self.images[name][self.animation_index]
        self.image.set_colorkey((0,0,0))
        self.animation_index += 1
        if self.animation_index >= len(self.images[name]):
            self.animation_index=0

    def get_images(self, y,taille):
        """
Description :
    La fonction get_images est utilisée pour récupérer la rangée d'images souhaitée d'une feuille de sprites, en spécifiant la coordonnée y de la rangée et une taille pour conserver les changements de dimension.

Paramètres :
    y : La coordonnée y de la rangée d'images souhaitée sur la feuille de sprites.
    taille : Un facteur de taille pour conserver les changements de dimension lors de la récupération des images.
Préconditions :
    La feuille de sprites (sprite_sheet) doit être correctement chargée avant d'appeler cette fonction.
    Les coordonnées (0, y), (32, y), et (64, y) doivent correspondre à une rangée valide sur la feuille de sprites.
Retour :
    Retourne une liste d'images représentant la rangée spécifiée. Chaque image est récupérée en utilisant la fonction get_image.
Postconditions :
    Une liste d'images de la rangée spécifiée est renvoyée, prête à être utilisée pour des animations ou des affichages.
        """
        images=[]
        for i in range (0,3):
            x = i*32*taille
            image=self.get_image(x,y,taille)
            images.append(image)
        return images