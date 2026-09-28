# ⚔️ Viking Quest — *The Impossible (casse pas ton écran)*

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![Pygame](https://img.shields.io/badge/Pygame-2.x-green)
![Tiled](https://img.shields.io/badge/Maps-Tiled-orange)

Jeu d'aventure/labyrinthe en 2D développé en **Python avec Pygame**, réalisé dans le cadre du projet de NSI en Terminale par **Maxime Sempels** et **Ilès Said Ouamar**.

<!-- Ajoute ici une capture d'écran ou un GIF du jeu, par ex. : ![Aperçu](docs/apercu.gif) -->

## Fonctionnalités

- **Mode histoire** : 2 mondes de 6 niveaux, jouables en parallèle, avec des pièges qui se corsent au fil des niveaux (murs invisibles, limite de temps, obscurité, totems à retrouver…)
- **Mini-jeux** accessibles depuis un menu dédié
- **Système de gemmes** gagnées en réussissant les niveaux
- **Boutique de skins** : personnages à débloquer avec les gemmes
- **Amélioration** : réduction de la taille du personnage pour faciliter les passages étroits
- **Sauvegarde** automatique de la progression
- Cartes conçues avec [Tiled](https://www.mapeditor.org/), musiques et effets sonores

## Installation

Prérequis : Python 3.10+

```bash
git clone https://github.com/Rjk3d/Viking-Quest-Pygame.git
cd Viking-Quest-Pygame
pip install -r requirements.txt
```

Le script `init.py` peut aussi installer les dépendances et réinitialiser la sauvegarde (ou tout débloquer pour tester le jeu rapidement) :

```bash
python init.py
```

## Lancer le jeu

```bash
python main.py
```

N'oubliez pas le son 🔊

## Commandes

| Action | Touches |
|---|---|
| Se déplacer | `Z` `Q` `S` `D` ou flèches directionnelles |
| Menus | Souris |

Dans le menu principal : le bouton en haut à gauche ouvre la personnalisation du skin, celui en dessous bascule entre le mode histoire et les mini-jeux, et la barre en bas (avec les flèches) sert à acheter l'amélioration de taille.

## Structure du projet

```
main.py            Menu principal (point d'entrée)
game.py            Boucle de jeu, niveaux et pièges
player.py          Personnage joueur
animation.py       Animation des sprites
get_user.py        Personnalisation / déblocage des skins
menu_mini_jeu.py   Menu des mini-jeux
mini_jeu1.py       Mini-jeux
mini_jeu2.py
init.py            Installation et réinitialisation de la sauvegarde
cartes/            Cartes Tiled (.tmx) et tilesets
visual/            Images et sprites
sound/             Musiques et effets sonores
```

## Auteurs

- Maxime Sempels
- Ilès Said Ouamar
