#! /usr/bin/env python3
# -*- coding: Utf-8 -*-

####----####----####----####----####
###############IMPORT###############
####----####----####----####----####

from os import path
from os import getcwd
from os import mkdir
from os import chdir

import configparser

####----####----####----####----####
##############function##############
####----####----####----####----####

def save(stat, record):
    chemin = path.join(getcwd(),'save.ini')
    save_ini = configparser.ConfigParser()
    if path.isfile(chemin):
        save_ini.read(chemin)
        f_parti = int(save_ini.get("Facile", "Nombre de parties")) + stat["facile"]
        f_coup = int(save_ini.get("Facile", "Nombre de coups")) + stat["facile coup"]
        n_parti = int(save_ini.get("Normal", "Nombre de parties")) + stat["normal"]
        n_coup = int(save_ini.get("Normal", "Nombre de coups")) + stat["normal coup"]
        d_parti = int(save_ini.get("Difficile", "Nombre de parties")) + stat["difficile"]
        d_coup = int(save_ini.get("Difficile", "Nombre de coups")) + stat["difficile coup"]
        e_parti = int(save_ini.get("Extrême", "Nombre de parties")) + stat["extreme"]
        e_coup = int(save_ini.get("Extrême", "Nombre de coups")) + stat["extreme coup"]
        if f_parti != 0:
            save_ini.set("Facile", "Nombre de parties", str(f_parti))
            save_ini.set("Facile", "Nombre de coups", str(f_coup))
            save_ini.set("Facile", "Moyenne", str(int(f_coup/f_parti)))
            save_ini.set("Facile", "Record de coups", str(record[0]))
            save_ini.set("Facile", "Pseudo du record", record[1])
        if n_parti != 0:
            save_ini.set("Normal", "Nombre de parties", str(n_parti))
            save_ini.set("Normal", "Nombre de coups", str(n_coup))
            save_ini.set("Normal", "Moyenne", str(int(n_coup/n_parti)))
            save_ini.set("Normal", "Record de coups", str(record[2]))
            save_ini.set("Normal", "Pseudo du record", record[3])
        if d_parti != 0:
            save_ini.set("Difficile", "Nombre de parties", str(d_parti))
            save_ini.set("Difficile", "Nombre de coups", str(d_coup))
            save_ini.set("Difficile", "Moyenne", str(int(d_coup/d_parti)))
            save_ini.set("Difficile", "Record de coups", str(record[4]))
            save_ini.set("Difficile", "Pseudo du record", record[5])
        if e_parti != 0:
            save_ini.set("Extrême", "Nombre de parties", str(e_parti))
            save_ini.set("Extrême", "Nombre de coups", str(e_coup))
            save_ini.set("Extrême", "Moyenne", str(int(e_coup/e_parti)))
            save_ini.set("Extrême", "Record de coups", str(record[6]))
            save_ini.set("Extrême", "Pseudo du record", record[7])
        save_ini.write(open(chemin,"w"))

def CreateIni():
    chemin = path.join(getcwd(),'save.ini')
    save_ini = configparser.ConfigParser()
    difficulty = ["Facile", "Normal", "Difficile", "Extrême"]
    if not path.isfile(chemin):
        for dif in difficulty:
            save_ini.write(open(chemin,"w"))
            save_ini.add_section(dif)
            save_ini.set(dif, "Nombre de parties", "0")
            save_ini.set(dif, "Nombre de coups", "0")
            save_ini.set(dif, "Moyenne", "0")
            save_ini.set(dif, "Record de coups", "0")
            save_ini.set(dif, "Pseudo du record", "NoOne")
        save_ini.write(open(chemin,"w"))


def Load():
    chemin = path.join(getcwd(),'save.ini')
    save_ini = configparser.ConfigParser()
    difficulty = ["Facile", "Normal", "Difficile", "Extrême"]
    record =[]
    for dif in difficulty:
        save_ini.read(chemin)
        record.append(int(save_ini.get(dif, "Record de coups")))
        record.append(save_ini.get(dif, "Pseudo du record"))
    return record