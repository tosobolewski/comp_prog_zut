# Zadanie 1 lista 3


def main():
    imie = input("Podaj imię : ")
    
    # obciecie ewentualnych białych znaków na końcach
    # sprawdzenie, czy napis nie jest pusty
    # i zamiana wielkości liter na schemat 'duża litera + pozostałe małe'
    imie = imie.strip()
    if(imie == ''):
        print("Nie podałeś imienia, nie mogę Ci pomóc!")
        return
    imie = imie.capitalize()

    # definicja wyjątków imion męskich
    lista_wyjatkow = ["Kuba","Bonawentura"]
    wyjatek = False


    # test wyjątków
    for el in lista_wyjatkow:
        if imie == el:
            wyjatek = True
            break

    # sprawdzenie 'płci' imienia i wydruk wyniku
    if imie.endswith("a") and not wyjatek:
        print(imie + ", jesteś kobietą!")
    else:
        print(imie, ", jesteś mężczyzną!",sep='')

main()
