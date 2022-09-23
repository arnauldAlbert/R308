from Personnage import Personnage

class Joueur:
    def __init__(self, nom :str, maximum: int = 5, liste = []):
        self.__nom = nom
        self.__maximum = maximum
        if liste.size() <= maximum:
            self.__liste = liste
        else:
            self.__liste = liste[-5]

    def __str__(self):
        rep = f"Joueur {self.__nom} possédant {self.__liste.size()} Personnage(s):"
        if self.__liste.size()>0:
            for p in self.__liste:
                rep += f"\n - {p}"

    def ajout_joueur(self, p:Personnage) ->bool:
        if self.liste.size() < self.__maximum:
            self.__liste.add(p)
            return True
        else:
            return False

    def cherche_id(self,index : int) -> Personnage :
        if index < self.__maximum:
            return self.__liste[index]
        else:
            return None

    def cherche_nom(self, nom:str) -> Personnage:
        for p in self.__liste:
            if p.nom == nom:
                return p
        return None

    def cherche_personnage(self, p :Personnage) -> Personnage:
        for per in self.__liste:
            if per == p:
                return p
        return None