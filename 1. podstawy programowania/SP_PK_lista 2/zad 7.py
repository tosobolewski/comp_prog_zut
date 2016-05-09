#Zadanie 7 lista 2

lista = [ 2, 6, 7, 1, 34, 64, 2, 7, 35, 1 ]
print()
print(lista)
print("---------------------------------")

for i in range(0,len(lista)):
    test = lista[i]
    dl_listy = len(lista)
    print("szukam elementu ",lista[i]," w liscie postaci: ", lista)
    for j in range(i+1,dl_listy):
        if lista[j] == test:
            del lista[j]
            dl_listy -= 1
            print("usuniety element na poz =",j+1,"  nowa dł listy = ", dl_listy)
            print(lista)
            break

