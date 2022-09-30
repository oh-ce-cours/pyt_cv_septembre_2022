class Path:
    def __init__(self, path):
        self.path = path
        self.separateur = self.get_separator()

    def __str__(self):
        return self.path

    def append_path(self, other):
        res = self.path + self.separateur + other
        CorrectPath = type(self)
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


p = UnixPath(".")
intermediaire = p / "toto"
print(type(intermediaire), intermediaire)  # "./toto"
q = intermediaire / "tata.txt"
print(q)  # "./toto/tata.txt"

# | ".\toto\tata.txt"
