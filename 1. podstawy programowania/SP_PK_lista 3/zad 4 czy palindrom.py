# Zadanie 4 lista 3

napis1 = input("Podaj napis :")
napis2 = ''
#napis3 = reversed(napis1)

for i in range(len(napis1)):
    napis2 += napis1[-(i+1)]


print("Napis 2 = ", napis2)
    
if napis1 == napis2:
    print("Napis", napis1, "jest palindromem!")
else:
    print("Napis nie jest palindromem!")

