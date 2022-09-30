class Path:
    def __init__(self, path, plateforme):
        self.path = path
        self.plateforme = plateforme
        if plateforme == "windows":
            self.separateur = "\\"
        else:
            self.separateur = "/"

    def __str__(self):
        return self.path

    def append_path(self, other):
        res = self.path + self.separateur + other
        return Path(res, self.plateforme)

    def __truediv__(self, other: str):
        return self.append_path(other)


class WindowsPath(Path):
    pass


class UnixPath(Path):
    pass


p = Path(".", "windows")
intermediaire = p / "toto"
print(type(intermediaire), intermediaire)  # "./toto"
q = intermediaire / "tata.txt"
print(q)  # "./toto/tata.txt"

# | ".\toto\tata.txt"
