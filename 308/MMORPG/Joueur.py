from Personnage import Personnage

class Joueur:
    def __init__(self, nom :str, maximum: int = 5, liste = []):
        self.__nom = nom
        self.__maximum = maximum
        if len(liste) <= maximum:
            self.__liste = liste
        else:
            self.__liste = liste[:self.__maximum]

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
        if 0 <= index < self.__maximum:
            if index <= len(self.__liste):
                return self.__liste[index]
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
                return per
        return None

    def delete_id(self,index : int) -> bool:
        if 0<= index < len(self.__liste):
            self.__liste.pop(index)
            #del(self.__liste[index])
            return True
        return False

    def delete_nom(self, nom:str) -> bool:
        for i in range(len(self.__liste)):
            if self.__liste[i].pseudo == nom:
                self.__liste.remove(self.__liste[i])
                # del(self.__liste[i])
                return True
        return False

    def delete_personnage(self, per: str) -> bool:
        for p in self.__liste:
            if p == per:
                self.__liste.remove(p)
                # del(p)
                return True
        return False


    @property
    def nom(self) ->str:
        return self.__nom