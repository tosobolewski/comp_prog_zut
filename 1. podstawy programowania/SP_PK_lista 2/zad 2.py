# Zadanie 2 lista 2

klocki = int(input("Podaj ilość klocków: "))
print("Podałeś: ", klocki)

warstwa = 1
klocki_w_warstwie_n = 1

if klocki == 0 :
    print("nie można ułożyć piramidy")
else:
    while klocki >= klocki_w_warstwie_n :
        klocki -= klocki_w_warstwie_n
        warstwa += 1
        klocki_w_warstwie_n += 1
    print("można ułożyć ", warstwa -1," warstw z podanej ilości klocków")
    print("pozoistanie ", klocki," klocków")
        
