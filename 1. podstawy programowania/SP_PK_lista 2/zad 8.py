#Zadanie 8 lista 2

lista = [ 2, 6, 7, 1, 34, 64, 2, 7, 35, 1 ]
nowa_lista = []


for i in range(len(lista)):
    print(lista[i])
    nowa_lista.append(lista[len(lista)-1-i])


print(lista)
print(nowa_lista)






# test test test

lista = [ 2, 6, 7, 1, 34, 64, 2, 7, 35, 1 ]
nowa_lista = []


for el in reversed(lista):
    print(el)
    nowa_lista.append(el)


print(lista)
print(nowa_lista)
