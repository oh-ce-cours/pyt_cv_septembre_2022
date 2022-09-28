## Solution 1
# for nombre in range(1, 101):
#     if nombre % 5 == 0 and nombre % 3 == 0:
#         print("fizzbuzz")
#     elif nombre % 3 == 0:
#         print("fizz")
#     elif nombre % 5 == 0:
#         print("buzz")
#     else:
#         print(nombre) 

## Solution 2 (sans les elif)
# for nombre in range(1, 101):
#     resultat = ""
#     # "fizzbuzz" = "fizz" + "buzz"
#     if nombre % 3 == 0:
#         resultat = resultat + "fizz"
#     if nombre % 5 == 0:
#         resultat = resultat + "buzz"
#     if resultat:
#         resultat = str(nombre)
#     print(resultat)

## Solution 3 (sans les if)
for nombre in range(1, 101):
    gauche_plus = "fizz" * (nombre % 3 == 0)
    droite_plus = "buzz" * (nombre % 5 == 0)
    gauche = gauche_plus + droite_plus
    droite = str(nombre)
    print(gauche or droite)
    # version en une ligne
    # print("fizz" * (nombre % 3 == 0) + "buzz" * (nombre % 5 == 0) or str(nombre))


## Solution 4 avec match / case (python >= 3.10)
# for nombre in range(1, 101):
#     match (nombre % 3, nombre % 5):
#         case (0, 0):
#             print("fizzbuzz")
#         case (0, _):
#             print("fizz")
#         case (_, 0):
#             print(f"buzz")
#         case _, _:
#             print(nombre)
