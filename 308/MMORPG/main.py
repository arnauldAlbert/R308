import sys

from mod import *
from Joueur import Joueur

def main():
    p : Personnage = Personnage("Merlin")
    print(p)
    p2 : Personnage = Personnage("Conan",45)
    print(p2)
    p3 : Personnage = Personnage("Merlin")

    if p3 == p:
        print("les personnages p et p3 sont identiques")
    else :
        print("les personnages p et p3 sont différents")

    p.combat(p2)

    print(p)
    if p3 == p:
        print("les personnages p et p3 sont identiques")
    else:
        print("les personnages p et p3 sont différents")

    print(p2)
    if (p.points_de_vie>0):
        print(f"le personnage {p.pseudo} a vaincu {p2.pseudo}")
    elif (p2.points_de_vie>0):
        print(f"le personnage {p2.pseudo} a vaincu {p.pseudo}")
    else:
        print(f"les personnages {p2.pseudo} et {p.pseudo} se sont entretués")

    p.soins()
    p2.soins()
    print(p)
    print(p2)

    g1 : Guerrier = Guerrier("arnauld",10)
    print (g1)

    m1 : Mage = Mage("toto", 12)
    m1.combat(g1)
    if (m1.points_de_vie>0):
        print(f"le personnage {m1.pseudo} a vaincu {g1.pseudo}")
    elif (g1.points_de_vie>0):
        print(f"le personnage {g1.pseudo} a vaincu {m1.pseudo}")
    else:
        print(f"les personnages {g1.pseudo} et {m1.pseudo} se sont entretués")

    chaine = p2.toJson()
    print(chaine)
    p4 = fromJson(chaine)
    print(p4)
    chaine = g1.toJson()
    p4 = fromJson(chaine)
    print(p4)

    buff = p4.toBuffer()
    p5 = Personnage.fromPickle(buff)
    print(p5)

    j1 : Joueur = Joueur("arnauld", 7)
    j1.ajout_joueur(p)
    print(j1)

    liste=[p,p2,p3,p4]
    j2 : Joueur = Joueur("toto",liste=liste)
    print(j2)

if __name__ == "__main__":
    sys.exit(main())