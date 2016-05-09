# Spirala wersja prosta


bok = int(input('Podaj bok spirali : '))              # podaj bok spirali

if bok == 1:    # jeżeli wymiar 1 x 1 to oczywiście  wynik => 1
    print(1)
else:
    print((bok * bok) - (bok -1) - (bok-1))  # liczba na polu w prawym dolnym rogu

