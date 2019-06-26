#! /usr/bin/env python3
# -*- coding: Utf-8 -*-

####----####----####----####----####
###############IMPORT###############
####----####----####----####----####

import random
import Save


####----####----####----####----####
##############function##############
####----####----####----####----####

def Jeu():
    play = True
    stat = {"facile":0, "facile coup":0, "normal":0, "normal coup":0, "difficile":0, "difficile coup": 0, "extreme": 0, "extreme coup" : 0}
    Save.CreateIni()
    pseudo = ChooseName()
    record = Save.Load()

    while play:
        print ("Bienvenue dans le jeu de plus ou moins")
        print("Veuillez choisir une difficulté :\n1) Facile\n2) Normal\n3) Difficile\n4) Extrême\n")
        difficulte = NombreUser()
        nbre_mystere = LaunchDifficulty(difficulte, stat)
        compteur = 0
        while 1:
            nbre_entree = NombreUser()
            compteur+= 1
            if nbre_mystere == nbre_entree:
                print ("Vous avez gagné en {0} coups! bravo !".format(compteur))
                Compteur(difficulte, compteur, stat)
                Score(difficulte, compteur, record, pseudo)
                break
            elif nbre_mystere > nbre_entree:
                print("C'est plus")
            elif nbre_mystere < nbre_entree:
                print ("C'est moins")
            else:
                print ("Error")
        play = PlayAgain(stat, record)

def NombreMystere(maxi):
    nombre_mystere = random.randint(1, maxi)
    return nombre_mystere

def PlayAgain(stat, record):
    while 1:
        play_again = input("Voulez-vous rejouer ? oui / non\n")
        if play_again == "oui":
            return True
        elif play_again == "non":
            print ("Vous avez jouer {0} facile, {1} normal, {2} difficile, {3} extrême".format(stat["facile"], stat["normal"], stat["difficile"], stat["extreme"]))
            Save.save(stat, record)
            return False
        else:
            print("Merci de répondre par 'oui' ou 'non'")

def NombreUser():
    while 1:
        try:
            nbre_entree = int(input("Votre réponse ? \n"))
            break
        except ValueError:
            print("Mauvaise valeur entrée")
    return nbre_entree

def LaunchDifficulty(difficulte, stat):
    play = True
    while play:
        if difficulte == 1:
            print("Bienvenue dans le mode facile, un nombre sera tirer entre 1 et 10")
            stat["facile"]+= 1
            nbre_mystere = NombreMystere(10)
            play = False
        elif difficulte == 2:
            print("Bienvenue dans le mode normal, un nombre sera tirer entre 1 et 100")
            stat["normal"]+= 1
            nbre_mystere = NombreMystere(100)
            play = False
        elif difficulte == 3:
            print("Bienvenue dans le mode difficile, un nombre sera tirer entre 1 et 1000")
            stat["difficile"]+= 1
            nbre_mystere = NombreMystere(1000)
            play = False
        elif difficulte == 4:
            print("Bienvenue dans le mode extrême, un nombre sera tirer entre 1 et 10.000")
            stat["extreme"]+= 1
            nbre_mystere = NombreMystere(10000)
            play = False
        else:
            print("Mauvaise valeur rentrée..")
    return nbre_mystere

def Compteur(difficulte, compteur, stat):
    if difficulte == 1:
        stat["facile coup"]+= compteur
    elif difficulte == 2:
        stat["normal coup"]+= compteur
    elif difficulte == 3:
        stat["difficile coup"]+= compteur
    elif difficulte == 4:
        stat["extreme coup"]+= compteur

def ChooseName():
    pseudo = input("Veuillez choisir votre pseudo:  ")
    print("Bienvenue {0} ! Amusez-vous bien !".format(pseudo))
    return pseudo

def Score(difficulte, compteur, record, pseudo):
    if difficulte == 1:
        if record[0] == 0:
            record[0] = compteur
            record[1] = pseudo
        elif record[0] > compteur:
            record[0] = compteur
            record[1] = pseudo            
    elif difficulte == 2:
        if record[2] == 0:
            record[2] = compteur
            record[3] = pseudo
        elif record[2] > compteur:
            record[2] = compteur
            record[3] = pseudo
    elif difficulte == 3:
        if record[4] == 0:
            record[4] = compteur
            record[5] = pseudo
        elif record[4] > compteur:
            record[4] = compteur
            record[5] = pseudo
    elif difficulte == 4:
        if record[6] == 0:
            record[6] = compteur
            record[7] = pseudo
        elif record[6] > compteur:
            record[6] = compteur
            record[7] = pseudo
