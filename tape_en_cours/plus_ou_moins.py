import random


def jeu_plus_moins():
    a = int(input("Entrez un nombre entre 1 et 100 : "))
    try:
        nombre = random.randint(1, 100)
    except:
        print("on a dit un nombre")
    print(nombre)
    while a != nombre:
        if a < nombre:
            print("Plus !")
            a = int(input("Testez à nouveau ! : "))
        else:
            print("Moins !")
            a = int(input("Testez à nouveau ! : "))
    print("C'est gagné !")


jeu_plus_moins()
