class Path:
    def __init__(self, path):
        self.path = path

    def __str__(self):
        return self.path

    def __truediv__(self, other:str):



p = Path(".")
intermediaire = p / "toto"
print(intermediaire)
q = intermediaire / "tata.txt"
print(p)  # "./toto/tata.txt"

# | ".\toto\tata.txt"
