print("avant def f1")


def fonction2():
    print("dans f2")
    return 3


def fonction1():
    print("dans f1")
    return fonction2()


print("avant def f2")


print("avant appel de f1")
fonction1()
