class Path:
    def __init__(self, path):
        self.path = path
        self.separateur = "/"

    def __str__(self):
        return self.path

    def __truediv__(self, other: str):
        res = self.path + separateur + other


p = Path(".")
intermediaire = p / "toto"
# print(intermediaire) # "./toto"
# q = intermediaire / "tata.txt"
# print(p)  # "./toto/tata.txt"

# | ".\toto\tata.txt"
