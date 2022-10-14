from abc import ABC, abstractmethod
import sys
import mysql.connector

class Pokemon(ABC):
    def __init__(self,nom : str, poids : float):
        self.__nom = nom
        self.__poids = poids

    def __str__(self) -> str:
        return f"Je suis le pokémon {self.__nom}, mon poids est de {self.__poids}"

    def __repr__(self):
        return f"{self.__class__} {self.__nom}"
    @abstractmethod
    def vitesse(self) -> float:
        pass
    @property
    def nom(self):
        return self.__nom

    @property
    def poids(self):
        return self.__poids

    @poids.setter
    def poids(self,poids:float) -> float:
        self.__poids=poids

class PokemonTerre(Pokemon):
    def __init__(self, nom : str, poids : float, nb_pattes : int, taille : float):
        super().__init__(nom,poids)
        self.__nb_pattes = nb_pattes
        self.__taille = taille

    def __str__(self) -> str:
        return f"{super().__str__()} ma vitesse est de {self.vitesse():.2f} km/h. J'ai {self.__nb_pattes} " \
               f"pattes, ma taille est de {self.__taille}"

    def vitesse(self) -> float:
        return self.__taille*self.__nb_pattes*3

    @property
    def taille(self) -> float:
        return self.__taille

    @taille.setter
    def taille(self,taille : float):
        self.__taille=taille
    @property
    def nb_pattes(self)-> int:
        return self.__nb_pattes

    @nb_pattes.setter
    def nb_pattes(self,nb):
        self.__nb_pattes=nb



class PokemonCasanier(PokemonTerre, ):
    def __init__(self, nom : str, poids : float, nb_pattes : int, taille : float, nb_heures_tv : int):
        super().__init__(nom,poids,nb_pattes,taille)
        self.__nb_heures_tv = nb_heures_tv

    def __str__(self)-> str:
        return f"{super().__str__()} et je regarde la télé {self.__nb_heures_tv} heures par jour"

    def save(self,curseur):
        query = f"insert into pokemoncasanier (nom,poids, nombrepattes,taille,nbheurestv) values {tuple(self.__dict__.values())}"
        curseur.execute(query)

class PokemonSportif(PokemonTerre):
    def __init__(self, nom : str, poids : float, nb_pattes : int, taille : float, frequence_cardiaque : int):
        super().__init__(nom,poids,nb_pattes,taille)
        self.__frequence_cardiaque = frequence_cardiaque

    def __str__(self)-> str:
        return f"{super().__str__()} et ma freqence cardiaque est de  {self.__frequence_cardiaque} pulsation par minutes"

    def save(self,curseur):
        query = f"insert into pokemonsportif (nom,poids, nombrepattes,taille,frequencecardiaque) values {tuple(self.__dict__.values())}"
        curseur.execute(query)


class PokemonEau(Pokemon):
    def __init__(self, nom : str, poids : float, nb_nageoires ):
        super().__init__(nom,poids)
        self.__nb_nageoires = nb_nageoires

    @property
    def nb_nageoires(self)-> int:
        return self.__nb_nageoires

    def __str__(self) -> str:
        return f"{super().__str__()} ma vitesse est de {self.vitesse():.2f} km/h, j'ai {self.nb_nageoires} nageoires"

class PokemonMer(PokemonEau):
    def __init__(self, nom : str, poids : float, nb_nageoires ):
        super().__init__(nom,poids,nb_nageoires)

    def vitesse(self) -> float:
        return self.poids/25 * self.nb_nageoires

    def save(self,curseur):
        query = f"insert into pokemonmer (nom,poids, nombrenageoires) values {tuple(self.__dict__.values())}"
        curseur.execute(query)


class PokemonCroisiere(PokemonEau):
    def __init__(self, nom : str, poids : float, nb_nageoires ):
        super().__init__(nom,poids,nb_nageoires)

    def vitesse(self) -> float:
        return self.poids/25 * self.nb_nageoires

    def save(self,curseur, id = None):
        if id is None:
            liste = self.__dict__.values()
            query = f"insert into pokemoncroisiere (nom,poids, nombrenageoires) values {tuple(liste)}"
        else :
            liste =[id ,]
            for p in self.__dict__.values():
                liste.append(p)
            query = f"insert into pokemoncroisiere (pokedex_id, nom,poids, nombrenageoires) values {tuple(liste)}"
        print (query)
        #curseur.execute(query)

class pokedex:
    def __init__(self,nom : str, liste_pokemon : list = []):
        self.__nom = nom
        self.__liste_pokemon = liste_pokemon

    def __str__(self) -> str:
        return f"pokedex {self.__nom} possédant {len(self.__liste_pokemon)} pokemon {self.__liste_pokemon}"

    def vitesse_moyenne(self) -> float:
        if len(self.__liste_pokemon)>0:
            moy = 0
            for p in  self.__liste_pokemon:
                moy += p.vitesse()
            moy /= len(self.__liste_pokemon)
            return moy
        return 0

    def add(self, pokemon : Pokemon):
        return self.__liste_pokemon(pokemon)

    def size(self):
        return len(self.__liste_pokemon)

    def recherche(self,index : int) -> Pokemon:
        if 0<= index < len(self.__liste_pokemon):
            return self.__liste_pokemon[index]
        return None

    def recherche_nom(self,nom : str)-> Pokemon:
        pass

def main():
   pick = PokemonCasanier("salameche",12,2,.65,8)
   print(pick)
   po = PokemonSportif("pikachu",18,2,0.85,120)
   print(po)
   p = PokemonMer("rondoudou",45,2)
   print (p)
   p2 = PokemonCroisiere("bulbizarre",15,3)
   print(p2)
   pok = pokedex("mon pokedex",[po,pick,p2,p])
   print(pok)
   print (pok.vitesse_moyenne())

   db = mysql.connector.connect(user='toto',password='toto',database='pokemon')
   moncurseur = db.cursor()
   po.save(moncurseur)
   p.save(moncurseur)
   p2.save(moncurseur)
   pick.save(moncurseur)
   db.commit()
   moncurseur.close()
   db.close()

if __name__ == "__main__":
    sys.exit(main())