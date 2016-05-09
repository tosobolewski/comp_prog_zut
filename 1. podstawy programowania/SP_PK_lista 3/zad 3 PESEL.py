#Zadanie 3 lista 3

pesel = input("Podaj PESEL :")

pesel = pesel.strip()

lista_wsp = [1,3,7,9,1,3,7,9,1,3,1]
suma = 0


# jeżeli PESEL ma nieprawidłową liczbę lub niewłasciwe znaki
if (len(pesel) != 11) or (pesel.isdigit == False):
    print("Nie podałeś prawidłowego numeru PESEL!")
else:
    # jeżeli PESEL jest w przybliżeniu OK
    for i in range(len(lista_wsp)):
        suma += lista_wsp[i] * int(pesel[i])

# sprawdzenie ...
if str(suma)[-1] =='0':
    print("wprowadzony PESEL posiada poprawną sumę kontrolną !")
else:
    print("Niepoprawna suma kontrolna numeru PESEL!")
