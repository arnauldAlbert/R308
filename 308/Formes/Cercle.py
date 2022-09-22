import math

from Point import Point
class Cercle:

    def __init__(self,rayon : float, centre : Point = None):
        self.__rayon = rayon
        if centre != None:
            self.__centre = centre
        else:
            self.__centre = Point(0,0)

    def __str__(self):
        return f"Cercle de rayon {self.__rayon} et de centre {self.__centre}"

    def diametre(self):
        return self.__rayon * 2

    def perimetre(self):
        return self.diametre()*math.pi

    def surface(self):
        return self.__rayon * self.__rayon * math.pi