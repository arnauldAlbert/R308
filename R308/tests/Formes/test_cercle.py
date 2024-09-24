import math

from R308.src.Formes.Cercle import Cercle
from R308.src.Formes.Point import Point
c1 = Cercle (2)
def test_diametre():

    assert c1.diametre() == 4

def test_perimetre():
    assert c1.perimetre() == math.pi * 2 * 2

def test_contient():
    p = Point(5,6)
    assert c1.contient(p) == False