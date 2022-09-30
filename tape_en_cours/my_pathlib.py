class Path:
    def __init__(self, path):
        self.path = path


p = Path(".")
# q = p / "toto" / "tata.txt"
print(p)  # "./toto/tata.txt"

# | ".\toto\tata.txt"
