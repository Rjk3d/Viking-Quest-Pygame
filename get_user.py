import pyautogui
from main import main_menu
from menu_mini_jeu import menu_mini_jeu
import pygame
import pygame.freetype
import ast

def get_image(path):
    """
    La fonction get_image a pour objectif de charger un sprite_sheet de personnage à partir d'un chemin d'accès et de renvoyer uniquement l'image du personnage de face.

Paramètres:

    path (str): Le chemin d'accès au sprite_sheet du personnage.
Comportement:

    La fonction vérifie que le paramètre path est une chaîne de caractères (str) se terminant par ".png". Si cette condition n'est pas satisfaite, une assertion est levée.
    Elle charge le sprite_sheet du personnage à partir du chemin d'accès fourni à l'aide de la fonction pygame.image.load.
    La fonction crée une surface image de taille (32, 32) et y copie uniquement la partie du sprite_sheet correspondant à l'image du personnage de face (position (32, 0) avec une taille de (32, 32)).
    L'image est redimensionnée à une taille de (80, 80) à l'aide de pygame.transform.scale.
    La couleur (0, 0, 0) est définie comme couleur transparente (set_colorkey([0, 0, 0])).
    La fonction renvoie l'image ainsi obtenue.
Exceptions:

    Une assertion est utilisée pour vérifier que le paramètre path est une chaîne de caractères (str) se terminant par ".png". Si cette condition n'est pas satisfaite, une assertion est levée.
Dépendances:

    La fonction dépend du module Pygame pour charger et manipuler des images.
Utilisation:

    La fonction est utilisée lorsque vous avez besoin de récupérer l'image de face d'un personnage à partir de son sprite_sheet.
    """
    assert path[-4:] == '.png' and type(path) == str, "path doit être un string qui finit par .png"
    sprite_sheet = pygame.image.load(path)  # "visual/perso_mec/mec1.png"
    image = pygame.Surface([32, 32])
    image.blit(sprite_sheet, (0, 0), (32, 0, 32, 32))
    image = pygame.transform.scale(image, (80, 80))
    image.set_colorkey([0, 0, 0])
    return image


def unlock(skin):
    """
    La fonction unlock a pour objectif de déverrouiller un skin spécifié dans le jeu en mettant à jour la sauvegarde actuelle stockée dans le fichier "sauvegarde.txt".

Paramètres:

    skin (str): Le nom du skin à déverrouiller.
Comportement:

    1°La fonction ouvre le fichier "sauvegarde.txt" en mode lecture ("r").
    2°Elle parcourt le contenu du fichier ligne par ligne pour charger la sauvegarde actuelle sous forme de dictionnaire à l'aide de la fonction ast.literal_eval.
    3°La fonction vérifie que le paramètre skin est de type chaîne de caractères (str). Si ce n'est pas le cas, une assertion est levée.
    4°Elle modifie le dictionnaire pour déverrouiller le skin spécifié en mettant à jour la valeur associée à la clé correspondante dans la structure de données.
    5°La sauvegarde modifiée est convertie en chaîne de caractères.
    6°La fonction ouvre à nouveau le fichier "sauvegarde.txt", mais cette fois-ci en mode écriture ("w").
    7°Elle réécrit la sauvegarde modifiée dans le fichier "sauvegarde.txt", remplaçant ainsi l'ancienne sauvegarde.
    8°La fonction se termine.
Exceptions:

    Une assertion est utilisée pour vérifier que le type du paramètre skin est une chaîne de caractères (str). Si ce n'est pas le cas, une assertion est levée.
Dépendances:

    La fonction utilise le module ast pour évaluer la représentation littérale de la sauvegarde sous forme de dictionnaire.
    La fonction dépend du fichier "sauvegarde.txt" pour charger la sauvegarde actuelle et y écrire les modifications.
Utilisation:

    La fonction est appelée lorsqu'il est nécessaire de déverrouiller un skin spécifique dans le jeu, par exemple, après qu'un utilisateur a effectué un achat réussi.
Préconditions:

    Assurez-vous que le fichier "sauvegarde.txt" existe et contient une sauvegarde au format correct.
    Assurez-vous que le paramètre skin est une chaîne de caractères représentant le nom du skin que vous souhaitez déverrouiller.
Postconditions:

    Le fichier "sauvegarde.txt" est mis à jour avec la sauvegarde modifiée, déverrouillant ainsi le skin spécifié.
    """
    assert type(skin)==str,"skin doit être un string"
    with open("sauvegarde.txt", "r") as fichier:
        for elem in fichier:
            dict = ast.literal_eval(elem)
            dict["User1"]["skin"][skin] = True

    a = str(dict)
    with open("sauvegarde.txt", "w") as fichier:
        fichier.write(a)


def achat_skin(solde,mode,a_unlock="mec1",nv_perso="visual/perso_mec/mec2.png"):
    """
Description :
    La fonction achat_skin est utilisée pour gérer l'achat d'un skin dans le jeu. Elle affiche une boîte de dialogue demandant à l'utilisateur s'il souhaite acheter un skin non débloqué pour 10 gemmes. Si l'utilisateur accepte et a suffisamment de gemmes, le skin est débloqué et le solde est mis à jour.

Paramètres :
    solde : Le solde actuel du joueur.
    mode : Le mode de jeu en cours (peut être "h" pour histoire ou "mj" pour mini-jeu).
    a_unlock : Le skin à débloquer (par défaut, "mec1").
    nv_perso : L'image du nouveau personnage (par défaut, "visual/perso_mec/mec2.png").
Préconditions :
    Les fichiers de sauvegarde (sauvegarde.txt) et de skins (skin.txt) doivent exister et contenir des données valides.
Effets :
    Affiche une boîte de dialogue demandant à l'utilisateur s'il veut acheter un skin non débloqué.
    Si l'utilisateur accepte et a suffisamment de gemmes, le skin est débloqué, le solde est mis à jour, et le fichier de sauvegarde est modifié.
    Si l'utilisateur n'a pas suffisamment de gemmes, une alerte est affichée.
Postconditions :
    Le skin est débloqué et le solde est mis à jour si l'utilisateur a accepté l'achat et a suffisamment de gemmes.
    Une alerte est affichée si l'utilisateur n'a pas suffisamment de gemmes.
    """
    a = pyautogui.confirm("Vous ne l'avez pas débloqué, Voulez-vous l'acheter pour 10 gemmes?",
                          buttons=["Oui", "Non"])
    if a == "Oui":
        if int(solde) >= 10:  # vérification du solde
            with open("sauvegarde.txt", "r") as fichier:
                for elem in fichier:
                    dict = ast.literal_eval(elem)
            solde -= 10
            dict["User1"]["Solde"] = str(solde)
            a = str(dict)
            with open("sauvegarde.txt", "w") as fichier:  # réécrit le fichier en enlevant 10 au solde
                fichier.write(a)
            unlock(a_unlock)
            with open("skin.txt", "w") as file:
                file.write(nv_perso)
                file.close()
                if mode == "h":
                    main_menu(deb=False)
                elif mode == "mj":
                    menu_mini_jeu()
        else:
            pyautogui.alert("Vous n'avez pas assez de gemmes")



def get_user(mode="h"):
    """
    La fonction get_user est responsable de l'affichage d'un menu permettant à l'utilisateur de choisir un skin pour son personnage. Elle prend en compte le mode de jeu ("h" pour l'histoire ou "mj" pour le mini-jeu) pour permettre le retour au menu approprié après la sélection du skin. La fonction affiche les skins disponibles, vérifie s'ils sont débloqués, empêche l'accès à ceux qui sont bloqués, et permet l'achat de nouveaux skins.

Paramètres:

    mode (optionnel, str): Le mode de jeu, par défaut "h" (histoire). Peut être "h" pour le mode histoire ou "mj" pour le mini-jeu. Utilisé pour retourner au bon menu après la sélection du skin.
Comportement:

    1°La fonction utilise la bibliothèque Pygame pour créer une interface graphique.
    2°Elle charge les visuels nécessaires, tels que les images de fond, les chaînes de texte, et les images des skins masculins et féminins.
    3°Les skins sont affichés sur l'écran, et un cadenas est superposé s'ils ne sont pas débloqués.
    4°La fonction détecte les clics de l'utilisateur sur les images des skins et effectue les actions appropriées.
        °Si un skin débloqué est cliqué, le fichier "skin.txt" est mis à jour avec le nouveau chemin d'image, et l'utilisateur est renvoyé au menu principal (main_menu) ou au menu du mini-jeu (menu_mini_jeu) en fonction du mode.
        °Si un skin non débloqué est cliqué, un message d'alerte est affiché.
    5°La fonction gère également les clics sur les boutons d'achat (achat), permettant à l'utilisateur d'acheter des skins débloqués pour 10 gemmes, en vérifiant d'abord si l'utilisateur a suffisamment de gemmes.
Retour:

    La fonction n'a pas de valeur de retour explicite. Elle gère l'interface utilisateur et les interactions avec les skins.
Exceptions:

    Si le mode fourni n'est ni "h" ni "mj", la fonction lève une assertion indiquant que le mode doit être soit "h" (histoire) soit "mj" (mini-jeu).
Dépendances:

    La fonction dépend de fichiers externes tels que "sauvegarde.txt" pour récupérer le solde des gemmes et "skin.txt" pour mettre à jour le chemin d'image du skin.
Utilisation:

    La fonction est exécutée si le script est exécuté en tant que programme principal (__name__ == '__main__'). Elle peut également être appelée directement si nécessaire.
    """
    assert mode == "mj" or mode == "h", "mode doit être mj(mini jeu) ou h (histoire)"  # sert à savoir d'où l'on vient pour retourner au même endroit après le choix
    pygame.init()

    #récupère le solde dans le fichier sauvegarde
    with open("sauvegarde.txt", "r") as fichier:
        for elem in fichier:
            dict = ast.literal_eval(elem)
    dico_skin = dict["User1"]["skin"]

    #######Importation de tout les visuels et paramétrage de la page
    screen = pygame.display.set_mode((1280, 720))
    GAME_FONT = pygame.freetype.Font("for_construction/font.ttf", 24)

    bg = pygame.image.load("visual/menu_background2.jpg")
    bg = pygame.transform.scale(bg, (1280, 720))#redonne le bon format à l'image

    cadena = pygame.image.load("visual/cadena.jpg")
    cadena = pygame.transform.scale(cadena, (50, 50))
    cadena.set_colorkey([255, 255, 255])#enlève le fond blanc

    gemme = pygame.image.load("visual/gem.png")
    gemme = pygame.transform.scale(gemme, (30, 30))

    #récupère le solde dans le fichier sauvegarde
    with open("sauvegarde.txt", "r") as fichier:
        for elem in fichier:
            dict = ast.literal_eval(elem)
            solde = int(dict["User1"]["Solde"])

    text_solde, rect = GAME_FONT.render(str(solde), (255, 255, 255))

    ar_menu = pygame.image.load("visual/ar_menu.png")  # 585*427
    ar_menu.set_colorkey([255, 255, 255])

    txt_skin_mec, rect = GAME_FONT.render("Garçons:", (255, 255, 255))
    txt_skin_meuf, rect = GAME_FONT.render("Filles:", (255, 255, 255))

    txt_menu_skin, rect = GAME_FONT.render("CHOISISSEZ UN SKIN (en cliquant dessus)", (255, 255, 255))

    #création de la liste images_mecs avec le path pour tout les skin de garcon
    images_mecs = []
    for i in range(1, 5):
        path = f"visual/perso_mec/mec{i}.png"
        images_mecs.append(get_image(path))

    # création de la liste images_meufs avec le path pour tout les skin de fille
    images_meufs = []
    for i in range(1, 6):
        path = f"visual/perso_meuf/meuf{i}.png"
        images_meufs.append(get_image(path))

    pygame.display.set_caption("Choisissez un skin")

    run = True
    while run:
        # affichage de tout les visuels importé ci-dessus
        screen.blit(bg, (0, 0))
        screen.blit(ar_menu, ((1280 - 585) / 2, (720 - 427) / 2))

        screen.blit(text_solde, (1250 - list(text_solde.get_rect())[-2], 10))
        screen.blit(gemme, (1250, 5))

        screen.blit(txt_menu_skin, ((1280 - list(txt_menu_skin.get_rect())[-2]) / 2, 10))

        screen.blit(txt_skin_mec, (560, 190))
        screen.blit(txt_skin_meuf, (560, 360))

        #affiche l'image des skins et un cadena dessus si ils ne sont pas dévérouillé
        for i in range(4):
            screen.blit(images_mecs[i], (420 + i * 120, 240))
            if dico_skin[f"mec{i}"] == False:
                screen.blit(cadena, (435 + i * 120, 255))

        #même chose pour les skins des filles
        for i in range(5):
            screen.blit(images_meufs[i], (400 + i * 100, 440))
            if dico_skin[f"meuf{i}"] == False:
                screen.blit(cadena, (415 + i * 100, 455))

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                #gère le clics sur chaque image (répétitif mais les clics ne marchait pas dans un for, il fallait spammer pour tomber pile au moment ou il lancait la bonne vérification)
                if 420 <= event.pos[0] <= 500 and 240 <= event.pos[1] <= 320:
                    if dico_skin["mec0"] == True:
                        with open("skin.txt", "w") as file:
                            file.write("visual/perso_mec/mec1.png")
                            file.close()
                            if mode == "h":
                                main_menu(deb=False)
                            elif mode == "mj":
                                menu_mini_jeu()
                    else:
                        pyautogui.alert("Vous ne l'avez pas débloqué")
                if 540 <= event.pos[0] <= 620 and 240 <= event.pos[1] <= 320:
                    if dico_skin["mec1"] == True:
                        with open("skin.txt", "w") as file:
                            file.write("visual/perso_mec/mec2.png")
                            file.close()
                            if mode == "h":
                                main_menu(deb=False)
                            elif mode == "mj":
                                menu_mini_jeu()
                    else:#gestion de l'achat (A METTRE DANS UNE FONCTION POUR EVITER LES copié-collé)
                        achat_skin(solde,mode,a_unlock="mec1", nv_perso="visual/perso_mec/mec2.png")

                #toujours pareil pour chaque image car impossible de faire un for
                if 660 <= event.pos[0] <= 740 and 240 <= event.pos[1] <= 320:
                    if dico_skin["mec2"] == True:
                        with open("skin.txt", "w") as file:
                            file.write("visual/perso_mec/mec3.png")
                            file.close()
                            if mode == "h":
                                main_menu(deb=False)
                            elif mode == "mj":
                                menu_mini_jeu()
                    else:
                        achat_skin(solde, mode, a_unlock="mec2", nv_perso="visual/perso_mec/mec3.png")

                if 780 <= event.pos[0] <= 860 and 240 <= event.pos[1] <= 320:
                    if dico_skin["mec3"] == True:
                        with open("skin.txt", "w") as file:
                            file.write("visual/perso_mec/mec4.png")
                            file.close()
                            if mode == "h":
                                main_menu(deb=False)
                            elif mode == "mj":
                                menu_mini_jeu()
                    else:
                        achat_skin(solde, mode, a_unlock="mec3", nv_perso="visual/perso_mec/mec4.png")

                if 400 <= event.pos[0] <= 480 and 440 <= event.pos[1] <= 520:
                    if dico_skin["meuf0"] == True:
                        with open("skin.txt", "w") as file:
                            file.write("visual/perso_meuf/meuf1.png")
                            file.close()
                            if mode == "h":
                                main_menu(deb=False)
                            elif mode == "mj":
                                menu_mini_jeu()
                    else:
                        achat_skin(solde, mode, a_unlock="meuf0", nv_perso="visual/perso_meuf/meuf1.png")

                if 500 <= event.pos[0] <= 580 and 440 <= event.pos[1] <= 520:
                    if dico_skin["meuf1"] == True:
                        with open("skin.txt", "w") as file:
                            file.write("visual/perso_meuf/meuf2.png")
                            file.close()
                            if mode == "h":
                                main_menu(deb=False)
                            elif mode == "mj":
                                menu_mini_jeu()
                    else:
                        achat_skin(solde, mode, a_unlock="meuf1", nv_perso="visual/perso_meuf/meuf2.png")


                if 600 <= event.pos[0] <= 680 and 440 <= event.pos[1] <= 520:
                    if dico_skin["meuf2"] == True:
                        with open("skin.txt", "w") as file:
                            file.write("visual/perso_meuf/meuf3.png")
                            file.close()
                            if mode == "h":
                                main_menu(deb=False)
                            elif mode == "mj":
                                menu_mini_jeu()
                    else:
                        achat_skin(solde, mode, a_unlock="meuf2", nv_perso="visual/perso_meuf/meuf3.png")


                if 700 <= event.pos[0] <= 780 and 440 <= event.pos[1] <= 520:
                    if dico_skin["meuf3"] == True:
                        with open("skin.txt", "w") as file:
                            file.write("visual/perso_meuf/meuf4.png")
                            file.close()
                            if mode == "h":
                                main_menu(deb=False)
                            elif mode == "mj":
                                menu_mini_jeu()
                    else:
                        achat_skin(solde, mode, a_unlock="meuf3", nv_perso="visual/perso_meuf/meuf4.png")

                if 800 <= event.pos[0] <= 880 and 440 <= event.pos[1] <= 520:
                    if dico_skin["meuf4"] == True:
                        with open("skin.txt", "w") as file:
                            file.write("visual/perso_meuf/meuf5.png")
                            file.close()
                            if mode == "h":
                                main_menu(deb=False)
                            elif mode == "mj":
                                menu_mini_jeu()
                    else:
                        achat_skin(solde, mode, a_unlock="meuf4", nv_perso="visual/perso_meuf/meuf5.png")

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        pygame.display.update()
    pygame.quit()

if __name__ == '__main__':
    get_user()
