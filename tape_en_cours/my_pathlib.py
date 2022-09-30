class Path:
    def __init__(self, path):
        self.path = path
        self.separateur = "/"

    def __str__(self):
        return self.path

    def append_path(self, other):
        res = self.path + self.separateur + other
        self.path = res
        return self

    def __truediv__(self, other: str):
        return self.append_path(other)


p = Path(".")
intermediaire = p / "toto"
print(type(intermediaire), intermediaire)  # "./toto"
q = intermediaire / "tata.txt"
print(q)  # "./toto/tata.txt"

# | ".\toto\tata.txt"
