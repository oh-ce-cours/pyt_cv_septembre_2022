def addition(x, y):
    # facile à tester
    return x + y


def lire_fichier(nom_fichier):
    # pas facile à tester
    # dépend du contenu et de l'existence du fichier
    return open(nom_fichier).readlines()


def entre_un_nombre():
    # pas facile à tester
    # pour la meme entrée, plein de résultats possibles
    return input()


# ce qui est facile à tester, ce sont des fonctions "pures"
# pour une entrée donnée, on a toujours le même résultat
