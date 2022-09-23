from Personnage import Personnage

class Joueur:
    def __init__(self, nom :str, maximum: int = 5, liste = []):
        self.__nom = nom
        self.__maximum = maximum
        if len(liste) <= maximum:
            self.__liste = liste
        else:
            self.__liste = liste[-5]

    def __str__(self):
        rep = f"Joueur {self.__nom} possédant {len(self.__liste)} Personnage(s):"
        if len(self.__liste)>0:
            for p in self.__liste:
                rep += f"\n - {p}"
        return rep

    def ajout_joueur(self, p:Personnage) ->bool:
        if len(self.__liste) < self.__maximum:
            self.__liste.append(p)
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
            print(f"liste : {p}")
            if p.pseudo == nom:
                return p
        return None

    def cherche_personnage(self, p :Personnage) -> Personnage:
        for per in self.__liste:
            if per == p:
                return p
        return None

    def delete_id(self,index : int) -> bool:
        if index < self.__maximum:
            del(self.__liste[index])
            return True
        else:
            return False

    def delete_nom(self, nom:str) -> bool:
        for i in range(len(self.__liste)):
            if self.__liste[i].pseudo == nom:
                del(self.__liste[i])
                return True
        return False

    def delete_personnage(self, per: str) -> bool:
        for i in range(len(self.__liste)):
            if self.__liste[i] == per:
                del (self.__liste[i])
                return True
        return False

    @property
    def nom(self) ->str:
        return self.__nom