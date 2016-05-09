# szyfrator wiadomości metodą Gronsfelda

# przykład: (ALAMAKOTA, K=12340) -> BNDQALQWE

klucz = input('Podaj liczbę całkowitą 0<=k<=1000000000 :')
wiadomość = input('Podaj tekst do zaszyfrowania :').upper()


tablica_przesunięć = []
for znak in klucz:
    tablica_przesunięć.append(int(znak))
długość_klucza = len(tablica_przesunięć)

n = 0
wyjscie = ''
for znak in wiadomość:
    przesunięcie = tablica_przesunięć[n % długość_klucza]
    if znak >= 'A' and znak <= 'Z':
        znak_wyjscie = ord('A') + (((ord(znak) - ord('A')) + przesunięcie) % 26) # kod znaku szyfru w tablicy ASCII 
        wyjscie = wyjscie + chr(znak_wyjscie)
    else:
        wyjscie = wyjscie + znak
    n += 1

print(wyjscie)
