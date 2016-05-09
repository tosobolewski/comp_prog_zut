# Spirala rekurencyjna



def spiralaRekurencyjna(bok):
    if bok % 2 == 0: # liczby parzyste odpadają!
        return None
    if bok == 1:     # dla 1 zawsze wynik będzie 1
        return 1
    else:           # poniżej są obliczenia
        wy = spiralaRekurencyjna(bok-2) + 4 * (bok-2)
        return wy


bok = int(input('Podaj bok spirali : '))
print('Dla boku', bok, 'wynik ',spiralaRekurencyjna(bok))
