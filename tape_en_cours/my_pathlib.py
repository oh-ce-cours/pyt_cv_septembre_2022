class Path:
    def __init__(self, path):
        self.path = path

    def __str__(self):
        return self.path


p = Path(".")
intermediaire = p / "toto"
q = intermediaire / "tata.txt"
print(p)  # "./toto/tata.txt"

# | ".\toto\tata.txt"
