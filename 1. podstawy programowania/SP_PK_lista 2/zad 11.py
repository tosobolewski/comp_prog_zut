#Zad 11 lista 2

lista = [ 2, 6, 7, 1, 34, 64, 2, 7, 35, 100 ]

lista2 = [1, 35, 7, 2, 64, 34, 1, 7, 6, 2, 2, 6, 7, 1, 34, 64, 1000]

listy_takie_same = True


for el in lista:
    if not el in lista2:
        print("elementu ",el, " nie ma na drugiej liście")
        listy_takie_same = False

for el in lista2:
    if not el in lista:
        print("elementu ",el, " nie ma na pierwszej liście")        
        listy_takie_same = False


if listy_takie_same:
    print("Listy zawierają takie same elementy.")
