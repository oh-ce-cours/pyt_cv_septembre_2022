class Path:
    def __init__(self, path):
        """Un constructeur qui prend le chemin de base"""
        self.path = path
        self.separateur = self.get_separator()

    def __str__(self):
        """La méthode pour afficher notre objet (nous n'affichons que le path)"""
        return self.path

    def append_path(self, other):
        """
        La méthode coeur de l'objet qui rajoute le chemin passé
        en argument au chemin courant et crée un nouvel objet.
        """
        res = self.path + self.separateur + other
        CorrectPath = type(
            self
        )  # on ne sait pas à l'avance quel est le type de self, soit un Path, soit un WindowsPath soit un UnixPath
        return CorrectPath(res)

    def __truediv__(self, other: str):
        """
        On supporte la division '/' et on retourne un nouvel
        objet du meme type que l'objet courant.
        """
        return self.append_path(other)

    def get_separator(self):
        """Surchargé dans les classes filles.
        Dans ce cas, on pourrait utiliser une classe abstraite comme expliqué ici :
         https://www.geeksforgeeks.org/abstract-classes-in-python/
        """
        return ""


class WindowsPath(Path):
    """Une classe permettant de générer des chemins windows"""

    def get_separator(self):
        return "\\"


class UnixPath(Path):
    """Une classe permettant de générer des chemins Unix (linux / macOS)"""

    def get_separator(self):
        return "/"


print("dans my_pathlib", __name__)
# if ce_fichier_est_execute_directement:
p = WindowsPath(".")
intermediaire = p / "toto"
print(type(intermediaire), intermediaire)  # "./toto"
q = intermediaire / "tata.txt"
print(q)  # "./toto/tata.txt"
print("toto")
