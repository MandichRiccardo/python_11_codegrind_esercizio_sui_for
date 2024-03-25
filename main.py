# esercizio 1
print("esercizio 1")
lista = ["penna", "matita", "gomma", "righello"]
for i in lista:
    print(i)
# esercizio 2
print("esercizio 2")
for i in range(1, 11):
    print(i)
# esercizio 3
print("esercizio 3")
numeri = list(range(1, 11, 2))
somma = 0
for i in numeri:
    print(i)
    somma = somma + i
print(somma)
# esercizio 4
print("esercizio 4")
for i in range(2, 21, 2):
    print(i)
# esercizio 5
print("esercizio 5")
for i in "stringa":
    print(i)
# esercizio 6
print("esercizio 6")
dizionario = {"nome": "Mario", "cognome": "Rossi", "eta": 30}
for i in dizionario:
    print(i)
# esercizio 7
print("esercizio 7")
for chiave, valore in dizionario.items():
    print(chiave, ":", valore)
# esercizio 8
print("esercizio 8")
for i in lista:
    for j in i:
        print(j)
    print("")
# esercizio 9
print("esercizio 9")
a = "a"
h = 0
for i in lista[1]:
    if i == a:
        h += 1
print("la a compare " + str(h) + " volte in " + lista[1])
# esercizio 10
print("esercizio 10")
numeri = list(range(1, 11, 2))
somma = 0
for i in numeri:
    somma = somma + i
somma = somma/len(numeri)
print(somma)