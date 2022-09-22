import math

class Point:
    def __init__(self,x:float=0,y:float=0):
        self.__x :float = x
        self.__y :float = y

    def __str__(self) ->str:
        return f"Point x: {self.__x} y: {self.__y}"

    def distance_coordonnees(self,x:float=0,y:float=0)->float:
        res = math.sqrt((self.__x-x)*(self.__x-x) + (self.__y-y)*(self.__y-y))
        return res

    def distance_point(self,camarade) -> float:
        res = math.sqrt((self.__x-camarade.__x)*(self.__x-camarade.__x) + (self.__y-camarade.__y)*(self.__y-camarade.__y))
        return res