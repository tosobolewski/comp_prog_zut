# Zadanie 6 lista 3

def czyAdresEmail(napis):

    # czy napis może być adresem e-mail ?

    #usuń spacje i zamień duże na małe litery
    napis = napis.strip()
    napis = napis.lower()


    #definicje grup znaków
    litery = 'abcdefghijklmnopqrstuwxyz'
    cyfry = '0123456789'
    łączniki = '_-'
    kropka = '.'

    #zmienna testowa
    test = True


    # jezeli brak @ lub więcej niż jedna @ to NIE JEST ADRES EMAIL:
    if napis.count('@') != 1:
        test = False

    # jezeli jedna @ to sprawdzaj dalej:    
    else:
        # podziel adres na dwie częsci
        lista = napis.split('@')
        nazwaUzytkownika = lista[0]
        nazwaDomeny = lista[1]

        # czy nazwa użytkownika jest dłuższa niż 0 (min. 1 znak)
        if len(nazwaUzytkownika) == 0:
            test = False

        # czy nazwa domeny jest dłuższa niż 0 (min. 1 znak)
        if len(nazwaDomeny) == 0:
            test = False

        # czy nazwa użytkownika nie zaczyna się znakiem specjalnym '_' lub '-'
        if nazwaUzytkownika[0] in (łączniki + kropka):
            test = False
        


        # podziel nazwy kropkami 
        listaU = nazwaUzytkownika.split('.')
        listaD = nazwaDomeny.split('.')
        



        # czy są niedozwolone znaki w liscie elementów nazwy użytkownika
        for el in listaU:
            if len(el) == 0: # adres zaczyna się od kropki lub 2 kropki obok siebie
                test = False
            else:
                 es = el.strip(litery + cyfry + łączniki)
                 if len(es) != 0: # pozostały niedozwolone znaki
                     test = False




        # czy są niedozwolone znaki w liscie elementów nazwy domenny
        for el in listaD:
            if len(el) == 0: # domena zaczyna się od kropki lub 2 kropki obok siebie
                test = False
            else:
                 es = el.strip(litery + cyfry + łączniki)
                 if len(es) != 0: # pozostały niedozwolone znaki
                     test = False    


    return test

#
#   PROGRAM:
#

#napis = input("Podaj napis :")


#
#   TESTY
#


lista_testów = ['abc@wp.pl', 'ABC@@wp.pl', 'aaa@wp.pl.pl.pl', \
                '_aaa@wp.pl.pl.pl',\
                # dwie kropki obok siebie
                'a..b@wp.pl', 'ab@wp...pl']

for el in lista_testów:   
    print(el,'\t',czyAdresEmail(el))








##    if test == True:
##        print('To jest adres e-mail')
##    else:
##        print('Nie jest to adres e-mail')
    






