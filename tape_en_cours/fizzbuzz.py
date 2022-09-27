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
for nombre in range(1, 101):
    resultat = ""
    # "fizzbuzz" = "fizz" + "buzz"
    if nombre % 3 == 0:
        resultat = resultat + "fizz"
    if nombre % 5 == 0:
        resultat = resultat + "buzz"

    if resultat == "":
        resultat = str(nombre)

    print(resultat)
