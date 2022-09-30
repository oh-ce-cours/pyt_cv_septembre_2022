class Path:
    pass


p = Path(".")
q = p / "toto" / "tata.txt"
print(p)  # "./toto/tata.txt"

# | ".\toto\tata.txt"
