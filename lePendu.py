import random
# ---------------------------------------
# Jeu du Pendu - Gabarit minimaliste
# À compléter par les étudiants
# ---------------------------------------

class color:
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

themes = {
    "Animaux" : ["chat", "chien", "oiseau", "chaton", "chienon"],
    "Pays" : ["france", "allemagne", "italie", "espagne", "portugal"],
    "Fruits" : ["pomme", "banane", "orange", "kiwi", "melon"],
    "Profession" : ["medecin", "chimiste", "professeur", "medecin", "chimiste"],
}

stages = [
    '''
       
       |   
       |   
       |   
       |   
       |
    =============
    ''',
    '''
       ---------
       |       |
       |       
       |       
       |       
       |
    =============
    ''',
    '''
       ---------
       |       |
       |      😨
       |       
       |       
       |
    =============   
    ''',
    '''
       ---------
       |       |
       |      😱
       |       |
       |       
       |
    =============
    ''',
    '''
       ---------
       |       |
       |      😭
       |      /|
       |       
       |
    =============
    ''',
    '''
       ---------
       |       |
       |      😵‍💫
       |      /|\\
       |       
       |
    =============
    ''',
    '''
       ---------
       |       |
       |      😵
       |      /|\\
       |      / 
       |
    =============
    ''',
    '''
       ---------
       |       |
       |      💀
       |      /|\\
       |      / \\
       |
    =============
    '''
]

mot_affiche = []

def afficher_titre():
    # Afficher un joli titre ASCII ou un message de bienvenu
    print(color.GREEN + color.BOLD + "\t\t\t Bienvenue dans le jeu du pendu" + color.END)
    print("""                                                                                   
     ██ ███████ ██    ██     ██████  ███████     ██████  ███████ ███    ██ ██████  ██    ██ 
     ██ ██      ██    ██     ██   ██ ██          ██   ██ ██      ████   ██ ██   ██ ██    ██ 
     ██ █████   ██    ██     ██   ██ █████       ██████  █████   ██ ██  ██ ██   ██ ██    ██ 
██   ██ ██      ██    ██     ██   ██ ██          ██      ██      ██  ██ ██ ██   ██ ██    ██ 
 █████  ███████  ██████      ██████  ███████     ██      ███████ ██   ████ ██████   ██████                                                   
                                                                                        
                                                                                        """)
    
def choisir_mot():

    # Choisir un mot au hasard dans une liste
    while True:
        print("""Choisissez un theme :
        1 - Animaux
        2 - Pays
        3 - Fruits
        4 - Profession
        """)

        numtheme = int(input(color.YELLOW + "\t Entrer le numero de theme choisir : " + color.END))
        if numtheme-1 in range(len(themes)):
            break
    
    theme = list(themes.keys())[numtheme-1]
    mot_secret = random.choice(themes[theme])        
    return mot_secret

def page_one():
    print("""
            ---------
            |       |
            |      💀
            |      /|\\
            |      / \\
            |
            ===========
    """)

def choisir_difficulte():
    while True:
        print("""Choisissez un niveau de difficulté :
        1 - Facile
        2 - Normal
        3 - Difficile
        4 - Retour au menu principal
        """)
        try:
            numdifficulte = int(input(color.YELLOW + "\t Entrer le numero de difficulté choisir : " + color.END))
            if numdifficulte == 4:
                return None
            if 1 <= numdifficulte <= 3:
                return numdifficulte
            print(color.RED + "Veuillez entrer un numéro entre 1 et 4." + color.END)
        except ValueError:
            print(color.RED + "Veuillez entrer un numéro valide." + color.END)

def vies(numdifficulte):
    if numdifficulte == 1:
        return 7
    elif numdifficulte == 2:
        return 5
    elif numdifficulte == 3:
        return 3

def afficher_etat(mot_affiche, vies_restantes):
    
    for lettre in mot_affiche:
        print(lettre, end=" ")
    print()
    print("Vies restantes :", vies_restantes)
    
    # Map vies_restantes to a valid stage index
    # stages list has 8 elements (0-7), so we need to ensure the index is within range
    stage_index = min(7, max(0, 7 - vies_restantes))
    print(stages[stage_index])

    # Afficher l'état actuel du jeu
def demander_lettre():
    while True:
        lettre = input(color.YELLOW + "\t Entrer une lettre : " + color.END)
        if lettre.isalpha() and len(lettre) == 1:
            break
    return lettre
    # Demander une lettre à l'utilisateur
def verifier_lettre(mot_secret, mot_affiche, lettre):
    if lettre in mot_secret:
        for i in range(len(mot_secret)):
            if mot_secret[i] == lettre:
                mot_affiche[i] = lettre
    else:
        return False
    return True
    # Vérifier la lettre et mettre à jour l'affichage du mot
def afficher_victoire():
    print(""" 
        ██████  ██████   █████  ██    ██  ██████      ██ 
        ██   ██ ██   ██ ██   ██ ██    ██ ██    ██     ██ 
        ██████  ██████  ███████ ██    ██ ██    ██     ██ 
        ██   ██ ██   ██ ██   ██  ██  ██  ██    ██        
        ██████  ██   ██ ██   ██   ████    ██████      ██                                              
    """)
    print("\tVous Avez Gagné !! ")

def afficher_defaite(mot_secret):
    print("""
        
    ██████  ███████ ██████  ██████  ██    ██ 
    ██   ██ ██      ██   ██ ██   ██ ██    ██ 
    ██████  █████   ██████  ██   ██ ██    ██ 
    ██      ██      ██   ██ ██   ██ ██    ██ 
    ██      ███████ ██   ██ ██████   ██████  
                                         
    """)
    print("\t Mot correct est : ")
    print(color.BLUE + color.BOLD +"\t" + mot_secret + color.END)
    # Afficher un message de défaite et le mot secret
def jouer(p1, p2):
    mot_secret = choisir_mot()
    difficulte = choisir_difficulte()
    if difficulte is None:
        return
    
    mot_affiche = ["-" for _ in mot_secret]
    vies_restantes = vies(difficulte)
    while vies_restantes > 0:
        afficher_etat(mot_affiche, vies_restantes)
        lettre = demander_lettre()
        if verifier_lettre(mot_secret, mot_affiche, lettre):
            if "-" not in mot_affiche:
                afficher_victoire()
                break
        else:
            vies_restantes -= 1
    if vies_restantes == 0:
        afficher_defaite(mot_secret)
    # Boucle principale du jeu (appel des fonctions précédentes)
# Boucle pour rejouer


def playerselect():
    while True:
        print("""Choisissez un mode de jeu :
        1 - Un joueur
        2 - Deux joueurs
        """)
        try:
            numplayer = int(input(color.YELLOW + "\t Entrer le numero de mode choisir : " + color.END))
            if numplayer == 1:
                return 1
            elif numplayer == 2:
                return 2
            print(color.RED + "Veuillez entrer un numéro entre 1 et 2." + color.END)
        except ValueError:
            print(color.RED + "Veuillez entrer un numéro valide." + color.END)


afficher_titre()
page_one()
p=playerselect()
if (p == 1):
    jouer(p1, None)
else:
    jouer(p1, p2)


while True:
    jouer(p1, p2)
    rejouer = input(color.YELLOW + "\t Voulez-vous rejouer ? (o/n) : " + color.END)
    if rejouer.lower() != "o":
        break
print("\n")


