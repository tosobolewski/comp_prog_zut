#szyfr Cezara

# przykład:  (PYTHON, p=1) -> QZUIPO

s = input('Podaj tekst do szyfrowania: ').upper()
p = int(input('Podaj przesunięcie: '))
sc = ''

for znak in s:
    if znak >= 'A' and znak <= 'Z':
        znak_sc = ord('A') + (((ord(znak) - ord('A')) + p) % 26) # kod znaku szyfru w tablicy ASCII 
        sc = sc + chr(znak_sc)
    else:
        sc = sc + znak
print(sc)
