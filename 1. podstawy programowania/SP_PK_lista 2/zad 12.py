#Zadanie 12 lista 2

from math import pow

lista = [1,2,3,4,5]

n = len(lista)

suma = 0
mianownik_do_sr_harmonicznej = 0
iloczyn = 1
suma_kwadratów = 0


for el in lista:
    suma += el
    mianownik_do_sr_harmonicznej += 1/el
    iloczyn *= el
    suma_kwadratów += el * el

print("Średnia arytmetyczna wynosi :", suma / n)
print("Średnia harmoniczna wynosi  :", n / mianownik_do_sr_harmonicznej)
print("Średnia geometryczna wynosi :", pow(iloczyn, 1/n))
print("Średnia kwadratowa wynosi   :", pow(suma_kwadratów/n, 1/2))
