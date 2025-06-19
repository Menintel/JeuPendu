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
def jouer_un_joueur():
    score = {"gagne": 0, "perdu": 0}
    while True:
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
                    score["gagne"] += 1
                    break
            else:
                vies_restantes -= 1
        if vies_restantes == 0:
            afficher_defaite(mot_secret)
            score["perdu"] += 1

        rejouer = input(color.YELLOW + "\t Voulez-vous rejouer ? (o/n) : " + color.END)
        if rejouer.lower() != "o":
            print(color.BOLD + color.GREEN + f"\nScore final : {score['gagne']} victoire(s), {score['perdu']} défaite(s)." + color.END)
            break
    # Boucle principale du jeu (appel des fonctions précédentes)
# Boucle pour rejouer

def jour1_contre_joueur2():
    print(color.BLUE + "\tEntrez le nom du Joueur 1 :" + color.END)
    joueur1 = input()
    print(color.BLUE + "\tEntrez le nom du Joueur 2 :" + color.END)
    joueur2 = input()
    joueurs = [joueur1, joueur2]
    tour = 0

    while True:
        current_setter = joueurs[tour % 2]
        current_guesser = joueurs[(tour + 1) % 2]

        print(color.GREEN + f"\n{current_setter}, tapez un mot à faire deviner à {current_guesser}." + color.END)
        mot_secret = input("(Le mot doit rester secret !) ").lower()
        print("\n" * 50)  # Clear screen

        difficulte = choisir_difficulte()
        if difficulte is None:
            return

        mot_affiche = ["-" for _ in mot_secret]
        vies_restantes = vies(difficulte)

        print(color.BOLD + f"\n{current_guesser}, à vous de jouer !" + color.END)

        while vies_restantes > 0:
            afficher_etat(mot_affiche, vies_restantes)
            lettre = demander_lettre()
            if verifier_lettre(mot_secret, mot_affiche, lettre):
                if "-" not in mot_affiche:
                    afficher_victoire()
                    print(color.GREEN + f"\t{current_guesser} a gagné ce tour contre {current_setter}!" + color.END)
                    break
            else:
                vies_restantes -= 1
        if vies_restantes == 0:
            afficher_defaite(mot_secret)
            print(color.RED + f"\t{current_guesser} a perdu. {current_setter} remporte ce tour!" + color.END)

        rejouer = input(color.YELLOW + "\t Voulez-vous rejouer ? (o/n) : " + color.END)
        if rejouer.lower() != "o":
            break
        tour += 1

def jours_contre_pc():
    print(color.BLUE + "\tEntrez le nom du Joueur 1 :" + color.END)
    joueur1 = input()
    print(color.BLUE + "\tEntrez le nom du Joueur 2 :" + color.END)
    joueur2 = input()
    
    scores = {joueur1: {"gagne": 0, "perdu": 0}, joueur2: {"gagne": 0, "perdu": 0}}
    
    while True:
        # Player 1's turn
        print(color.BOLD + f"\n--- Tour de {joueur1} ---" + color.END)
        mot_secret_p1 = choisir_mot()
        difficulte_p1 = choisir_difficulte()
        if difficulte_p1 is None:
            break # Go back to main menu
        
        mot_affiche_p1 = ["-" for _ in mot_secret_p1]
        vies_restantes_p1 = vies(difficulte_p1)
        
        while vies_restantes_p1 > 0:
            afficher_etat(mot_affiche_p1, vies_restantes_p1)
            lettre_p1 = demander_lettre()
            if verifier_lettre(mot_secret_p1, mot_affiche_p1, lettre_p1):
                if "-" not in mot_affiche_p1:
                    afficher_victoire()
                    print(color.GREEN + f"\t{joueur1} a trouvé le mot !" + color.END)
                    scores[joueur1]["gagne"] += 1
                    break
            else:
                vies_restantes_p1 -= 1
        if vies_restantes_p1 == 0:
            afficher_defaite(mot_secret_p1)
            print(color.RED + f"\t{joueur1} n'a pas trouvé le mot." + color.END)
            scores[joueur1]["perdu"] += 1

        # Player 2's turn
        print(color.BOLD + f"\n--- Tour de {joueur2} ---" + color.END)
        mot_secret_p2 = choisir_mot()
        difficulte_p2 = choisir_difficulte()
        if difficulte_p2 is None:
            break # Go back to main menu
        
        mot_affiche_p2 = ["-" for _ in mot_secret_p2]
        vies_restantes_p2 = vies(difficulte_p2)
        
        while vies_restantes_p2 > 0:
            afficher_etat(mot_affiche_p2, vies_restantes_p2)
            lettre_p2 = demander_lettre()
            if verifier_lettre(mot_secret_p2, mot_affiche_p2, lettre_p2):
                if "-" not in mot_affiche_p2:
                    afficher_victoire()
                    print(color.GREEN + f"\t{joueur2} a trouvé le mot !" + color.END)
                    scores[joueur2]["gagne"] += 1
                    break
            else:
                vies_restantes_p2 -= 1
        if vies_restantes_p2 == 0:
            afficher_defaite(mot_secret_p2)
            print(color.RED + f"\t{joueur2} n'a pas trouvé le mot." + color.END)
            scores[joueur2]["perdu"] += 1
            
        print("\n--- Scores Actuels ---")
        print(f"{joueur1}: Victoires - {scores[joueur1]['gagne']}, Défaites - {scores[joueur1]['perdu']}")
        print(f"{joueur2}: Victoires - {scores[joueur2]['gagne']}, Défaites - {scores[joueur2]['perdu']}")


        rejouer = input(color.YELLOW + "\t Voulez-vous rejouer ? (o/n) : " + color.END)
        if rejouer.lower() != "o":
            print(color.BOLD + "\n--- Score Final ---" + color.END)
            print(color.GREEN + f"{joueur1}: {scores[joueur1]['gagne']} victoire(s), {scores[joueur1]['perdu']} défaite(s)." + color.END)
            print(color.GREEN + f"{joueur2}: {scores[joueur2]['gagne']} victoire(s), {scores[jouleur2]['perdu']} défaite(s)." + color.END)
            break
    
    

def playerselect():
    while True:
        print("""Choisissez un mode de jeu :
        1 - Un joueur contre PC
        2 - Un joueur contre un autre joueur
        3 - Deux joueurs contre PC
        """)
        try:
            numplayer = int(input(color.YELLOW + "\t Entrer le numero de mode choisir : " + color.END))
            if numplayer == 1:
                return 1
            elif numplayer == 2:
                return 2
            elif numplayer == 3:
                return 3
            print(color.RED + "Veuillez entrer un numéro entre 1 et 2." + color.END)
        except ValueError:
            print(color.RED + "Veuillez entrer un numéro valide." + color.END)


afficher_titre()
page_one()
p=playerselect()

if (p == 1):
    jouer_un_joueur()
elif (p == 2):
    jouer1_contre_joueur2()
else:
    jours_contre_pc()