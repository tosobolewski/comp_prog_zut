# zadanie 10 lista 3
# szyfr Cezara - szyfrator z dowolnym przesunięciem,
# dodano uwzglednianie spacji w tekscie

matryca = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # bez polskich znaków !
matryca = matryca + matryca #dla wartości przekraczających literę Z
wyjątki = ' '  # spacja

# wprowadzanie danych użytkownika

wiersz_użytkownika = input("Podaj wiersz tekstu do zaszyfrowania szyfrem Cezara: ")
wiersz_użytkownika = wiersz_użytkownika.upper()
przesunięcie = int(input('Podaj przesunięcie: '))


# dla wartości przesunięcia większych niż 26 (bo koniec matrycy przekroczony)
przesunięcie = przesunięcie % 26


# szyfrowanie

wynik = ''

for el in wiersz_użytkownika:
    
    if el in wyjątki:
        wynik = wynik + el
        continue
        
    poz1 = ord(el) - ord('A')
    
    if poz1 >= 0 and poz1 <= (ord('Z')-ord('A') ):
        wynik = wynik + matryca[poz1 + przesunięcie]
    else:
        print("Podano nieprawidłowy znak: ", '<',el, '>')
        print('Szyfrowanie zakończone.')
        break

    
# wynik końcowy

if len(wiersz_użytkownika) == len(wynik):
    print('szyfr Cezara: ', wynik)
else:
    print('Udało sie zaszyfrować jedynie fragment: ', \
          wynik.ljust(len(wiersz_użytkownika),'-'))
