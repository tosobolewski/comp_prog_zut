# zadanie 13 lista 3

tekst = (input('Podaj tekst: ')).upper()

lista = [0] * 26

for el in tekst:
    if el >= 'A' and el <= 'Z':
        lista[ord(el)-ord('A')] += 1

for i in range(0,len(lista)):
    if lista[i] != 0:
        print(chr(ord('A') + i), lista[i] )
