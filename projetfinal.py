import datetime
import json


class Personne(object):
    # définition du constructeur
    def __init__(self, nom: str = "", prenom: str = ""):
        # initialisation des attributs
        self.set_nom(nom)
        self.set_prenom(prenom)

    def get_nom(self) -> str:
        return self.__nom

    def set_nom(self, value) -> None:
        if value.__len() > 6 and value.__len__() <= 20 and value[0].isupper():
            self.__nom = value

        else:
            raise ValueError("Votre nom doit être entre 5 et 15 caractères et commencer par une lettre majuscule.")

    def get_prenom(self) -> str:
        return self.__prenom

    def set_prenom(self, value) -> None:
        if value.__len() > 6 and value.__len__() <= 20 and value[0].isupper():
            self.__prenom = value

        else:
            raise ValueError("Votre nom doit être entre 5 et 15 caractères et commencer par une lettre majuscule.")


class Employe(object):
    # définition du constructeur
    def __init__(self, code: int = 0, fonction: str = ""):
        # initialisation des attributs
        self.set_code(code)
        self.set_fonction(fonction)

    def get_code(self) -> int:
        return self.__code

    def set_code(self, value) -> None:
        self.__code = value

    def get_fonction(self) -> str:
        return self.__fonction

    def set_fonction(self, value: str):
        self.__fonction = value


class Client(object):
    # définition du constructeur
    def __init__(self, telephone: str = "", courriel: str = ""):
        # initialisation des attributs
        self.set_telephone(telephone)
        self.set_courriel(courriel)

    def get_telephone(self) -> str:
        return self.__telephone

    def set_telephone(self, value: str):
        self.__telephone = value

    def get_courriel(self) -> str:
        return self.__courriel

    def set_courriel(self, value: str):
        self.__courriel = value


class Reparation(object):
    # definition du constructeur
    def __init__(self, code: int = 0, description: str = "", montant: float = 0, datereparation: datetime = "",
                 codeemploye: int = 0):
        self.set_code(code)
        self.set_description(description)
        self.set_montant(montant)
        self.set_datereparation(datereparation)
        self.set_codeemploye(codeemploye)

        # les méthodes d'acces avec encapsulation des attributs

    def get_code(self) -> int:
        return self.__code

    def set_code(self, value) -> None:
        self.__code = value

    def get_description(self) -> str:
        return self.__description

    def set_description(self, value: str):
        self.__description = value

    def get_montant(self) -> float:
        return self.__montant

    def set_montant(self, value) -> None:
        self.__montant = value

    def get_datereparation(self) -> datetime:
        return self.__datereparation

    def set_datereparation(self, value: datetime):
        self.__datereparation = value

    def get_codeemploye(self) -> int:
        return self.__codeemploye

    def set_codeemploye(self, value) -> None:
        self.__codeemploye = value


class Voiture(object):
    # definition du constructeur
    def __init__(self, numeroplaque: str = "", marque: str = "", modele: str = "", couleur: str = "",
                 annee: int = 0, proprietaire=Client, reparations=list[Reparation]):
        self.set_numeroplaque(numeroplaque)
        self.set_marque(marque)
        self.set_modele(modele)
        self.set_couleur(couleur)
        self.set_annee(annee)
        self.set_proprietaire(proprietaire)
        self.set_reparations(reparations)

        # les méthodes d'acces avec encapsulation des attributs

    def get_numeroplaque(self) -> str:
        return self.__numeroplaque

    def set_numeroplaque(self, value: str):
        self.__numeroplaque = value

    def get_marque(self) -> str:
        return self.__marque

    def set_marque(self, value: str):
        self.__marque = value

    def get_modele(self) -> str:
        return self.__modele

    def set_modele(self, value: str):
        self.__modele = value

    def get_couleur(self) -> str:
        return self.__couleur

    def set_couleur(self, value: str):
        self.__couleur = value

    def get_annee(self) -> int:
        return self.__annee

    def set_annee(self, value) -> None:
        self.__annee = value

    def get_proprietaire(self) -> Client:
        return self.__proprietaire

    def set_proprietaire(self, value: Client):
        self.__proprietaire = value

    def get_reparations(self) -> list:
        return self.__reparations

    def set_reparations(self, value: list):
        self.__reparations = list

    def ajouterreparation(self, reparations: Reparation) -> None:
        if not self.isexistajoutreparations(reparations):
            self.__ajoutreparations.append(reparations)
        else:
            raise ValueError("reparation existe dejà")


class Garage(object):
    # definition du constructeur
    def __init__(self, nom: str = "", adresse: str = "", telephone: str = "", employes=list[Employe],
                 voitures=list[Voiture]):
        self.set_nom(nom)
        self.set_adresse(adresse)
        self.set_telephone(telephone)
        self.set_employes(employes)
        self.set_voitures(voitures)

        # les méthodes d'acces avec encapsulation des attributs

    def get_nom(self) -> str:
        return self.__nom

    def set_nom(self, value: str):
        self.__nom = value

    def get_adresse(self) -> str:
        return self.__adresse

    def set_adresse(self, value: str):
        self.__adresse = value

    def get_telephone(self) -> str:
        return self.__telephone

    def set_telephone(self, value: str):
        self.__telephone = value

    def get_employes(self) -> list:
        return self.__employes

    def set_employes(self, value: list):
        self.__employes = list

    def get_voitures(self) -> list:
        return self.__voitures

    def set_voitures(self, value: list):
        self.__voitures = list

    def serialisergarage(cls, element: Garage, fichier: str) -> None:
        #  ouvrir le fichier (créer le stream)
        path: Path = Path(self.getchemin())
        stream = path.open("w")
        #  serialiser la valur vers le fichier
        json.dump(element, stream, default=Garage.converttodict)
        #  fermer le stream
        stream.close()

    def deserialisergarage(cls, fichier: str) -> Garage:
        #  ouvrir le fichier (créer le stream)
        path: Path = Path(self.getchemin())
        stream = path.open("r")
        #  deserialiser le fichier vers un objet etudiant
        fichier: fichier = json.load(stream, object_hook=Garage.converfromodict)
        #  fermer le stream
        stream.close()
        #  retourne le resultat
        return fichier

    def ajoutervoiture(self, element: Voiture) -> None:
        # vérifier si le compte n'existe pas déjà
        voiture: Voiture = self.rechercher(element.getnumero())
        if voiture is None:
            self.__voitures.append(element)
        else:
            raise ValueError("La voiture existe deja")

    def getvoiture(self, numvoiture: str) -> Voiture:
        return Garage.set_voitures(numvoiture)

    def ajouterreparation(self, numvoiture: str, reparation: Reparation) -> None:
        Voiture.ajouterreparation(numvoiture), reparation

    def getreparation(self, numvoiture: str) -> list[Reparation]:
        return Garage.getreparation(self, numvoiture)
