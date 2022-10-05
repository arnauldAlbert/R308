from Personnage import Personnage
import json,pickle
class Mage(Personnage):
    def __init__(self,pseudo : str, niveau:int=1):
        super().__init__(pseudo,niveau)
        self.__mana = niveau * 5
        self.points_de_vie = niveau* 5+10
        self.initiative = niveau *6+4

    def __str__(self):
        return f"Mage {super().__str__()} "
    def soin(self):
        self.points_de_vie = self.niveau*5+10

    def degats(self) -> int:
        deg = self.niveau
        if self.__mana > 4:
            deg +=3
            self.__mana -=4
        return deg

    def toJson(self)-> str:
        dict = {"class": "Mage", "pseudo": self.pseudo, "niveau": self.niveau, "points_de_vie": self.points_de_vie, "initiative": self.initiative}

        print(dict)
        return json.dumps(dict)