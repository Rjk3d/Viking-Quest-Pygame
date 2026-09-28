import pygame
import random
import ast
from pygame.locals import *
import pygame.freetype
from player import Player

pygame.init()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
GAME_FONT = pygame.freetype.Font("for_construction/font.ttf", 24)
pygame.display.set_caption("Jeu de météores")

class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.original_image = pygame.image.load("visual/projectile.png")
        self.original_image = pygame.transform.scale(self.original_image,(30,30))
        self.image=self.original_image
        self.rect = self.image.get_rect()
        self.gauche_ou_haut = random.randint(0, 1)
        if self.gauche_ou_haut==1:
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randint(-100, -40)
            self.speedy = random.randint(5, 7)
        else:
            self.rect.x = random.randint(-100, -40)
            self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)
            self.speedy = random.randint(5, 7)
        self.rotation_angle = 0

    def update(self):
        """
Description :
    La fonction update est utilisée pour mettre à jour la position et l'orientation d'un objet, dans le jeu.

Fonctionnalités :
    Déplace l'objet vers le bas ou vers la droite en fonction de la valeur de l'attribut gauche_ou_haut.
    Gère le déplacement en boucle de l'objet lorsqu'il atteint le bord de l'écran.
    Met à jour l'angle de rotation de l'objet et applique une rotation à l'image.
Préconditions :
    Les attributs rect, speedy, rotation_angle, image, et original_image doivent être correctement initialisés avant d'appeler cette fonction.
    SCREEN_HEIGHT et SCREEN_WIDTH doivent représenter les dimensions de l'écran de jeu.
Effets :
    Modifie la position de l'objet en fonction de sa vitesse verticale (speedy) ou horizontale.
    Gère le redémarrage de la position de l'objet lorsqu'il atteint le bord de l'écran.
    Met à jour l'angle de rotation de l'objet et applique une rotation à l'image.
        """
        if self.gauche_ou_haut==1:
            self.rect.y += self.speedy
            if self.rect.top > SCREEN_HEIGHT:
                self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
                self.rect.y = random.randint(-100, -40)
                self.speedy = random.randint(3, 10)
        else:
            self.rect.x += self.speedy
            if self.rect.left > SCREEN_WIDTH:
                self.rect.x = 10
                self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)
                self.speedy = random.randint(3, 10)
        self.rotation_angle = (self.rotation_angle + 5) % 360
        self.image = pygame.transform.rotate(self.original_image, self.rotation_angle)


class mini_jeu1:
    def __init__(self,user="User1"):
        pygame.mixer.music.unload()
        pygame.mixer.quit()
        pygame.mixer.init()
        pygame.mixer.music.load("sound/mj1.wav")
        pygame.mixer.music.set_volume(0.7)
        pygame.mixer.music.play(-1)

        self.user=user
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Mini jeu 1")
        self.all_sprites = pygame.sprite.Group()
        self.meteors = pygame.sprite.Group()
        with open("skin.txt", "r") as f:
            for l in f:
                skin = l

        self.player = Player(600,500,taille=2.5,speed=6,skin=skin)
        self.all_sprites.add(self.player)
        self.lst_time_init = []

        self.img_menu = pygame.image.load("visual/img_menu.png")
        self.img_menu = pygame.transform.scale(self.img_menu, (60, 60))
        self.img_fond = pygame.image.load("visual/fond_mini_jeu.jpeg")
        self.img_fond = pygame.transform.scale(self.img_fond, (1280, 720))

        self.meteor_add = False

        with open("sauvegarde.txt", "r") as fichier:
            for elem in fichier:
                dict = ast.literal_eval(elem)
                self.solde = int(dict[self.user]["Solde"])
                self.niv_taille = int(dict[self.user]["niv_taille"])

        self.text_solde, rect = GAME_FONT.render(str(self.solde), (255, 255, 255))
        gemme = pygame.image.load("visual/gem.png")
        self.gemme = pygame.transform.scale(gemme, (30, 30))

        self.nbr_meteor=3

        for _ in range(self.nbr_meteor):
            meteor = Meteor()
            self.all_sprites.add(meteor)
            self.meteors.add(meteor)
        pygame.init()

    def handle_input(self):
        """
Description :
    La fonction handle_input est utilisée pour gérer les entrées de l'utilisateur liées aux mouvements du joueur. Elle appelle les fonctions de déplacement du joueur en fonction des touches pressées et gère l'inversion des touches pour le monde 6.

Préconditions :
    La fonction doit être appelée dans la boucle principale du jeu pour détecter les événements liés aux touches.
Paramètres :
    Aucun paramètre explicite n'est passé à cette fonction. Cependant, elle utilise les méthodes de l'objet player pour gérer les mouvements.

Effets :
    Appelle les méthodes de déplacement du joueur (move_up, move_down, move_left, move_right) en fonction des touches pressées.
    Appelle la méthode change_animation pour mettre à jour l'animation du joueur en fonction de la direction du mouvement.
Postconditions :
    Les mouvements du joueur sont gérés en fonction des touches pressées.
        """
        pressed = pygame.key.get_pressed()

        if pressed[K_UP] and self.player.get_pos()[1] > 0 or pressed[K_z] and self.player.get_pos()[1] > 0:
            self.player.move_up()
            self.player.change_animation('up')
        elif pressed[K_DOWN] and self.player.get_pos()[1] < 660 or pressed[K_s] and self.player.get_pos()[1] < 660:
                self.player.move_down()
                self.player.change_animation('down')
        elif pressed[K_LEFT] and self.player.get_pos()[0]>0 or pressed[K_q] and self.player.get_pos()[0]>0:
            self.player.move_left()
            self.player.change_animation('left')
        elif pressed[K_RIGHT] and self.player.get_pos()[0] < 1245 or pressed[K_d] and self.player.get_pos()[0] < 1245:
            self.player.move_right()
            self.player.change_animation('right')

    def add_solde(self,a_ajoute):
        """
Description :
    La fonction add_solde est utilisée pour ajouter une quantité spécifiée au solde associé à un utilisateur dans le fichier de sauvegarde.

Paramètres :
    a_ajoute : La quantité à ajouter au solde existant.
Préconditions :
    Le fichier de sauvegarde (sauvegarde.txt) doit exister et contenir les données attendues au bon format (utilisé le fichier init.py si c'est pas bon)
Effets :
    Lit le fichier de sauvegarde pour récupérer les données actuelles.
    Ajoute la quantité spécifiée au solde associé à l'utilisateur.
    Met à jour le fichier de sauvegarde avec la nouvelle valeur de solde.
    Met à jour l'attribut solde de l'instance de la classe.
    Met à jour l'attribut text_solde pour refléter la nouvelle valeur de solde.
    Active le marqueur a_ete_ajoute pour indiquer que l'ajout a été effectué et ne le faire qu'une fois par seconde.
Postconditions :
    Le solde associé à l'utilisateur est mis à jour dans le fichier de sauvegarde.
    Les attributs solde, text_solde, et a_ete_ajoute sont mis à jour.
        """
        with open("sauvegarde.txt", "r") as fichier:
            for elem in fichier:
                dict = ast.literal_eval(elem)
                self.solde += a_ajoute
                dict[self.user]["Solde"] = self.solde

        dict[self.user]["Solde"] = str(self.solde)
        a = str(dict)
        with open("sauvegarde.txt", "w") as fichier:
            fichier.write(a)
        self.solde = int(dict[self.user]["Solde"])
        self.text_solde, rect = GAME_FONT.render(str(self.solde), (255, 255, 255))
        self.a_ete_ajoute=True#permet de l'ajouter qu'une seule fois

    def temps(self):
        """
Description :
    La fonction temps est utilisée pour créer et afficher un chronomètre dans le jeu. Elle ajoute également périodiquement une gemme au solde du joueur et gère l'apparition de météores à des intervalles spécifiques.

Préconditions :
    La police GAME_FONT doit être définie avant d'appeler cette fonction.
Effets :
    Initialise le temps de départ si la liste lst_time_init est vide.
    Calcule le temps écoulé depuis le début du jeu.
    Affiche le temps écoulé à l'écran à l'aide de la police GAME_FONT.
    Ajoute 1 gemme au solde toutes les 20 secondes.
    Ajoute un météore toutes les 7 secondes.
    Gère l'ajout de météores à des intervalles spécifiques.
Postconditions :
    Le temps écoulé est affiché à l'écran.
    Des gemmes sont ajoutées au solde du joueur à des intervalles spécifiques.
    Des météores sont ajoutés au jeu à des intervalles spécifiques.
        """
        if len(self.lst_time_init)==0:
            self.lst_time_init.append(int(pygame.time.get_ticks()/1000))
        temps = 0
        temps = temps + int(int(pygame.time.get_ticks()/1000)-self.lst_time_init[0])
        text_temps, rect = GAME_FONT.render(str(temps),(255,163,26))
        self.screen.blit(text_temps, (70, 15))
        if temps%30==0 and temps>0 and self.a_ete_ajoute==False:
            self.add_solde(int(temps/30))
        if temps % 31 == 0:
            self.a_ete_ajoute=False
        if temps%7==0 and temps>0 and self.meteor_add==False:
            meteor = Meteor()
            self.nbr_meteor+=1
            self.all_sprites.add(meteor)
            self.meteors.add(meteor)
            self.meteor_add=True
        if temps % 8 == 0 and temps%56!=0:
            self.meteor_add=False

    def run(self):
        """
Description :
    La fonction run constitue la boucle principale du jeu. Elle gère les événements Pygame, les entrées utilisateur, la mise à jour des sprites, l'affichage des éléments graphiques, la collision avec les météores, l'affichage du solde, et la gestion du temps.

Préconditions :
    Les sprites, les images, la musique, et les polices nécessaires doivent être correctement initialisés avant d'appeler cette fonction.
Effets :
    Gère les événements Pygame, tels que la fermeture de fenêtre et les clics de souris.
    Appelle la fonction handle_input pour gérer les entrées utilisateur.
    Met à jour les sprites avec la méthode update.
    Affiche les éléments graphiques à l'écran.
    Gère la collision du joueur avec les météores.
    Affiche le solde du joueur à l'écran.
    Gère le temps dans le jeu avec la fonction temps.
Postconditions :
    La boucle principale du jeu fonctionne jusqu'à ce que l'utilisateur quitte le jeu ou ferme la fenêtre.
    Les événements, les entrées utilisateur, les collisions, et les mises à jour sont gérés conformément au code de la fonction.
        """
        running = True
        clock = pygame.time.Clock()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
            self.handle_input()

            self.all_sprites.update()
            self.screen.blit(self.img_fond, (0, 0))
            self.screen.blit(self.img_menu, (1, 1))
            self.screen.blit(self.text_solde, (1250 - list(self.text_solde.get_rect())[-2], 10))
            self.screen.blit(self.gemme, (1250, 5))

            hits = pygame.sprite.spritecollide(self.player, self.meteors, False)
            if hits:
                pygame.mixer.music.stop()
                import menu_mini_jeu as mmj
                mmj.menu_mini_jeu(deb=True)

            self.all_sprites.draw(self.screen)
            self.temps()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 1 <= event.pos[0] <= 60 and 1 <= event.pos[1] <= 60:
                        pygame.mixer.music.stop()
                        import main
                        main.main_menu(user=self.user)

                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    quit()

            clock.tick(60)

if __name__=='__main__':
    game1 = mini_jeu1()
    game1.run()