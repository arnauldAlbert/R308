import sys
from abc import ABC, abstractmethod
import mysql.connector

class Pokemon(ABC):
    def __init__(self,nom : str, poids : float):
        self.__nom = nom
        self.__poids = poids

    def __str__(self) -> str:
        return f"Je suis le Pokemon {self.__nom}, mon poids est de {self.__poids} kg."

    def __repr__(self) -> str:
        return self.__nom
    @abstractmethod
    def vitesse(self) -> float :
        pass

    @property
    def nom(self) -> str:
        return self.__nom

    @property
    def poids(self) -> float:
        return self.__poids

class PokemonTerre(Pokemon):
    def __init__(self,nom : str, poids : float, nbpattes : int, taille : float):
        super().__init__(nom, poids)
        self.__nbpattes = nbpattes
        self.__taille = taille

    def vitesse(self) -> float:
        return self.__taille * self.__nbpattes * 3

    def __str__(self) -> str:
        return f"{super().__str__()}, ma vitesse est de {self.vitesse():.2f} km/h." \
               f" J'ai {self.__nbpattes} pattes, ma taille est de {self.__taille}"

    @property
    def nbpattes(self)->int:
        return self.__nbpattes

    @property
    def taille(self)->float:
        return self.__taille

class PokemonSportif(PokemonTerre):
    def __init__(self,nom : str, poids : float, nbpattes : int, taille : float, frequence : int):
        super().__init__(nom,poids,nbpattes,taille)
        self.__frequenceCardiaque = frequence
    def __str__(self) -> str:
        return f"{super().__str__()}. ma fréquence cardiaque est de {self.__frequenceCardiaque} pulsations à la minute"

    @property
    def frequenceCardiaque(self):
        return self.__frequenceCardiaque

    def save(self, conn : mysql.connector, id : int):
        query = f"select count(id) from pokemonsportif where nom='{self.nom}' and pokedex_id={id}"
        res = conn.cursor()
        res.execute(query)

        if res.fetchone() == 0:
            query = f"insert into pokemonsportif values (0,'{self.nom}',{self.poids},{self.nbpattes},{self.taille},{self.__frequenceCardiaque},{id})"
            curseur = conn.cursor()
            curseur.execute(query)
            conn.commit()
            curseur.close()
        else :
            print("pokemon déjà la")


class PokemonCasanier(PokemonTerre):
    def __init__(self, nom : str, poids : float, nb_pattes : int, taille : float, nb_heures_tv : int):
        super().__init__(nom,poids,nb_pattes,taille)
        self.__nb_heures_tv = nb_heures_tv

    def __str__(self)-> str:
        return f"{super().__str__()} et je regarde la télé {self.__nb_heures_tv} heures par jour"

    def save(self, conn : mysql.connector, id : int):
        query = f"select count(id) from pokemoncasanier where nom='{self.nom}' and pokedex_id={id}"
        res = conn.cursor()
        res.execute(query)

        if res.fetchone() == 0:
            query = f"insert into pokemoncasanier values (0,'{self.nom}',{self.poids},{self.nbpattes},{self.taille},{self.__nb_heures_tv},{id})"
            curseur = conn.cursor()
            curseur.execute(query)
            conn.commit()
            curseur.close()
        else :
            print("pokemon déjà la")


class PokemonEau(Pokemon, ABC):
    def __init__(self, nom : str, poids : float, nb_nageoires ):
        Pokemon.__init__(self,nom,poids)
        self.__nb_nageoires = nb_nageoires

    @property
    def nb_nageoires(self)-> int:
        return self.__nb_nageoires

    @abstractmethod
    def vitesse(self):
        pass

    def __str__(self) -> str:
        return f"{super().__str__()} ma vitesse est de {self.vitesse():.2f} km/h," \
               f" j'ai {self.__nb_nageoires} nageoires"


class PokemonMer(PokemonEau):
    def __init__(self, nom : str, poids : float, nb_nageoires : int):
        super().__init__(nom,poids,nb_nageoires)

    def vitesse(self) -> float:
        return self.poids/25 * self.nb_nageoires

    def save(self, conn: mysql.connector, id: int):
        query = f"select count(id) from pokemonmer where nom='{self.nom}' and pokedex_id={id}"
        res = conn.cursor()
        res.execute(query)

        if res.fetchone() == 0:
            query = f"insert into pokemonmer values (0,'{self.nom}',{self.poids},{self.nb_nageoires},{id})"
            curseur = conn.cursor()
            curseur.execute(query)
            conn.commit()
            curseur.close()
        else:
            print("pokemon déjà la")


class PokemonCroisiere(PokemonEau):
    def __init__(self, nom : str, poids : float, nb_nageoires ):
        super().__init__(nom,poids,nb_nageoires)

    def vitesse(self) -> float:
        return self.poids/25 * self.nb_nageoires

    def save(self, conn: mysql.connector, id: int):
        query = f"select count(id) from pokemoncroisiere where nom='{self.nom}' and pokedex_id={id}"
        res = conn.cursor()
        res.execute(query)

        if res.fetchone() == 0:
            query = f"insert into pokemoncroisiere values (0,'{self.nom}',{self.poids},{self.nb_nageoires},{id})"
            curseur = conn.cursor()
            curseur.execute(query)
            conn.commit()
            curseur.close()
        else:
            print("pokemon déjà la")

class Pokedex ():
    def __init__(self,nom : str, liste : list[Pokemon] = []):
        self.__nom = nom
        self.__liste = liste

    def __str__(self) ->str:
        res = f"podekedx appartenant à {self.__nom} et contenant {self.nb()} pokemon(s): \n"
        for p in self.__liste:
            res += f"Pokemon {p.nom} de type {type(p)} \n"
        return res

    @property
    def nom(self) -> str:
        return self.__nom

    def ajout(self,p : Pokemon) ->bool:
        return self.__liste.append(p)

    def nb(self) -> int:
        return len(self.__liste)

    def save(self, conn: mysql.connector,):
        res = conn.cursor()
        query = f"select id from "


def main():
    print ("fonction principale")
    p1 : PokemonSportif = PokemonSportif("pikachu",18,2,0.85,120)
    p2 : PokemonCasanier = PokemonCasanier("Salameche",12,2,0.65,8)
    p3 : PokemonMer = PokemonMer ("Rondoudou",45,2)
    p4 : PokemonCroisiere = PokemonCroisiere("Bulbizarre",15,3)
    print(p1)
    print(p2)
    print(p3)
    print(p4)
    l =[p1,p2,p3,p4]
    print(l)

    print ("-----------pokedex --------------")
    poke :Pokedex = Pokedex("Arnauld",l)
    print(poke)

    print("-------------- DB ------------")
    myconnector = mysql.connector.connect(user="nono", password="nono",host="localhost", database="pokemon")
    curseur = myconnector.cursor()
    query = "show tables"
    curseur.execute(query)
    res = curseur.fetchall()
    for row in res:
        print(row)

    p1.save(myconnector,1)
    myconnector.close()



if __name__=="__main__":
    sys.exit(main())