import sys
import subprocess

rep_pack=input("Voulez-vous installer tout les packages nécessaires? y/n")
assert rep_pack=="y" or rep_pack=="Y" or rep_pack=="n" or rep_pack=="N", "vous ne pouvez répondre que par y/Y ou n/N"

if rep_pack=="y" or rep_pack=="Y":
    lst_packages = list((elem for elem in open("requirements.txt", "r")))

    for elem in lst_packages:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', elem.strip("\n")])


rep=input("Tapez 0 pour réinitialisé le jeu pour un nouveau joueur, \n1 pour être full gemmes et pour avoir tout les niveaux niveaux réussis,\n2 pour ne rien faire:\n")
assert rep=="1" or rep=="0" or rep=="2", "Vous ne pouvez répondre que par 0, 1 ou 2"
if rep=="0":
    with open("sauvegarde.txt","w") as file:
        file.write("{'User1': {'Monde1': '0', 'Monde2': '0', 'Solde': '0', 'skin': {'mec0': True, 'mec1': False, 'mec2': False, 'mec3': False, 'meuf0': True, 'meuf1': False, 'meuf2': False, 'meuf3': False, 'meuf4': False}, 'niv_taille': 0, 'niv_taille_deb': 0}, 'Dev': {'Monde1': '6', 'Monde2': '6'}}")
        file.close()

if rep=="1":
    with open("sauvegarde.txt","w") as file:
        file.write("{'User1': {'Monde1': '6', 'Monde2': '6', 'Solde': '10000', 'skin': {'mec0': True, 'mec1': False, 'mec2': False, 'mec3': False, 'meuf0': True, 'meuf1': False, 'meuf2': False, 'meuf3': False, 'meuf4': False}, 'niv_taille': 0, 'niv_taille_deb': 0}, 'Dev': {'Monde1': '6', 'Monde2': '6'}}")
        file.close()



