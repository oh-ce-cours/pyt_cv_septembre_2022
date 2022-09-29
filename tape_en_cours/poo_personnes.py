from datetime import date


class Personne:
    AGE_MAJORITE = 18

    def __init__(self, annee_de_naissance, nom):
        self.annee_naissance = annee_de_naissance
        self.nom = nom

    def est_majeur(self):
        return date.today().year - self.annee_naissance >= self.AGE_MAJORITE

    def __str__(self):
        if self.est_majeur():
            return f"Bonjour, je suis {self.nom}, je suis né en {self.annee_naissance} et je suis majeur"
        else:
            return f"Bonjour, je suis {self.nom}, je suis né en {self.annee_naissance} et je suis mineur"


personne1 = Personne(1990, "Matthieu")
personne2 = Personne(1995, "Matthieu")

print(personne1 > personne2)

Personne.AGE_MAJORITE = 40
personne1.AGE_MAJORITE = 15  # on a masqué la variable de classe avec un attribut
print(
    f"Nom {personne1.nom}, date de naissance {personne1.annee_naissance}, Majeur ? {personne1.est_majeur()}"
)
