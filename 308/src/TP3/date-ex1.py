from datetime import date, datetime
import locale
locale.setlocale(locale.LC_ALL, 'fr_FR')
import sys
from dateparser import parse
class Personne:
    """
    classe définissant une personne

    .. py:attribute:: nom

        le nom de famille de la personne
        :type: str

    .. py:attribute:: prenom

        le prenom de la personne
        :type: str

    .. py:attribute:: dateNaissance

        la date de naissance de la personne
        :type: date
    """

    def __init__(self,nom:str,prenom:str,datenaissance: date):
        self.__nom = nom
        self.__prenom = prenom
        if isinstance(datenaissance,date):
            self.__dateNaissance=datenaissance

    def __str__(self):
        return f"Personne Nom: {self.__nom} prénom : {self.__prenom} né(e) le {self.__dateNaissance.strftime('%d %B %Y')}"

def main():
    d1 = date(1975,11,23)
    personne1 = Personne("ALBERT","Arnauld",d1)
    print(personne1)


    nom = input("saisir le nom : ")
    prenom = input("saisir le prenom: ")
    date2 = str(input("saisir la date de naissance (dd/mm/yyyy): "))
    d2 = datetime.strptime(date2,"%d/%m/%Y")
    personne2= Personne(nom,prenom,d2)
    print (personne2)

    date3= input("saisissez une date de naissance")
    d3=parse(date3)
    print(d3.strftime("%d/%m/%Y"))


if __name__=="__main__":
    sys.exit(main())