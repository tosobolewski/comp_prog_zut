# Spirala


def spirala(bok):
    if bok % 2 == 0:
        return None
    n = 1
    while n <= bok:
        if n == 1:
            wynik = 1
        else:
            wynik = wynik + 4 * (n - 2)
        n += 2
    return wynik


bok = int(input('Podaj bok spirali : '))
print('Dla boku', bok, 'wynik ',spirala(bok))
