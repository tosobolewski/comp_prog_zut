#Zadanie 10 lista 2

lista = [ 2, 6, 7, 1, 34, 64, 2, 7, 35, 100 ]

lista2 = [1, 35, 7, 2, 64, 34, 1, 7, 6, 2, 2, 6, 7, 1, 34, 64, 1000]

lista3 = []

for el in lista:
    if el not in lista2:
        lista3.append(el)

for el in lista2:
    if el not in lista:
        lista3.append(el)

print(lista3)
