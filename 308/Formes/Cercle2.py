import math

from Point import Point

class Cercle2:
    def __init__(self,rayon : float, centre : Point = None):
        self.__rayon = rayon
        if centre != None:
            self.__centre = centre
        else:
            self.__centre = Point(0,0)


    def __str__(self):
        return f"Cercle de centre {self.__centre} et de rayon {self.__rayon}"

    def diametre(self) -> float:
        return 2*self.__rayon

    def perimetre(self) -> float:
        return self.diametre()*math.pi

    def surface(self) -> float:
        return self.__rayon*self.__rayon*math.pi

    def intersection(self,autrecercle) ->bool:
        if (self.__centre.distance_point(autrecercle.__centre))< self.__rayon+autrecercle.__rayon :
            return True
        else:
            return False

