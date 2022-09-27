def cat():
    f = open("./fizzbuzz.py", encoding="utf8")
    for line in f.readlines():
        line = line.rstrip()
        print(line)
    f.close()


def tac():
    f = open("./fizzbuzz.py", encoding="utf8")
    for line in f.readlines()[::-1]:
        line = line.rstrip()
        print(line)
    f.close()


def head(nombre_de_lignes_a_afficher):
    f = open("./fizzbuzz.py", encoding="utf8")
    for line in f.readlines()[:nombre_de_lignes_a_afficher]:
        line = line.rstrip()
        print(line)
    f.close()


def tail(nombre_de_lignes_a_afficher=5):
    f = open("./fizzbuzz.py", encoding="utf8")
    for line in f.readlines()[-nombre_de_lignes_a_afficher:]:
        line = line.rstrip()
        print(line)
    f.close()


def autre():
    f = open("./fizzbuzz.py", encoding="utf8")
    for line in f.readlines()[5:-10:3]:
        line = line.rstrip()
        print(line)
    f.close()


autre()
