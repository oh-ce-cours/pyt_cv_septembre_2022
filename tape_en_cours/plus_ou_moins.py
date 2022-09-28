import random


def jeu_plus_moins():
    while True:
        try:
            a = intt(input("Entrez un nombre entre 1 et 100 : "))
            break
        except:
            print("on a dit un nombre")

    nombre = random.randint(1, 100)
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
