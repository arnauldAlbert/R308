import sys
from Personnage import Personnage
import json,pickle
class Guerrier(Personnage):
    def __init__(self,pseudo : str, niveau:int=1) :
        super().__init__(pseudo,niveau)

        self.points_de_vie = niveau*8+4
        self.initiative = niveau *4+6

    def __str__(self):
        return f"Guerrier {super().__str__()} "
    def soin(self):
        self.points_de_vie = self.niveau*5+3

    def degats(self) -> int:
        return self.niveau*2+2

    def toJson(self)-> str:
        dict = {"class": "Guerrier", "pseudo": self.pseudo, "niveau": self.niveau, "points_de_vie": self.points_de_vie, "initiative": self.initiative}
        print(dict)
        return json.dumps(dict)

