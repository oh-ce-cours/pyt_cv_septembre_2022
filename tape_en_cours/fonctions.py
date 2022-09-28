print("avant def nouvelle")


def ma_nouvelle_fonction():
    print("dans nouvelle")
    return ma_nouvelle_fonction_autre()


print("avant def autre nouvelle")


def ma_nouvelle_fonction_autre():
    print("dans autre nouvelle")
    return 3


print("avant appel de nouvelle")
ma_nouvelle_fonction()
