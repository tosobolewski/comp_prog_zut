
nazwa = input('Podaj nazwę pliku: ')

# open(nazwa,tryb)
#
# funkcja otwiera plik o nazwie podanej w pierwszym parametrze,
# przetwarzając go w sposób określony w drugim parametrze; w tym
# programi interesuje nas wyłącznie czytanie pliku, dlatego też
# użyjemy trybu oznaczanego jako 'r' (od ang. read - czytać);
# można również określić, jakie kodowanie znaków narodowych
# ma być brane pod uwagę w czasie odczytywania pliku (encoding)
# funkcja zwraca jako rezultat tajemniczy obiekt reprezentujący
# otwarty plik; jeśli otwarcie pliku się nie uda, funkcja podniesie
# wyjątek klasy IOError

try:
    plik = open(nazwa, 'r',encoding='UTF8')

# .readline()
#
# metoda odczytuje jedną linię tekstu z otwartego pliku;
# jeśli w pliku nie ma już więcej danych, metoda zwraca łańcuch pusty
# znaki końca linii pochodzące z pliku są zachowywane

    nrlinii = 1
    linia = plik.readline();
    while(linia != ''):
        linia = linia.replace('\n','').replace('\r','')
        print('Linia nr', nrlinii, ':', linia)
        nrlinii += 1
        linia = plik.readline()
    print('*** KONIEC PLIKU ***')

# .close()
#
# metoda zamyka otwarty plik; od tego momentu plik staje się
# niedostępny

    plik.close()
except IOError:
    print('Nie potrafię otworzyć pliku o nazwie', nazwa)

        
