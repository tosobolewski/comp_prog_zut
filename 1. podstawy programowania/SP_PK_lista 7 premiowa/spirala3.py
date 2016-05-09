# Spirala rekurencyjna
# Spirala


def spiralaRekurencyjna(we):
    print('we = ',we)
    if we % 2 == 0: # liczby parzyste odpadają!
        return None
    if we == 1:     # dla 1 zawsze wynik będzie 1
        return 1
    else:           # poniżej są obliczenia
        print('....we - 2 , spiralaRekurencyjna(we-2) :',we-2, spiralaRekurencyjna(we-2))
        wy = spiralaRekurencyjna(we-2) + 4 * (we-2)
        return wy


def spirala(we):
    if we % 2 == 0:
        return None
    n = 1
    while n <= we:
        if n == 1:
            wynik = 1
        else:
            wynik = wynik + 4 * (n - 2)
        n += 2
    return wynik

print('.............................................')
s7 = spiralaRekurencyjna(7)
print(s7)
print('.............................................')
s13 = spiralaRekurencyjna(13)
print(s13)
print('.............................................')

print(spirala(7))
