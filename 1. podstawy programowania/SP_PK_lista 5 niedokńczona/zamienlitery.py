
def main():
    nazwawej = input('Podaj nazwę pliku wejściowego: ')
    nazwawyj = input('Podaj nazwę pliku wyjściowego: ')
    try:
        plikwej = open(nazwawej, 'r', encoding='UTF8')
    except IOError:
        print('Nie potrafię otworzyć pliku o nazwie', nazwawej)
        return False
    try:
        plikwyj = open(nazwawyj, 'w')
    except IOError:
        print('Nie potrafię utworzyć pliku o nazwie', nazwawyj)
        return False
    linia = plikwej.readline();
    while linia != '':
        linia = linia.upper()
        plikwyj.write(linia)
        linia = plikwej.readline()
    plikwyj.close()
    plikwej.close()
    return True

main()
                       

        
