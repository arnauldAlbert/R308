import json,pickle

class Personnage:
    def __init__(self, pseudo : str, niveau : int =1):
        self.__pseudo = pseudo
        self.__niveau = niveau
        self.__points_de_vie = niveau
        self.__initiative = niveau

    def __str__(self) -> str:
        return f"{self.__pseudo} est de niveau {self.__niveau} possède {self.__points_de_vie} " \
               f"points de vie et une initiative de {self.__initiative}"

    def degats(self) -> int:
        return self.__niveau

    def attaque(self, opposant):
        if (self.__initiative>opposant.__initiative):
            opposant.__points_de_vie -= self.degats()
            if opposant.__points_de_vie < 0:
                self.__points_de_vie -= opposant.degats()
        elif (opposant.__initiative>self.__initiative):
            self.__points_de_vie -= opposant.degats()
            if self.points_de_vie < 0:
                opposant.__points_de_vie -= self.degats()
        else:
            opposant._points_de_vie -= self.degats()
            self.__points_de_vie -= opposant.degats()

    def combat(self,opposant):
        while (self.__points_de_vie>0 and opposant.__points_de_vie>0) :
            self.attaque(opposant)

    def soins(self):
        self.__points_de_vie = self.__niveau

    def __eq__(self,other):
        if (self.__pseudo == other.__pseudo and self.__niveau == other.__niveau):
            return True
        else:
            return False
    @property
    def points_de_vie(self) -> int:
        return self.__points_de_vie

    @points_de_vie.setter
    def points_de_vie(self,pv):
        if pv > 0:
            self.__points_de_vie = pv

    @property
    def initiative(self) -> int:
        return self.__initiative

    @initiative.setter
    def initiative(self, initiative:int):
        if initiative>0:
            self.__initiative = initiative


    @property
    def pseudo(self) -> str:
        return self.__pseudo

    @property
    def niveau(self) -> int:
        return self.__niveau

    def toJson(self) -> str:
        dict = {"class" : "Personnage" , "pseudo": self.__pseudo, "niveau": self.__niveau, "points_de_vie" : self.__points_de_vie, "initiative" : self.__initiative}
        return json.dumps(dict)

    def toBuffer(self) :
        ser = pickle.dumps(self)
        return ser
    @staticmethod
    def fromPickle(buffer):
        object = pickle.loads(buffer)
        return object

