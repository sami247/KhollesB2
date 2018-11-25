#!/usr/bin/python

import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-l',action= lecture)
parser.add_argument('-a',action= ecriture)
parser.add_argument('-c',action= supprimer)
parser.add_argument('-s --max', action= maximum)
parser.add_argument('-s --min', action = minimum)
parser.add_argument('-s --moy' action= moyenne)
parser.add_argument('-s --sum' action = somme)
parser.add_argument('-t' action = ordre)
parser.add_argument('-t --desc' action = decroissant)
args = parser.parse_args()


def lecture():
    read = csv.reader(open("MONFICHIER.csv",))
    for read in cr: print row




def ecriture():
    c = csv.writer(open("MONFICHIER.csv"))
    c.writerow(liste1 = [5,3,9])


def supprimer():
    read = csv.reader(open("MONFICHIER.csv",))
    for read in cr: print row
    del liste1


def maximum():
    liste1 = [5,3,9]
    max(liste1)
    print max(liste1)


def minimum():
    liste1 = [5,3,9]
    min(liste1)
    print min(liste1)


def moyenne():
    liste1 = [5,3,9]
    moy(liste1)
    print moy(liste1)


def somme():
    liste1 = [5,3,9]
    sum(liste1)
    print sum(liste1)



def ordre():
    liste1 = [5,3,9]
    sorted(liste1)


def decroissant():
    liste1 = [5,3,9]
    sorted(liste1, reverse=True)







    












