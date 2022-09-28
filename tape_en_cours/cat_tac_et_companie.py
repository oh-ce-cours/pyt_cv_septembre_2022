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


def wc_paresseux():
    f = open("./fizzbuzz.py", encoding="utf8")
    count = 0
    for _ in f:
        count += 1
    f.close()
    print(f"Il y a {count} lignes dans le fichier")


def cat_paresseux():
    f = open("./fizzbuzz.py", encoding="utf8")
    for line in f:
        line = line.rstrip()
        print(line)
    f.close()


def head_paresseux_1():
    f = open("./fizzbuzz.py", encoding="utf8")
    line_counter = 1
    for line in f:
        line = line.rstrip()
        print(line)
        line_counter += 1
        if line_counter > 10:
            break
    f.close()


def head_paresseux():
    f = open("./fizzbuzz.py", encoding="utf8")
    for item in zip(f, range(10)):
        line, index = item
        # line = item[0]
        # index = item[1]
        line = line.rstrip()
        print(line)
    f.close()


head_paresseux()
