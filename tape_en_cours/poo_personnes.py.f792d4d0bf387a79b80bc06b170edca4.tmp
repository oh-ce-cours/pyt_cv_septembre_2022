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

    def __gt__(self, other):
        if isinstance(other, Personne):
            return self.__gt_personne__(other)
        elif isinstance(other, int):
            return self.__gt_int__(other)
        else:
            raise TypeError(
                f"comparaison not suported between person and {type(other)}"
            )

    def __gt_personne__(self, other):
        return self.annee_naissance < other.annee_naissance

    def __gt_int__(self, other: int):
        return self.annee_naissance < other

    def __ge__(self, other):
        if not isinstance(other, Personne):
            raise TypeError("can only compare 2 Personnes")
        return self.annee_naissance <= other.annee_naissance


class Eleve(Personne):
    # prend un nouvel attribut => a_payer
    def __init__(self, annee_de_naissance, nom, a_paye=False):
        super().__init__(annee_de_naissance, nom)
        self.a_paye = a_paye


class Formateur(Personne):
    # possède une méthode de plus
    def est_ce_que_l_eleve_a_paye(self, eleve: Eleve) -> bool:
        return eleve.a_paye


eleve1 = Eleve(1990, "Joel", True)
f = Formateur(1990, "Matthieu")
print(f"{f.est_ce_que_l_eleve_a_paye(eleve1)=}")


class Formation:
    def __init__(self, eleves, formateur):
        self.eleves = eleves
        self.formateur = formateur


personne1 = Personne(1990, "p1")
personne2 = Personne(1995, "p2")

# print("***********")
# print(personne1 <= personne2)  # => personne1.__gt__(personne2)
# print("***********")

# Personne.AGE_MAJORITE = 40
# personne1.AGE_MAJORITE = 15  # on a masqué la variable de classe avec un attribut
# print(
#     f"Nom {personne1.nom}, date de naissance {personne1.annee_naissance}, Majeur ? {personne1.est_majeur()}"
# )
