from datetime import date


class Personne:
    AGE_MAJORITE = 18

    def __init__(self, annee_de_naissance, nom):
        self.annee_naissance = annee_de_naissance
        self.nom = nom

    def est_majeur(self):
        return date.today().year - self.annee_naissance >= AGE_MAJORITE


personne1 = Personne(1990, "Matthieu")

print(
    f"Nom {personne1.nom}, date de naissance {personne1.annee_naissance}, Majeur ? {personne1.est_majeur()}"
)

AGE_MAJORITE = 40
print(
    f"Nom {personne1.nom}, date de naissance {personne1.annee_naissance}, Majeur ? {personne1.est_majeur()}"
)
