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
        return self.append_path(other)

    def get_separator(self):
        return ""


class WindowsPath(Path):
    def get_separator(self):
        return "\\"


class UnixPath(Path):
    def get_separator(self):
        return "/"


p = WindowsPath(".")
intermediaire = p / "toto"
print(type(intermediaire), intermediaire)  # "./toto"
q = intermediaire / "tata.txt"
print(q)  # "./toto/tata.txt"

# | ".\toto\tata.txt"
