# zadanie 9 lista 3

liczba_str = input('Podaj datę urodzenia: ')
suma = 0

while len(liczba_str) != 1:
    for el in liczba_str:
        if el.isdigit():
            suma += int(el)
    liczba_str = str(suma)
    suma = 0
    #print(liczba_str, suma)

print('Twoja liczba życia wynosi ', liczba_str)
        
