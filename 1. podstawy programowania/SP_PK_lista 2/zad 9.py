#Zadanie 9 lista 2

lista = [ 1, 7, 5, 8, 5, 7, 1]
lista2 = []


# przepisz elementy do nowej listy w odwrotnej kolejności

for el in reversed(lista):
    lista2.append(el)

# porównaj obie listy

if lista != lista2:
    print("Lista nie jest palindromem")
else:
    print("Lista jest palindromem")

# KONIEC

print("lista oryginalna:             ",lista)
print("Lista w odwrotnej kolejności: ",lista2)

lista3 = list(reversed(lista))
print(lista3)
print("")
